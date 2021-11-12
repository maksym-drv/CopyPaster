from tkinter import Tk, Listbox, \
    EXTENDED, Button, END
import pyperclip

class Application:
    def __init__(self, clipboard):
        self.clipboard = clipboard
    
    def make_app(self):

        def get_list():
            sel = listbox.curselection()
            seltext = '\n'.join([listbox.get(x) for x in sel])
            pyperclip.copy(seltext)
            app.destroy()

        def on_closing():
            pyperclip.copy("")
            app.destroy()

        app = Tk()

        app.title("Буфер обмена")

        width  = app.winfo_screenwidth()
        height = app.winfo_screenheight()
        app.geometry(f'{int(width/2)}x{int(height/3.5)}')

        listbox = Listbox(app, selectmode = EXTENDED)
        listbox.grid(row=1, column=0, sticky="nsew")

        button = Button(app, text = "Вставить", command = get_list, height=2)
        button.grid(row=2, column=0, sticky="nsew")

        for text in self.clipboard:
            listbox.insert(END, text)

        listbox.selection_set(3)

        app.attributes('-topmost', True)
        app.update()
        app.attributes('-topmost', False)

        app.protocol("WM_DELETE_WINDOW", on_closing)

        app.columnconfigure(0, weight=1)
        app.rowconfigure(1, weight=1)

        listbox.configure(background="#242424", fg="white")
        button.configure(background="#434343", fg="white")

        app.mainloop()