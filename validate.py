from tkinter import messagebox
def validate_number(action, index, vlaue_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if vlaue_if_allowed == "":
        return True
    try:
        int(vlaue_if_allowed)
        return True
    except ValueError:
        messagebox.showerror("Invalid Input", "please enter a number")