import difflib
import json
import re

from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QListWidget, QWidget


class CodePrompt(QWidget):

    def __init__(self,fileList=None, parent=None):
        super().__init__(parent)
        self.projectFileList = fileList
        # 创建一个ComboBox
        self.listWidget = QListWidget(self)
        self.listWidget.setObjectName("codeListWidget")
        with open("utils\sassHighLight.json", "r") as f:
            data = json.load(f)
            keywords = data["keywords"]
            units = data["units"]
            attributes = data["attributes"]
            pseudostates = data["pseudostates"]
            subcontrols = data["subcontrols"]

        self.items = keywords + units + attributes + pseudostates + subcontrols


    def loadProjectVars(self):
        # 读取项目变量
        cpl = re.compile(r"\$[a-zA-Z0-9-_]+")
        if self.projectFileList is None:
            return
        else:
            for f in self.projectFileList:
                with open(f, "r") as f:
                    data = f.read()
                    self.items += cpl.findall(data)
                

    def updateItems(self, keyword):
        matches = []
        for item in self.items:
            similarity = difflib.SequenceMatcher(None, keyword, item).ratio()
            if similarity > 0.25:
                matches.append((item, similarity))

        matches.sort(key=lambda x: x[1], reverse=True)

        if len(matches) > 0:
            self.clearItems()
            for item, _ in matches:
                self.listWidget.addItem(item)
            return 1
        else:
            return 0

    def clearItems(self):
        self.listWidget.clear()

    def moveWithCursor(self, position, offset=QPoint(0, 30)):
        # 根据光标的位置移动Widget  # 设置Widget相对于光标的偏移量
        self.move(position + offset)
