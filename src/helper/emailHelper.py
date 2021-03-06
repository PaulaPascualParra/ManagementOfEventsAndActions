import smtplib

# todo: make the send email secure
# todo: check that the fields are valid


def send_email(*args, **kwargs):
    try:
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
    except Exception as e:
        print("Something went wrong" + str(e))
        raise
