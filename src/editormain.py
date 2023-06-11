import os

import sass
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (QComboBox, QDesktopWidget, QFileDialog,
                             QListWidgetItem, QMainWindow, QMenu, QPushButton,
                             QWidget)
from ui.ElemQssEditor import Ui_ElemQssEidtorMainWindow
from utils.sassHighLight import SassHighlighter
from utils.shortCutKeys import ShortCutKeys
from widgets.codeeditor import CodeEditor
from widgets.codeprompt import CodePrompt


class EditorMain(QMainWindow, Ui_ElemQssEidtorMainWindow):

    OPEN_FILE_NUM = 0
    OPEN_FILE_LIST = []
    CODE_EDITORS = []

    def __init__(self):
        super(EditorMain, self).__init__()
        self.Keys = ShortCutKeys().key_dict
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # 初始化无边框窗口
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 菜单
        self.fileMenu = QMenu(self)
        self.fileMenu.setObjectName("fileMenu")
        self.fileMenu.setAttribute(Qt.WA_TranslucentBackground)
        self.fileMenu.addAction("新建", self.newFile, self.Keys["NEW_FILE"])
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("打开.sass文件", self.openFile, self.Keys["OPEN_FILE"])
        self.fileMenu.addAction("打开文件夹", self.openFolder, self.Keys["OPEN_FOLDER"])
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("保存", self.saveFile, self.Keys["SAVE_FILE"])
        self.fileMenu.addAction("另存为", self.saveFileAs, self.Keys["SAVE_FILE_AS"])
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("退出", self.close, self.Keys["QUIT"])
        self.fileBtn.setMenu(self.fileMenu)

        self.editMenu = QMenu(self)
        self.editMenu.setObjectName("editMenu")
        self.editMenu.setAttribute(Qt.WA_TranslucentBackground)
        self.editMenu.addAction("撤销", self.undo, self.Keys["UNDO"])
        self.editMenu.addAction("重做", self.redo, self.Keys["REDO"])
        self.editMenu.addSeparator()
        self.editMenu.addAction("剪切", self.cut, self.Keys["CUT"])
        self.editMenu.addAction("复制", self.copy, self.Keys["COPY"])
        self.editMenu.addAction("粘贴", self.paste, self.Keys["PASTE"])
        self.editMenu.addSeparator()
        self.editMenu.addAction("查找")
        self.editMenu.addAction("替换")
        self.editBtn.setMenu(self.editMenu)

        # 加载全局QSS
        self.reloadQss()
        # self.reloadBtn.clicked.connect(self.reloadQss)

        # 选择文件
        self.listWidget.itemClicked.connect(self.selectFile)

        # 获取当前显示器分辨率
        self.screen = QDesktopWidget().screenGeometry()
        self.screenWidth = self.screen.width()

        # 初始化分裂窗口
        self.SIZE = [320,1600,self.screenWidth-320-1600]
        self.splitter.setSizes(self.SIZE)

        # hoempage
        self.stackedWidget.setCurrentIndex(0)
        # self.splitter.splitterMoved.connect(self.recordSizes)

        # 绑定窗口控制按钮
        self.minBtn.clicked.connect(self.showMinimized)
        self.closeBtn.clicked.connect(self.close)
        self.maxBtn.clicked.connect(self.maximize)

        # 初始化左侧按钮
        self.processBtn.setCheckable(True)
        self.processBtn.setChecked(True)
        self.processBtn.clicked.connect(lambda: self.select(self.processBtn))
        self.documentBtn.clicked.connect(lambda: self.select(self.documentBtn))
        self.searchBtn.clicked.connect(lambda: self.select(self.searchBtn))
        self.settingBtn.clicked.connect(lambda: self.select(self.settingBtn))
        self.githubBtn.clicked.connect(lambda: self.select(self.githubBtn))

        # 删除tabWidget的第二个tab
        self.EditorTabWidget.removeTab(1)
        self.EditorTabWidget.removeTab(0)

    '''Logic Func below'''

    def reloadQss(self):
        '''加载全局QSS'''
        with open('.\\resource\\\qss\\MainWindow_DarkStyle.scss', 'r') as f:
            scss = f.read()

        qss = sass.compile(string=scss)
        self.setStyleSheet(qss)
        self.QSS = qss

    def select(self, btn):
        '''左侧按钮点击事件'''
        tag_functionName = {
            'process': "项目文件夹",
            'document': "文档",
            'table': "表格",
            'image': "图片",
            'search': "搜索",
            'history': "历史版本",
            'todo': "日程待办",
            'setting': "设置",
            'github': "GitHub"
        }

        for btnObj in self.leftWidget.children():
            if isinstance(btnObj, QPushButton):
                btnObj.setCheckable(True)
                if btnObj.objectName() != btn.objectName():
                    btnObj.setChecked(False)
                else:
                    btnObj.toggle()
                    btnObj.setChecked(True)
                    self.functionLabel.setText(tag_functionName[btn.objectName().replace('Btn', '')])
            else:
                continue
    
    def maximize(self):
        '''最大化窗口'''
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    '''菜单Actions'''
    def openFile(self):
        '''打开单独的文件'''
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        self.stackedWidget.setCurrentIndex(1)
        if fileName:
            if self.OPEN_FILE_NUM == 0:
                curCodeEditor = CodeEditor(filelist=self.OPEN_FILE_LIST)
                curCodeEditor.loadFile(fileName)
                self.EditorTabWidget.addTab(curCodeEditor, fileName.split('/')[-1])
                self.OPEN_FILE_NUM += 1
                self.OPEN_FILE_LIST.append(fileName)
            else:
                if fileName in self.OPEN_FILE_LIST:
                    self.changeTabTitle(self.OPEN_FILE_LIST.index(fileName), fileName.split('/')[-1])
                else:
                    curCodeEditor = CodeEditor(filelist=self.OPEN_FILE_LIST)
                    curCodeEditor.loadFile(fileName)
                    self.EditorTabWidget.addTab(curCodeEditor, fileName.split('/')[-1])
                    self.OPEN_FILE_LIST.append(fileName)
                    self.EditorTabWidget.setCurrentIndex(self.OPEN_FILE_NUM)
                    self.OPEN_FILE_NUM += 1

            self.updatePreview()
        else:
            pass
    
    def saveFile(self):
        '''保存文件'''
        currentEditor = self.getCurrentEditor()
        if currentEditor is not None:
            filename = currentEditor.filename
            if filename:
                text = currentEditor.toPlainText()
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text)
                print("File saved:", filename)
            else:
                self.saveFileAs()
        self.updatePreview()

    def saveFileAs(self):
        '''另存为文件'''
        currentEditor = self.getCurrentEditor()
        if currentEditor is not None:
            dialog = QFileDialog()
            dialog.setDefaultSuffix(".sass")
            filename, _ = dialog.getSaveFileName(self, "Save File As", "", "Sass Files (*.sass);;All Files (*.*)")
            if filename:
                currentEditor.filename = filename
                self.changeTabTitle(self.getCurrentTabIndex(), os.path.basename(filename))
                self.saveFile()

    def openFolder(self):
        '''打开文件夹'''
        folderName = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.projectFolder = folderName
        if folderName:
            self.functionLabel.setText(folderName)
            self.projectTitleLabel.setText(folderName.split('/')[-1])
            self.listWidget.clear()
            for file in os.listdir(self.projectFolder):
                item = QListWidgetItem()
                item.setIcon(QIcon(":/dark/img/scss.png"))
                item.setText(file)
                self.listWidget.addItem(item)
        else:
            pass

    def undo(self):
        '''撤销'''
        pass
    
    def redo(self):
        '''重做'''
        pass
    
    def cut(self):
        '''剪切'''
        pass

    def copy(self):
        '''复制'''
        pass

    def paste(self):
        '''粘贴'''
        pass

    




    def getCurrentEditor(self):
        '''获取当前编辑器'''
        currentIndex = self.EditorTabWidget.currentIndex()
        if currentIndex != -1:
            return self.EditorTabWidget.widget(currentIndex)
        return None

    def selectFile(self, item):
        '''从项目列表选择文件'''
        self.stackedWidget.setCurrentIndex(1)
        if item.text() not in self.OPEN_FILE_LIST:
            if self.OPEN_FILE_NUM == 0:
                curCodeEditor = CodeEditor(filelist=self.OPEN_FILE_LIST)
                curCodeEditor.loadFile(self.projectFolder + '/' + item.text())
                self.EditorTabWidget.addTab(curCodeEditor, item.text())
                self.OPEN_FILE_LIST.append(item.text())
                self.CODE_EDITORS.append(self.CodeEditor)
                self.OPEN_FILE_NUM += 1
                curCodeEditor.textChanged.connect(self.updatePreview)
            else:
                self.OPEN_FILE_LIST.append(item.text())
                curCodeEditor = CodeEditor(filelist=self.OPEN_FILE_LIST)
                self.EditorTabWidget.addTab(curCodeEditor, item.text())
                curCodeEditor.loadFile(self.projectFolder + '/' + item.text())
                self.changeTabTitle(self.OPEN_FILE_NUM, item.text())
                self.EditorTabWidget.setCurrentIndex(self.OPEN_FILE_NUM)
                self.CODE_EDITORS.append(curCodeEditor)
                self.OPEN_FILE_NUM += 1
                curCodeEditor.highlighter = SassHighlighter(curCodeEditor.document())
                curCodeEditor.textChanged.connect(self.updatePreview)
        else:
            self.EditorTabWidget.setCurrentIndex(self.OPEN_FILE_LIST.index(item.text()))

    def changeTabTitle(self, idx, title):
        '''修改tab标题'''
        self.EditorTabWidget.setTabText(idx, title)

    def updatePreview(self):
        '''更新预览'''
        scss = ""
        for i in range(self.EditorTabWidget.count()):
            codeEditor = self.EditorTabWidget.widget(i)
            scss += codeEditor.toPlainText() + "\n"
        try:
            qss = sass.compile(string=scss)
            self.previewWidget.setStyleSheet(qss)
        except Exception as e:
            pass

    def newFile(self):
        pass
