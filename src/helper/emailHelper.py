import os
import smtplib
import keyring

# todo: make the send email secure

def send_email(*args, **kwargs):
    sender = kwargs['sender']
    to = kwargs['to']
    subject = kwargs['subject']
    message = kwargs['message']
    password = kwargs['password']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    message = 'Subject: {}\n\n{}'.format(subject, message)
    server.sendmail(sender, to, message)
