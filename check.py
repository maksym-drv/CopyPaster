import pyperclip
import json

class Check:
    def check_empty(self):
        if pyperclip.paste() == '[]':
            return True
        else:
            return False

    def check_clipboard(self, clipboard):
        try:
            lst = json.loads(clipboard)
            return lst
        except:
            lst = []
            return lst