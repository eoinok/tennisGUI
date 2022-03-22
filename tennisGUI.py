from Member import Member
from tkinter import *
class TennisGUI:
    
    def __init__(self, master):
        self.memberList = []
        self.master = master
        master.title("A Tennis Club GUI")

        
        self.label1 = Label(master, text="Enter name")
        self.label1.pack()
   
        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter age")
        self.label2.pack()

        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Enter smoker")
        self.label3.pack()
   
        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Enter member type")
        self.label4.pack()
   
        self.entry4 = Entry()
        self.entry4.pack()

        self.label5 = Label(master, text="Enter gender")
        self.label5.pack()
   
        self.entry5 = Entry()
        self.entry5.pack()

        self.quit = Button(master, text="QUIT", command=self.quit)
        self.quit.pack()

        self.addToListButton = Button(master, text="Add To List", command=self.addToList)
        self.addToListButton.pack()

        self.getAverageAgeButton = Button(master, text="Get Average Age", command=self.getAverageAge)
        self.getAverageAgeButton.pack()

    def quit(self):
        

    def addToList(self):
        print("add to list button works")
        #add code here to add each member to self.

    def getAverageAge(self):
        print("average age button works")
        #add code here to calculate the average age of the members in self.memberList


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
