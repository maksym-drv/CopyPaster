import pyperclip
import json

class Check:
    def check_empty(self):
        if pyperclip.paste() == '[]':
            return True
        else:
            return False

    def check_clipboard(self):
        try:
            clipboard = json.loads(pyperclip.paste())
            return clipboard
        except:
            lst = []
            return lst