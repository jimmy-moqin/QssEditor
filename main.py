import os

uipath = os.path.dirname(os.path.abspath(__file__)) + '/ui/'
os.system("pyuic5 \"" + uipath + "ElemQssEditor.ui\" --import-from=resource.qrc -o \""+ uipath +"ElemQssEditor.py\"")
os.system("pyuic5 \"" + uipath + "homepage.ui\" --import-from=resource.qrc -o \""+ uipath +"homepage.py\"")
resousepath = os.path.dirname(os.path.abspath(__file__)) + '/resource/qrc/'
os.system("pyrcc5 \"" + resousepath + "mainQrc.qrc\" -o \""+ resousepath +"mainQrc_rc.py\"")

from PyQt5.QtWidgets import QApplication

from src.editormain import EditorMain

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Ui_MainWindow = EditorMain()
    Ui_MainWindow.show()
    sys.exit(app.exec_())
