from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from src.helper import guiHelper
from src.interface import guiNewFile, guiSendMail


class GUI(QMainWindow):
    # todo: handle they remove the ui
    def __init__(self):
        super().__init__()
        self.action = ""
        ui_name = 'managementSystemInterface.ui'

        uic.loadUi(guiHelper.open_gui_helper(ui_name), self)
        self.start()

    def start(self):
        self.bttn_create_file.clicked.connect(self.open_new_file_window)
        self.bttn_send_mail.clicked.connect(self.open_send_mail_window)

    def open_new_file_window(self):
        self.window = guiNewFile.GUINewFile()
        self.window.show()

    def open_send_mail_window(self):
        self.window = guiSendMail.GUISendMail()
        self.window.show()
