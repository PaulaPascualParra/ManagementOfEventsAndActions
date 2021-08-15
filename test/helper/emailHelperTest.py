import unittest
from src.helper import emailHelper


class EmailHelperTest(unittest.TestCase):
    SENDER = "tests.python.name@gmail.com"
    TO = "tests.python.name@gmail.com"
    # todo: secure the password
    PASSWORD = "cK$!syGrGx$Z*zEaPZ40"
    SUBJECT = "test_mail_helper"
    TEXT = "just testing"

    def test_whenHaveAValidInput_raiseException(self):
        emailHelper.send_email(sender=self.SENDER, to=self.TO, password=self.PASSWORD, subject=self.SUBJECT,
                               message=self.TEXT)

    def test_whenHaveAnInvalidInput_sendEmail(self):
        self.assertRaises(Exception, emailHelper.send_email)


if __name__ == '__main__':
    unittest.main()
