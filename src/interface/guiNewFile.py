from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from src.helper import guiHelper
from src.decider import eventManagement


class GUINewFile(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_name = 'newFile.ui'

        try:
            uic.loadUi(guiHelper.get_gui_path_helper(ui_name), self)
            self.start()
        except FileNotFoundError:
            print("Cant find the file :(")

    def start(self):
        self.bttn_browse.clicked.connect(self.browse)
        self.btn_ok.clicked.connect(self.save_file)

    def save_file(self):
        name = self.txt_input_name_file.toPlainText()
        folder = self.txt_input_folder.toPlainText()
        text = self.txt_input_text.toPlainText()
        eventManagement.receive_event("NEW_FILE", folder=folder, name=name, text=text)
        self.close()

    def browse(self):
        folder = QFileDialog.getExistingDirectory()
        self.txt_input_folder.setPlainText(folder)
