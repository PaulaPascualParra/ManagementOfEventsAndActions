from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from src.helper import guiHelper
from src.decider import eventManagement


class GUISendMail(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_name = 'sendEmail.ui'

        try:
            uic.loadUi(guiHelper.get_gui_path_helper(ui_name), self)
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
        if not self.check_empty_fields(sender=sender, password=password, to=to, subject=subject, message=message):
            eventManagement.receive_event("SEND_MAIL", sender=sender, password=password, to=to, subject=subject, message=message)
            self.close()
        else:
            self.start()

    def check_empty_fields(self, sender, password, to, subject, message):
        fields_empty = False
        if sender == "":
            self.lbl_from.setStyleSheet('color: red')
            fields_empty = True
        else:
            self.lbl_from.setStyleSheet('color: black')

        if password == "":
            self.lbl_password.setStyleSheet('color: red')
            fields_empty = True
        else:
            self.lbl_password.setStyleSheet('color: black')

        if to == "":
            self.lbl_to.setStyleSheet('color: red')
            fields_empty = True
        else:
            self.lbl_to.setStyleSheet('color: black')

        if subject == "":
            self.lbl_subject.setStyleSheet('color: red')
            fields_empty = True
        else:
            self.lbl_subject.setStyleSheet('color: black')

        if message == "":
            self.lbl_message.setStyleSheet('color: red')
            fields_empty = True
        else:
            self.lbl_message.setStyleSheet('color: black')

        return fields_empty
