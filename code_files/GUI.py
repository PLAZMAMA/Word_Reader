#Mahi and Hargun
from tkinter import * 
from tkinter import scrolledtext
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import ImageGrab
import os
from Model import Model

class GUI:
    def __init__(self, master, size = "925x510"):
        self.master = master
        self.master.title("Word Reader")
        self.master.geometry(size) #GUI start size

        #Left frame, contains canvas
        self.left_side = Frame(self.master)
        self.left_side.pack(fill='both', expand='yes')
        self.left_side.place(x=0,y=0)

        #Right frame, contains everything else
        self.right_side = Frame(self.master)
        self.right_side.pack(fill='both',expand='yes')
        self.right_side.place(x=500,y=0)

        #Canvas click event(gets file opener)
        def click(event):
            file_path = filedialog.askopenfilename()
            im = Image.open(file_path)
            im.save("input.png","PNG")
            self.resize_img()
            self.input_image = ImageTk.PhotoImage(Image.open("input.png"))
            self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)

        #Canvas
        self.input_image = ImageTk.PhotoImage(Image.open("input.png")) #Image input file
        self.image_view = Canvas(self.left_side, width=500, height=500)
        self.image_view.bind('<Button-1>', click) #Bind click function to canvas
        self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)
        self.image_view.bind('<Control-v>', self.paste)
        self.image_view.pack()

        #output box
        self.textbox = scrolledtext.ScrolledText(self.right_side,width=50,height=25)
        self.textbox.bind('<Control-c>', self.copy)
        self.textbox.pack()
        
        #convert button
        self.convert_button = Button(self.right_side, text="Convert", command=self.convert)
        self.convert_button.pack()

        #copy button
        self.copy_button = Button(self.right_side, text="Copy", command=self.copy)
        self.copy_button.pack()
    
    def resize_img(self):
        """updates the input to the right size"""
        size = 500, 500 #Thumbnail size
        im = Image.open("input.png")
        im.thumbnail(size)
        im.save("input.png")

    def convert(self):
        """converts input.png into a string of a word"""
        model = Model()
        word = model.predict("input.png")
        self.textbox.insert(END, word)

    
    def copy(self):
        """function for copy button"""
        copy_text = self.textbox.get("1.0",END)
        self.master.clipboard_clear()
        self.master.clipboard_append(copy_text)
    
    def paste(self):
        """paste function"""
        im = ImageGrab.grabclipboard()
        im.save('input.png','PNG')
        self.resize_img()
        self.input_image=ImageTk.PhotoImage(Image.open("input.png"))
        self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)
