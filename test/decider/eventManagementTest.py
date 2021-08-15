import unittest
from unittest.mock import patch, MagicMock

from src.decider import eventManagement
from src.helper import fileHelper


class EventManagementTest(unittest.TestCase):
    NO_EVENT = "NO_EVENT"
    EVENT = "NEW_FILE"

    def test_whenEventDoesntExist_raiseException(self):
        self.assertRaises(Exception, eventManagement.receive_event, self.NO_EVENT)

    # todo: case everything works
    """
    @patch(fileHelper)
    def test_whenEventExists_callFunction(self, mock):
        mock.create_new_file() = MagicMock()
        eventManagement.receive_event(self.EVENT, folder="/Users/paulapascual/PycharmProjects/SkydanceManagement/test/decider", name="hi", message="")
"""
if __name__ == '__main__':
    unittest.main()