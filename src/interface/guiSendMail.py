from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from src.helper import guiHelper
from src.decider import eventManagement


class GUISendMail(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_name = 'sendEmail.ui'

        try:
            uic.loadUi(guiHelper.open_gui_helper(ui_name), self)
            self.start()
        except FileNotFoundError:
            print("Cant find the file :(")

    def start(self):
        self.bttn_send.clicked.connect(self.send_mail)

    def send_mail(self):
        sender = self.txt_from.toPlainText()
        password = self.txt_password.toPlainText()
        to = self.txt_to.toPlainText()
        subject = self.txt_subject.toPlainText()
        message = self.txt_message.toPlainText()
        eventManagement.receive_event("SEND_MAIL", sender=sender, password=password, to=to, subject=subject, message=message)
        self.close()