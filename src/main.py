import sys
from PyQt5.QtWidgets import QApplication
from interface import gui


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui.GUI()
    GUI.show()
    sys.exit(app.exec_())
