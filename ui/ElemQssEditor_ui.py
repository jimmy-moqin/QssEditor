# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ElemQssEditor.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)
import mainQrc_rc

class Ui_ElemQssEidtorMainWindow(object):
    def setupUi(self, ElemQssEidtorMainWindow):
        if not ElemQssEidtorMainWindow.objectName():
            ElemQssEidtorMainWindow.setObjectName(u"ElemQssEidtorMainWindow")
        ElemQssEidtorMainWindow.resize(1453, 828)
        self.centralwidget = QWidget(ElemQssEidtorMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = QWidget(self.centralwidget)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy)
        self.titleWidget.setMinimumSize(QSize(0, 40))
        self.titleWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_8 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.titleWidget)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(40, 40))
        self.logo.setPixmap(QPixmap(u":/dark/img/qe.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.logo)

        self.fileBtn = QPushButton(self.titleWidget)
        self.fileBtn.setObjectName(u"fileBtn")
        self.fileBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.fileBtn)

        self.editBtn = QPushButton(self.titleWidget)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy1)
        self.editBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.editBtn)

        self.viewBtn = QPushButton(self.titleWidget)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.viewBtn)

        self.helpBtn = QPushButton(self.titleWidget)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.helpBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.projectTitleLabel = QLabel(self.titleWidget)
        self.projectTitleLabel.setObjectName(u"projectTitleLabel")

        self.horizontalLayout_8.addWidget(self.projectTitleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.minBtn = QPushButton(self.titleWidget)
        self.minBtn.setObjectName(u"minBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy2)
        self.minBtn.setMinimumSize(QSize(18, 18))
        self.minBtn.setMaximumSize(QSize(18, 18))
        icon = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../pvcs/ui", QSize(), QIcon.Normal, QIcon.Off)

        self.minBtn.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.minBtn)

        self.maxBtn = QPushButton(self.titleWidget)
        self.maxBtn.setObjectName(u"maxBtn")
        self.maxBtn.setMinimumSize(QSize(18, 18))
        self.maxBtn.setMaximumSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.maxBtn)

        self.closeBtn = QPushButton(self.titleWidget)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(18, 18))
        self.closeBtn.setMaximumSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.verticalLayout_4.addWidget(self.titleWidget)

        self.mainWidget = QWidget(self.centralwidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.horizontalLayout = QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftWidget = QWidget(self.mainWidget)
        self.leftWidget.setObjectName(u"leftWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy3)
        self.leftWidget.setMinimumSize(QSize(72, 0))
        self.leftWidget.setMaximumSize(QSize(72, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.processBtn = QPushButton(self.leftWidget)
        self.processBtn.setObjectName(u"processBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(72)
        sizePolicy4.setVerticalStretch(72)
        sizePolicy4.setHeightForWidth(self.processBtn.sizePolicy().hasHeightForWidth())
        self.processBtn.setSizePolicy(sizePolicy4)
        self.processBtn.setMinimumSize(QSize(72, 72))
        self.processBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/dark/img/process.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/dark/img/process_blue.png", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u":/dark/img/process_blue.png", QSize(), QIcon.Active, QIcon.On)
        icon1.addFile(u":/dark/img/process_blue.png", QSize(), QIcon.Selected, QIcon.On)
        self.processBtn.setIcon(icon1)
        self.processBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.processBtn)

        self.documentBtn = QPushButton(self.leftWidget)
        self.documentBtn.setObjectName(u"documentBtn")
        self.documentBtn.setMinimumSize(QSize(72, 72))
        self.documentBtn.setMaximumSize(QSize(72, 72))
        icon2 = QIcon()
        icon2.addFile(u":/dark/img/document.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/dark/img/document_blue.png", QSize(), QIcon.Active, QIcon.On)
        icon2.addFile(u":/dark/img/document_blue.png", QSize(), QIcon.Selected, QIcon.On)
        self.documentBtn.setIcon(icon2)
        self.documentBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.documentBtn)

        self.searchBtn = QPushButton(self.leftWidget)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(72, 72))
        self.searchBtn.setMaximumSize(QSize(72, 72))
        icon3 = QIcon()
        icon3.addFile(u":/dark/img/search.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/dark/img/search_blue.png", QSize(), QIcon.Active, QIcon.On)
        icon3.addFile(u":/dark/img/search_blue.png", QSize(), QIcon.Selected, QIcon.On)
        self.searchBtn.setIcon(icon3)
        self.searchBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.searchBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settingBtn = QPushButton(self.leftWidget)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setMinimumSize(QSize(72, 72))
        self.settingBtn.setMaximumSize(QSize(72, 72))
        icon4 = QIcon()
        icon4.addFile(u":/dark/img/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/dark/img/setting_blue.png", QSize(), QIcon.Active, QIcon.On)
        icon4.addFile(u":/dark/img/setting_blue.png", QSize(), QIcon.Selected, QIcon.On)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.settingBtn)

        self.githubBtn = QPushButton(self.leftWidget)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setMinimumSize(QSize(72, 72))
        self.githubBtn.setMaximumSize(QSize(72, 72))
        icon5 = QIcon()
        icon5.addFile(u":/dark/img/github.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/dark/img/github_blue.png", QSize(), QIcon.Active, QIcon.On)
        icon5.addFile(u":/dark/img/github_blue.png", QSize(), QIcon.Selected, QIcon.On)
        self.githubBtn.setIcon(icon5)
        self.githubBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.githubBtn)


        self.horizontalLayout.addWidget(self.leftWidget)

        self.splitter = QSplitter(self.mainWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.ListWidget = QWidget(self.splitter)
        self.ListWidget.setObjectName(u"ListWidget")
        self.verticalLayout_6 = QVBoxLayout(self.ListWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.functionLabel = QLabel(self.ListWidget)
        self.functionLabel.setObjectName(u"functionLabel")
        self.functionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.functionLabel)

        self.listWidget = QListWidget(self.ListWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_6.addWidget(self.listWidget)

        self.splitter.addWidget(self.ListWidget)
        self.EditorWidget = QWidget(self.splitter)
        self.EditorWidget.setObjectName(u"EditorWidget")
        self.verticalLayout = QVBoxLayout(self.EditorWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.EditorWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.verticalLayout_8 = QVBoxLayout(self.homepage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 142, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.homepageLogo = QLabel(self.homepage)
        self.homepageLogo.setObjectName(u"homepageLogo")
        self.homepageLogo.setPixmap(QPixmap(u":/dark/img/qe.png"))
        self.homepageLogo.setScaledContents(False)
        self.homepageLogo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.homepageLogo)

        self.verticalSpacer_4 = QSpacerItem(20, 143, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.widget_5 = QWidget(self.homepage)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(136, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.hpTipsWidget = QWidget(self.widget_5)
        self.hpTipsWidget.setObjectName(u"hpTipsWidget")
        self.formLayout = QFormLayout(self.hpTipsWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.hpTipsWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.hpTipsWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.label_4 = QLabel(self.hpTipsWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.hpTipsWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_5)

        self.label_6 = QLabel(self.hpTipsWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.hpTipsWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_7)


        self.horizontalLayout_6.addWidget(self.hpTipsWidget)

        self.horizontalSpacer_4 = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addWidget(self.widget_5)

        self.verticalSpacer_5 = QSpacerItem(20, 142, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.homepage)
        self.editorPage = QWidget()
        self.editorPage.setObjectName(u"editorPage")
        self.verticalLayout_5 = QVBoxLayout(self.editorPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.EditorTabWidget = QTabWidget(self.editorPage)
        self.EditorTabWidget.setObjectName(u"EditorTabWidget")
        self.CodeEditor = QWidget()
        self.CodeEditor.setObjectName(u"CodeEditor")
        self.EditorTabWidget.addTab(self.CodeEditor, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.EditorTabWidget.addTab(self.tab_4, "")

        self.verticalLayout_5.addWidget(self.EditorTabWidget)

        self.stackedWidget.addWidget(self.editorPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.splitter.addWidget(self.EditorWidget)
        self.previewWidget = QWidget(self.splitter)
        self.previewWidget.setObjectName(u"previewWidget")
        self.verticalLayout_3 = QVBoxLayout(self.previewWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.previewTabWidget = QTabWidget(self.previewWidget)
        self.previewTabWidget.setObjectName(u"previewTabWidget")
        self.ButtonTab = QWidget()
        self.ButtonTab.setObjectName(u"ButtonTab")
        self.verticalLayout_7 = QVBoxLayout(self.ButtonTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.ButtonTab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DefaultBtn = QPushButton(self.widget_2)
        self.DefaultBtn.setObjectName(u"DefaultBtn")

        self.horizontalLayout_3.addWidget(self.DefaultBtn)

        self.PrimaryBtn = QPushButton(self.widget_2)
        self.PrimaryBtn.setObjectName(u"PrimaryBtn")

        self.horizontalLayout_3.addWidget(self.PrimaryBtn)

        self.SuccessBtn = QPushButton(self.widget_2)
        self.SuccessBtn.setObjectName(u"SuccessBtn")

        self.horizontalLayout_3.addWidget(self.SuccessBtn)

        self.InfoBtn = QPushButton(self.widget_2)
        self.InfoBtn.setObjectName(u"InfoBtn")

        self.horizontalLayout_3.addWidget(self.InfoBtn)

        self.WarningBtn = QPushButton(self.widget_2)
        self.WarningBtn.setObjectName(u"WarningBtn")

        self.horizontalLayout_3.addWidget(self.WarningBtn)

        self.DangerBtn = QPushButton(self.widget_2)
        self.DangerBtn.setObjectName(u"DangerBtn")

        self.horizontalLayout_3.addWidget(self.DangerBtn)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.ButtonTab)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.PlainBtn = QPushButton(self.widget_3)
        self.PlainBtn.setObjectName(u"PlainBtn")

        self.horizontalLayout_5.addWidget(self.PlainBtn)

        self.PlainPrimaryBtn = QPushButton(self.widget_3)
        self.PlainPrimaryBtn.setObjectName(u"PlainPrimaryBtn")

        self.horizontalLayout_5.addWidget(self.PlainPrimaryBtn)

        self.PlainSuccessBtn = QPushButton(self.widget_3)
        self.PlainSuccessBtn.setObjectName(u"PlainSuccessBtn")

        self.horizontalLayout_5.addWidget(self.PlainSuccessBtn)

        self.PlainInfoBtn = QPushButton(self.widget_3)
        self.PlainInfoBtn.setObjectName(u"PlainInfoBtn")

        self.horizontalLayout_5.addWidget(self.PlainInfoBtn)

        self.PlainWarningBtn = QPushButton(self.widget_3)
        self.PlainWarningBtn.setObjectName(u"PlainWarningBtn")

        self.horizontalLayout_5.addWidget(self.PlainWarningBtn)

        self.PlainDangerBtn = QPushButton(self.widget_3)
        self.PlainDangerBtn.setObjectName(u"PlainDangerBtn")

        self.horizontalLayout_5.addWidget(self.PlainDangerBtn)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.widget = QWidget(self.ButtonTab)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_2.addWidget(self.pushButton_6)


        self.verticalLayout_7.addWidget(self.widget)

        self.widget_4 = QWidget(self.ButtonTab)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_20 = QPushButton(self.widget_4)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_4.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.widget_4)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_4.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.widget_4)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_4.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.widget_4)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_4.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.widget_4)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_4.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.widget_4)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_4.addWidget(self.pushButton_25)


        self.verticalLayout_7.addWidget(self.widget_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.previewTabWidget.addTab(self.ButtonTab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.previewTabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.previewTabWidget)

        self.splitter.addWidget(self.previewWidget)

        self.horizontalLayout.addWidget(self.splitter)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_4.addWidget(self.mainWidget)

        ElemQssEidtorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ElemQssEidtorMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1453, 26))
        ElemQssEidtorMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ElemQssEidtorMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        ElemQssEidtorMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ElemQssEidtorMainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.EditorTabWidget.setCurrentIndex(0)
        self.previewTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ElemQssEidtorMainWindow)
    # setupUi

    def retranslateUi(self, ElemQssEidtorMainWindow):
        ElemQssEidtorMainWindow.setWindowTitle(QCoreApplication.translate("ElemQssEidtorMainWindow", u"ElementUI Qss Editor", None))
        self.logo.setText("")
        self.fileBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u6587\u4ef6(F)", None))
#if QT_CONFIG(shortcut)
        self.fileBtn.setShortcut(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Alt+F", None))
#endif // QT_CONFIG(shortcut)
        self.editBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u7f16\u8f91(E)", None))
#if QT_CONFIG(shortcut)
        self.editBtn.setShortcut(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.viewBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u67e5\u770b(V)", None))
#if QT_CONFIG(shortcut)
        self.viewBtn.setShortcut(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Alt+V", None))
#endif // QT_CONFIG(shortcut)
        self.helpBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u5e2e\u52a9(H)", None))
#if QT_CONFIG(shortcut)
        self.helpBtn.setShortcut(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Alt+H", None))
#endif // QT_CONFIG(shortcut)
        self.projectTitleLabel.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"test Project", None))
        self.minBtn.setText("")
        self.maxBtn.setText("")
        self.closeBtn.setText("")
        self.processBtn.setText("")
        self.documentBtn.setText("")
        self.searchBtn.setText("")
        self.settingBtn.setText("")
        self.githubBtn.setText("")
        self.functionLabel.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u9879\u76ee\u6587\u4ef6\u5939", None))
        self.homepageLogo.setText("")
        self.label_2.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u6253\u5f00 scss \u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Ctrl + O", None))
        self.label_4.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u65b0\u5efa scss \u6587\u4ef6", None))
        self.label_5.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Ctrl + N", None))
        self.label_6.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.label_7.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Ctrl + K", None))
        self.EditorTabWidget.setTabText(self.EditorTabWidget.indexOf(self.CodeEditor), QCoreApplication.translate("ElemQssEidtorMainWindow", u"Tab 1", None))
        self.EditorTabWidget.setTabText(self.EditorTabWidget.indexOf(self.tab_4), QCoreApplication.translate("ElemQssEidtorMainWindow", u"Tab 2", None))
        self.DefaultBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Default", None))
        self.PrimaryBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Primary", None))
        self.SuccessBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Success", None))
        self.InfoBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Info", None))
        self.WarningBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Warning", None))
        self.DangerBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Danger", None))
        self.PlainBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Plain", None))
        self.PlainPrimaryBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Primary", None))
        self.PlainSuccessBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Success", None))
        self.PlainInfoBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Info", None))
        self.PlainWarningBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Warning", None))
        self.PlainDangerBtn.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Danger", None))
        self.pushButton.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Round", None))
        self.pushButton_2.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Primary", None))
        self.pushButton_3.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Success", None))
        self.pushButton_4.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Info", None))
        self.pushButton_5.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Warning", None))
        self.pushButton_6.setText(QCoreApplication.translate("ElemQssEidtorMainWindow", u"Danger", None))
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.pushButton_22.setText("")
        self.pushButton_23.setText("")
        self.pushButton_24.setText("")
        self.pushButton_25.setText("")
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.ButtonTab), QCoreApplication.translate("ElemQssEidtorMainWindow", u"Buttons", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.tab_2), QCoreApplication.translate("ElemQssEidtorMainWindow", u"Tab 2", None))
    # retranslateUi

