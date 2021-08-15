from src.helper import fileHelper,emailHelper

switcher = {
        "NEW_FILE": fileHelper.create_new_file,
        "SEND_MAIL": emailHelper.send_email,
    }


def receive_event(event_type, *args, **kwargs):
    func = switcher.get(event_type, lambda: "Invalid action")
    func(*args, **kwargs)

