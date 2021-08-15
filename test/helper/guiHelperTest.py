import unittest
from src.helper import guiHelper
from unittest.mock import patch


class GuiHelperTest(unittest.TestCase):
    NAME = "newFile.ui"
    DIR = "/Users/paulapascual/PycharmProjects/SkydanceManagement/src/helper"
    PATH = "/Users/paulapascual/PycharmProjects/SkydanceManagement/src/helper/../interface/UI/newFile.ui"


    @patch('os.path.dirname')
    def test_whenHaveAnInvalidInput_returnGuiPath(self, mock_dir):
        mock_dir.return_value = self.DIR
        self.assertEqual(self.PATH, guiHelper.get_gui_path_helper(self.NAME))


    # todo: case everything works
    @patch('os.path.dirname')
    def test_whenHaveAValidInput_raiseException(self, mock_dir):
        mock_dir.return_value = Exception
        self.assertRaises(Exception, guiHelper.get_gui_path_helper, self.NAME)


if __name__ == '__main__':
    unittest.main()