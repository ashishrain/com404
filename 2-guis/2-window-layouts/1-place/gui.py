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
                       height=100,
                       width=400)

        #add components to the window
        self.__add_heading_label()
        self.__add_heading_label_two()
        self.__add_heading_label_three()
        self.__add_three_entry()
        self.__add_button()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.place(x=15, y=0)
        #style
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     bg="#ececec",
                                     fg="#000000",
                                     font="Ariel 16")
        #handle events

    def __add_heading_label_two(self):
        #create
        self.heading_label = Label()
        self.heading_label.place(x=5, y=50)
        #style
        self.heading_label.configure(text="Please enter your email below to receive our newsletter.",
                                  bg="#ececec",
                                  fg="#000000",
                                  font="Ariel 10")

    def __add_heading_label_three(self):
        #create
        self.heading_label = Label()
        self.heading_label.place(x=5, y=75)
        #style
        self.heading_label.configure(text="Email:",
                                     bg="#ececec",
                                     fg="#000000",
                                     font="Ariel 10")

    def __add_three_entry(self):
        #create
        self.three_entry = Entry()
        self.three_entry.place(x=50, y=75)
        #style
        self.three_entry.configure(bg="#dedede",
                                   width=30)

    def __add_button(self):
        #create
        self.button = Button()
        self.button.place(x=0, y=100)
        #style
        self.button.configure(text="Subscribe",
                              width=50)
