#Mahi and Hargun

from tkinter import * #the "*" means imoprt everythin
#below just initializes everything
class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Word Reader")
        self.pack(fill=BOTH, expand=1)
        convertButton=Button(self, text="convert")
        convertButton.place(x=0,y=0)


root = Tk()

app = Window(root)

root.mainloop()








        #super().__init__(master)
        #self.master = master #main window 

    #def set_win(self):


        
       

#if __name__ == "__main__":
    #root = Tk() #root of the window
    #app = Window(root)
    #app.set_win()
    #root.mainloop() #generates the window