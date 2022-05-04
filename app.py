import sys
from PyQt5 import QtWidgets
from gui import GUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
