#Mahi and Hargun
from tkinter import * 


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Word Reader")

        self.image_view = Canvas(master, width=200, height=100)
        self.image_view.pack()
        self.image_view.create_rectangle(50, 25, 150, 75, fill="blue")

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = GUI(root)
root.mainloop()