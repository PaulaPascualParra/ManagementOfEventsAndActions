import unittest
import os
import sys
from src.helper import emailHelper


class EmailHelperTest(unittest.TestCase):
    SENDER = "tests.python.name@gmail.com"
    TO = "tests.python.name@gmail.com"
    SUBJECT = "test_mail_helper"
    TEXT = "just testing"

    # todo: secure the password
    application_path = os.path.join(os.path.dirname(sys.executable), "..", "..", "test", "files", "password.txt")
    print(application_path)
    with open(application_path) as f:
        lines = f.readlines()
    f.close()
    PASSWORD = lines[0]

    def test_whenHaveAValidInput_raiseException(self):
        emailHelper.send_email(sender=self.SENDER, to=self.TO, password=self.PASSWORD, subject=self.SUBJECT,
                               message=self.TEXT)

    def test_whenHaveAnInvalidInput_sendEmail(self):
        self.assertRaises(Exception, emailHelper.send_email)


if __name__ == '__main__':
    unittest.main()
