import pyautogui as pya
import pyperclip
import time
import json
import keyboard
import asyncio
from app import Application

pyperclip.copy(json.dumps([]))

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.3)
    return pyperclip.paste()

def cut_clipboard():
    pya.hotkey('ctrl', 'x')
    time.sleep(.3)
    return pyperclip.paste()

def click_copy():
    pya.position() # позиция курсора
    clipboard = json.loads(pyperclip.paste())
    new_txt = copy_clipboard()
    add = True
    for data in clipboard:
        if new_txt == data:
            add = False
            break
    if add:
        clipboard.append(new_txt)
    pyperclip.copy(json.dumps(clipboard))

def click_cut():
    pya.position() # позиция курсора
    clipboard = json.loads(pyperclip.paste())
    new_txt = cut_clipboard()
    add = True
    for data in clipboard:
        if new_txt == data:
            add = False
            break
    if add:
        clipboard.append(new_txt)
    pyperclip.copy(json.dumps(clipboard))

def click_paste():
    empty = False
    if pyperclip.paste() == '[]':
        empty = True
    clipboard = json.loads(pyperclip.paste())
    Application(clipboard).make_app()
    if not empty:
        pya.position() # позиция курсора
        pya.hotkey('ctrl', 'v')
    pyperclip.copy(json.dumps(clipboard))
    time.sleep(.3)
    
async def main():
    keyboard.add_hotkey('ctrl+f10', click_copy)
    keyboard.add_hotkey('ctrl+f11', click_paste)
    keyboard.add_hotkey('ctrl+f9', click_cut)
    keyboard.wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.run(main())
    loop.run_forever()
    loop.close()