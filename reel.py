from tkinter import Tk, Text
import tkinter as tk
from tkinter import ttk


#link textbox
root = Tk()
root.resizable(False, False)
root.title("reel link here")

text = Text(root, height=5)
text.pack()


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        # place button at (0,0)
        exitButton.place(x=0, y=0)

    def clickExitButton(self):
        exit()


root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()