import sys
import os


def get_gui_path_helper(name):
    try:
        ui_name = name
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.join(os.path.dirname(sys.executable), "..", "interface")
        elif __file__:
            application_path = os.path.join(os.path.dirname(__file__), "..", "interface", "UI")

        return os.path.join(application_path, ui_name)
    except Exception as e:
        print("Something went wrong" + str(e))
        raise