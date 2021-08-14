import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class GUI(QMainWindow):
    # todo: handle they remove the ui
    def __init__(self):
        super().__init__()
        ui_name = 'managementSystemInterface.ui'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
            application_path = os.path.join(application_path, "interface")

        ui_name = os.path.join(application_path, ui_name)

        uic.loadUi(ui_name, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = GUI()
    GUI.show()
    sys.exit(app.exec_())
