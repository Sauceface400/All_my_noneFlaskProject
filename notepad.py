from tkinter import *
from tkinter.filedialog import *

__file = None

#creating the window for the notepad
def main():
    root = Tk()
    gui = window(root)
    gui.root.mainloop()

class window():
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x500")

        #create the section that we write the text
        self.textspace = Text(self.root)
        self.textspace.grid(row=1, column=0)
        
        #buttons for the notepad
        Button(self.root, text="Save as", command=self.save_as).grid(row=0, column=0)
        Button(self.root, text="Save", command=self.savefile).grid(row=0, column=1)
        Button(self.root, text="Open file", command=self.openfile).grid(row=0, column=2)
    
    def save_as(self):
        save_asGUI = Tk()
        save_asGUI.geometry("200x400")
        contentfile = self.textspace.get(0.0, END)
        self._f = FileDialog.asksaveasfilename(defaultextention=".txt", filetypes=(("Text Documents","*.txt")))
        
        #This is the function for the naming def
        def writefile():
            with open(FileName.get() + ".txt", "w+") as file:
                file.write(contentfile)
                file.close()
                save_asGUI.destroy()
        Label(save_asGUI, text="Save File As").grid(row=0, column=0)
        FileName = Entry(save_asGUI, width=35)
        FileName.grid(row=0, column=0)

        Button(save_asGUI, text="Save As", command=writefile).grid(row=0, column=1)

    def savefile(self):
        contentfile = self.textspace.get(1.0, END)
        try:
            with open(self._f, 'w') as file:
                file.write(contentfile)
        except AttributeError:
            self.save_as()

    def openfile(self):
        openfileGUI = Tk()
        openfileGUI.geometry("200x400")
        
        #this is for the function for the opening file def
        def salectingFile():
            try:
                with open(FileName.get() ,"r") as file:
                    self.textspace.delete(0.0, END)
                    self.textspace.insert(0.0, file.read())
                    file.close()
                    openfileGUI.destroy()
            except FileNotFoundError:
                FileName.delete(0.0, END)
                FileName.insert(0.0, "FILE NOT FOUND. TRY ANOTHER")
        Label(openfileGUI, text="Open file").grid(row=0, column=0)
        FileName = Entry(openfileGUI, width=35)
        FileName.grid(row=0, column=0)

        Button(openfileGUI, text="Open", command=salectingFile).grid(row=0, column=1)

main()