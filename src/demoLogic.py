import sass
import tinycss
from PyQt5.QtWidgets import QMainWindow, QWidget
from ui.demoUI import Ui_demoWidget
from ui.homepage import Ui_HomePage

class DemoLogic(QWidget, Ui_demoWidget):

    def __init__(self):
        super(DemoLogic, self).__init__()
        self.setupUi(self)
        
        
        self.initUI()
    
    def initUI(self):
        self.reloadQss()
        self.reloadBtn.clicked.connect(self.reloadQss)
        self.DefaultBtn.clicked.connect(self.parseQss)

    '''Logic Func below'''
    
    def reloadQss(self):
        with open('.\\resource\\qss\\buttons.scss', 'r') as f:
            scss = f.read()

        qss = sass.compile(string=scss)
        self.setStyleSheet(qss)
        self.QSS = qss

    def parseQss(self):
        qssDict = {}
        cssParser = tinycss.make_parser('page3')
        stylesheet = cssParser.parse_stylesheet(self.QSS)
        for rule in stylesheet.rules:
            selector = rule.selector.as_css()
            print(selector)
        

