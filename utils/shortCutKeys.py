import json

from PyQt5.QtGui import QKeySequence


class ShortCutKeys(object):
    def __init__(self):
        with open("utils\shortCutKeys.json", "r") as f:
            self.shortCutKeysDict = json.load(f)
        
        self.key_dict = {}
        for key in self.shortCutKeysDict:
            self.key_dict[key] = QKeySequence(self.shortCutKeysDict[key])
    
        