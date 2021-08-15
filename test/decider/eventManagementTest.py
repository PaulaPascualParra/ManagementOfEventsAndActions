import os
import sys
import unittest

from src.decider import eventManagement


class EventManagementTest(unittest.TestCase):
    NO_EVENT = "NO_EVENT"
    EVENT = "NEW_FILE"
    FOLDER = os.path.join(os.path.dirname(sys.executable), "..", "..", "test", "files")
    NAME = "test_file_helper"
    TEXT = "just testing"

    def test_whenEventDoesntExist_raiseException(self):
        self.assertRaises(Exception, eventManagement.receive_event, self.NO_EVENT)

    def test_whenEventExists_callFunction(self):
        eventManagement.receive_event(self.EVENT, folder=self.FOLDER, name=self.NAME, text=self.TEXT)

if __name__ == '__main__':
    unittest.main()