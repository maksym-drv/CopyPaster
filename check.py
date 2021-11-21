from tkinter.constants import FALSE
import pyperclip
import json

class Check:
    def check_output(clipboard):
        if pyperclip.paste() == clipboard:
            return False
        else:
            return True

    def check_clipboard(clipboard):
        try:
            lst = json.loads(clipboard)
            return lst
        except:
            lst = []
            return lst
    
    def check_new_text(clipboard, new_txt):
        num = 0
        for data in clipboard:
            if new_txt == data:
                clipboard.pop(num)
                return
            num += 1
