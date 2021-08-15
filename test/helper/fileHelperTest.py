import os
import sys
import unittest
from src.helper import fileHelper


class FileHelperTest(unittest.TestCase):

    FOLDER = os.path.join(os.path.dirname(sys.executable), "..", "..", "test", "files")
    NAME = "test_file_helper"
    TEXT = "just testing"

    def test_whenHaveAValidInput_createFile(self):
        fileHelper.create_new_file(folder=self.FOLDER, name=self.NAME, text=self.TEXT)

    def test_whenHaveAnIValidInput_raiseException(self):
        self.assertRaises(Exception, fileHelper.create_new_file)


if __name__ == '__main__':
    unittest.main()
