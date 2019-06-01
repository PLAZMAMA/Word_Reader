from GUI import GUI
from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.geometry("925x510") #GUI start size
    my_gui = GUI(root)
    root.mainloop()