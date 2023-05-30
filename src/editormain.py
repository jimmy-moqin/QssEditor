import sass
import tinycss
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QMenu, QPushButton, QSplitter, QWidget
from ui.ElemQssEditor import Ui_ElemQssEidtorMainWindow


class EditorMain(QMainWindow, Ui_ElemQssEidtorMainWindow):

    def __init__(self):
        super(EditorMain, self).__init__()
        self.setupUi(self)

        self.initUI()

    def initUI(self):

        self.fileMenu = QMenu(self)
        self.fileMenu.setObjectName("fileMenu")
        self.fileMenu.setAttribute(Qt.WA_TranslucentBackground)
        self.fileMenu.addAction("新建", self.newFile, QKeySequence.New)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("打开.sass文件", self.openFile, QKeySequence.Open)
        self.fileMenu.addAction("打开文件夹")
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("保存")
        self.fileMenu.addAction("另存为")
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("退出")
        self.fileBtn.setMenu(self.fileMenu)

        self.fileMenu.actions()[1].triggered.connect(self.openFile)

        self.editMenu = QMenu(self)
        self.editMenu.setObjectName("editMenu")
        self.editMenu.setAttribute(Qt.WA_TranslucentBackground)
        self.editMenu.addAction("撤销")
        self.editMenu.addAction("重做")
        self.editMenu.addSeparator()
        self.editMenu.addAction("剪切")
        self.editMenu.addAction("复制")
        self.editMenu.addAction("粘贴")
        self.editMenu.addSeparator()
        self.editMenu.addAction("查找")
        self.editMenu.addAction("替换")
        self.editBtn.setMenu(self.editMenu)

        self.reloadQss()
        self.reloadBtn.clicked.connect(self.reloadQss)

        self.CodeEditor.textChanged.connect(self.updatePreview)

        # 绑定窗口控制按钮
        # self.minBtn.clicked.connect(self.showMinimized)
        # self.closeBtn.clicked.connect(self.close)
        # self.maxBtn.clicked.connect(self.changeMax)

        # 初始化分裂窗口
        # self.SIZE = [320,1528]
        # self.splitter.setSizes(self.SIZE)
        # self.splitter.splitterMoved.connect(self.recordSizes)

        # 初始化左侧按钮
        self.processBtn.setCheckable(True)
        self.processBtn.setChecked(True)
        self.processBtn.clicked.connect(lambda: self.select(self.processBtn))
        self.documentBtn.clicked.connect(lambda: self.select(self.documentBtn))
        self.searchBtn.clicked.connect(lambda: self.select(self.searchBtn))
        self.settingBtn.clicked.connect(lambda: self.select(self.settingBtn))
        self.githubBtn.clicked.connect(lambda: self.select(self.githubBtn))

    '''Logic Func below'''

    def reloadQss(self):
        with open('.\\resource\\\qss\\MainWindow_DarkStyle.scss', 'r') as f:
            scss = f.read()

        qss = sass.compile(string=scss)
        self.setStyleSheet(qss)
        self.QSS = qss

    def select(self, btn):
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

    def openFile(self):
        from PyQt5.QtWidgets import QFileDialog
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        self.CodeEditor.loadFile(fileName)
        self.changeTabTitle(fileName.split('/')[-1])

    def changeTabTitle(self, title):
        self.EditorTabWidget.setTabText(0, title)

    def updatePreview(self):
        scss = self.CodeEditor.toPlainText()
        try:
            qss  = sass.compile(string=scss)
            self.previewWidget.setStyleSheet(qss)
        except Exception as e:
            print(e)
        
    def newFile(self):
        pass
    
