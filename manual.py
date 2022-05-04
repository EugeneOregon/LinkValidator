import os
from PyQt5 import QtCore

from faq_manual import user_manual


class Manual(QtCore.QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.manual = None

    def run(self):
        self.manual = 'manual.txt'
        with open(self.manual, 'w') as file:
            file.write(user_manual)
        os.startfile(self.manual)
