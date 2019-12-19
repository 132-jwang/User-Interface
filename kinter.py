from tkinter import *



class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   
                 
        self.master = master

        self.init_window()

    def init_window(self):
     
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)


        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)

        edit.add_command(label="Undo")

        menu.add_cascade(label="Edit", menu=edit)
        
        help = Menu(menu)

        help.add_command(label="Online help")

        menu.add_cascade(label="Help", menu=help)
        
        layout = Menu(menu)

        layout.add_command(label="change font")

        menu.add_cascade(label="layout", menu=layout)

        view = Menu(menu)

        view.add_command(label="Zoom in")

        menu.add_cascade(label="view", menu=view)

    
    def client_exit(self):
        exit()

        
root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop() 
