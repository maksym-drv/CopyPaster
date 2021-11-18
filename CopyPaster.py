import pyautogui as pya
import pyperclip
import time
import json
import keyboard
import asyncio
from app import Application
from check import Check as check

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.2)
    return pyperclip.paste()

def cut_clipboard():
    pya.hotkey('ctrl', 'x')
    time.sleep(.2)
    return pyperclip.paste()

def click_copy():
    pya.position() # позиция курсора
    clipboard = pyperclip.paste()
    new_txt = copy_clipboard()
    if not clipboard == new_txt:
        clipboard_list = check.check_clipboard(clipboard)
        if check.check_new_text(clipboard_list, new_txt):
            clipboard_list.append(new_txt)
        pyperclip.copy(json.dumps(clipboard_list))

def click_cut():
    pya.position() # позиция курсора
    clipboard = pyperclip.paste()
    new_txt = cut_clipboard()
    if not clipboard == new_txt:
        clipboard_list = check.check_clipboard(clipboard)
        if check.check_new_text(clipboard_list, new_txt):
            clipboard_list.append(new_txt)
        pyperclip.copy(json.dumps(clipboard_list))

def click_paste():
    clipboard = pyperclip.paste()
    clipboard_list = check.check_clipboard(clipboard)
    Application(clipboard_list).make_app()
    if check.check_output(clipboard):
        pya.position() # позиция курсора
        pya.hotkey('ctrl', 'v')
    pyperclip.copy(json.dumps(clipboard_list))
    time.sleep(.3)
    
async def main():
    keyboard.add_hotkey('ctrl+f11', click_copy)
    keyboard.add_hotkey('ctrl+f12', click_paste)
    keyboard.add_hotkey('ctrl+f10', click_cut)
    keyboard.wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.run(main())
    loop.run_forever()
    loop.close()