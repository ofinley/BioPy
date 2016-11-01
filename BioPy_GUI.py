#
# github.com/ofinley
# BioPy GUI
# Python v2.7.12
#
#

from Tkinter import *

#top =  Tkinter.Tk()
# Code to add widgets goes here

class Application(Frame):
    def createWidgets(self):
        m1 = PanedWindow()
        m1.pack(fill=BOTH, expand=1)

        #Goes to left side of window
        left = Label(m1, text="File tree over here")
        m1.add(left)

        #Goes to the top of window
        m2 = PanedWindow(m1, orient=VERTICAL)
        m1.add(m2)

        top = Label(m2, text="View contents of selected files here")
        m2.add(top)
        
        #Goes to bottom of window
        bottom = Label(m2, text="Buttons go here?")
        m2.add(bottom)

                
        


    def __init__(self, master=None):
        Frame.__init__(self,master)
        #self.pack()
        self.createWidgets()

        
#top.mainloop()
root = Tk()
app = Application(master=root)
app.master.title("BioPy v.1.0")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")

editmenu.add_separator()

editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

app.mainloop()
root.destroy()


