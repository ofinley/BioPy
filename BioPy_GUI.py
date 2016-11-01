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
        

        #self.QUIT = Button(self)
        #self.QUIT["text"] = "Quit"
        #self.QUIT["fg"] = "red"
        #self.QUIT["command"] = self.quit

        #self.QUIT.pack({"side": "left"})
        


    def __init__(self, master=None):
        Frame.__init__(self,master)
        #self.pack()
        self.createWidgets()

        
#top.mainloop()
root = Tk()
app = Application(master=root)
app.master.title("BioPy v.1.0")
app.mainloop()
root.destroy()


