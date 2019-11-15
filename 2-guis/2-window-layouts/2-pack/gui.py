#import all the classes from the tkinter library
from tkinter import *

#class definition for our Gui
class Gui (Tk):
    #constructor for making Gui objects
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="#ececec",
                       height=500,
                       width=500)

        #add components to the window
        self.add_main_frame()
        self.add_heading()
        self.add_heading_two()
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()
        self.add_button()

    def add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.pack()

    def add_heading(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.pack(fill=X)
        #style
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     bg="#ececec",
                                     fg="#000000",
                                     font="Ariel 24")

    def add_heading_two(self):
        self.heading_two_label = Label(self.main_frame)
        self.heading_two_label.pack(fill=X)
        #style
        self.heading_two_label.configure(text="Please enter your email below to receive our newsletter.",
                                  bg="#ececec",
                                  fg="#000000",
                                  font="Ariel 10")

    def add_email_frame(self):
        self.email_frame = Frame(self.main_frame)
        self.email_frame.pack(fill=X)

    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        #style
        self.email_label.configure(text="Email:",
                                   bg="#ececec",
                                   fg="#000000",
                                   font="Ariel 10")

    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)
        #style
        self.email_entry.configure(bg="#dedede",
                                   width=50)

    def add_button(self):
        #create
        self.button = Button(self.main_frame)
        self.button.pack(fill=X)
        #style
        self.button.configure(text="Subscribe")
