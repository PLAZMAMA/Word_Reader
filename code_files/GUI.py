#Mahi and Hargun
from tkinter import * 
from tkinter import scrolledtext
#test
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Word Reader")

        self.image_view = Canvas(master, width=200, height=100)
        self.image_view.pack()
        self.image_view.create_rectangle(50, 25, 150, 75, fill="blue")

        self.convert_button = Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.copy_button = Button(master, text="Copy", command=self.copy)
        self.copy_button.pack()

        self.textbox = scrolledtext.ScrolledText(self.master,width=40,height=10)
        self.textbox.pack()


    #fuction for convert button
    def convert(self):
        print("convert")
    #function for copy button
    def copy(self):
        print("copy")

        
root = Tk()
my_gui = GUI(root)
root.mainloop()