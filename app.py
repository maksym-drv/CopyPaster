from tkinter import Tk, StringVar, Listbox, \
    EXTENDED, Button, Label, END
import pyperclip

class Application:
    def __init__(self, clipboard):
        self.clipboard = clipboard
    
    def make_app(self):

        def get_list():
            sel = listbox1.curselection()
            seltext = '\n'.join([listbox1.get(x) for x in sel])
            pyperclip.copy(seltext)
            app.destroy()

        app = Tk()
        choices = StringVar(app)

        app.title("Буфер обмена")

        width  = app.winfo_screenwidth()
        height = app.winfo_screenheight()
        app.geometry(f'{int(width/2)}x{int(height/3.5)}')

        listbox1 = Listbox(app, width=90,selectmode = EXTENDED)
        listbox1.pack()

        button1 = Button(app, text = "Вставить", command = get_list)
        button1.pack()

        label1 = Label(app, textvariable = choices)
        label1.pack()

        for text in self.clipboard:
            listbox1.insert(END, text)

        listbox1.selection_set(3)

        app.attributes('-topmost', True)
        app.update()
        app.attributes('-topmost', False)

        app.mainloop()