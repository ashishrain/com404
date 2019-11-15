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
        self.add_heading()
        self.add_heading_two()
        self.add_email_label()
        self.add_email_entry()
        self.add_button()

    def add_heading(self):
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=1, columnspan=2)
        #style
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     bg="#ececec",
                                     fg="#000000",
                                     font="Ariel 24")

    def add_heading_two(self):
        self.heading_two_label = Label()
        self.heading_two_label.grid(row=2, column=1, columnspan=2)
        #style
        self.heading_two_label.configure(text="Please enter your email below to receive our newsletter.",
                                  bg="#ececec",
                                  fg="#000000",
                                  font="Ariel 10")

    def add_email_label(self):
        self.email_label = Label()
        self.email_label.grid(row=3, column=1, columnspan=1)
        #style
        self.email_label.configure(text="Email:",
                                   bg="#ececec",
                                   fg="#000000",
                                   font="Ariel 10",
                                   height=2)

    def add_email_entry(self):
        self.email_entry = Entry()
        self.email_entry.grid(row=3, column=2, columnspan=1)
        #style
        self.email_entry.configure(bg="#dedede",
                                   width=50)

    def add_button(self):
        #create
        self.button = Button()
        self.button.grid(row=4, column=1, columnspan=2)
        #style
        self.button.configure(text="Subscribe")
