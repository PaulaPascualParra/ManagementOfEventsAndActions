from src.helper import fileHelper,emailHelper

switcher = {
        "NEW_FILE": fileHelper.create_new_file,
        "SEND_MAIL": emailHelper.send_email,
    }


def receive_event(event_type, *args, **kwargs):
    try:
        func = switcher[event_type]
        func(*args, **kwargs)

    except Exception as e:
        print("The event is not save" + str(e))
        raise

