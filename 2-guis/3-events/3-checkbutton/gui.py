from tkinter import *
from tkinter import messagebox

#create class
class Gui(Tk):

    #create constructor
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Passport Checker")

        #add components
        self.__add_heading_label()
        self.__add_subheading_label()
        self.__add_checkbutton_one_a()
        self.__add_checkbutton_one_b()
        self.__add_subheading_label_two()
        self.__add_checkbutton_two_a()
        self.__add_checkbutton_two_b()
        self.__add_subheading_label_three()
        self.__add_checkbutton_three_a()
        self.__add_checkbutton_three_b()
        self.__add_check_button()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0,
                                column=0,
                                pady=50,
                                columnspan=3)
        #style
        self.heading_label.configure(text="Passport Checker",
                                     font="Ariel 25")

    def __add_subheading_label(self):
        #create
        self.subheading_label = Label()
        self.subheading_label.grid(row=1,
                                   column=0,
                                   padx=10,
                                   sticky=W)
        #style
        self.subheading_label.configure(text="1. Photo matches face?",
                                        font="Ariel 16")

    def __add_checkbutton_one_a(self):
        #create
        self.var_one_a = IntVar()
        self.checkbutton_one_a = Checkbutton(variable=self.var_one_a)
        self.checkbutton_one_a.grid(row=2,
                                    column=1)
        #style
        self.checkbutton_one_a.configure(text="Yes",
                                       font="Ariel 16")

    def __add_checkbutton_one_b(self):
        #create
        self.checkbutton_one_b = Checkbutton()
        self.checkbutton_one_b.grid(row=2,
                                    column=2,
                                    padx=30)
        #style
        self.checkbutton_one_b.configure(text="No",
                                         font="Ariel 16")

    def __add_subheading_label_two(self):
        #create
        self.subheading_label_two = Label()
        self.subheading_label_two.grid(row=3,
                                   column=0,
                                   padx=10,
                                   sticky=W)
        #style
        self.subheading_label_two.configure(text="2. Passport has at least 6 months validity?",
                                        font="Ariel 16")

    def __add_checkbutton_two_a(self):
        #create
        self.var_two_a = IntVar()
        self.checkbutton_two_a = Checkbutton(variable=self.var_two_a)
        self.checkbutton_two_a.grid(row=4,
                                    column=1)
        #style
        self.checkbutton_two_a.configure(text="Yes",
                                       font="Ariel 16")

    def __add_checkbutton_two_b(self):
        #create
        self.checkbutton_two_b = Checkbutton()
        self.checkbutton_two_b.grid(row=4,
                                    column=2,
                                    padx=30)
        #style
        self.checkbutton_two_b.configure(text="No",
                                       font="Ariel 16")

    def __add_subheading_label_three(self):
        #create
        self.subheading_label_three = Label()
        self.subheading_label_three.grid(row=5,
                                   column=0,
                                   padx=10,
                                   sticky=W)
        #style
        self.subheading_label_three.configure(text="2. Visa, if required valid?",
                                        font="Ariel 16")

    def __add_checkbutton_three_a(self):
        #create
        self.var_three_a = IntVar()
        self.checkbutton_three_a = Checkbutton(variable=self.var_three_a)
        self.checkbutton_three_a.grid(row=6,
                                      column=1)
        #style
        self.checkbutton_three_a.configure(text="Yes",
                                       font="Ariel 16")

    def __add_checkbutton_three_b(self):
        #create
        self.checkbutton_three_b = Checkbutton()
        self.checkbutton_three_b.grid(row=6,
                                      column=2,
                                      padx=30)
        #style
        self.checkbutton_three_b.configure(text="No",
                                       font="Ariel 16")

    def __add_check_button(self):
        #create
        self.check_button = Button()
        self.check_button.grid(row=7,
                               column=0,
                               columnspan=3,
                               pady=10)
        #style
        self.check_button.configure(text="Check",
                                    font="Ariel 16")
        #events
        self.check_button.bind("<ButtonRelease-1>", self.__check_button_clicked)

    def __check_button_clicked(self, event):
        #get if checked or not from all the checkbuttons
        one_yes = self.var_one_a.get()
        two_yes = self.var_two_a.get()
        three_yes = self.var_three_a.get()

        #display using if statement
        if ((one_yes == 1) and (two_yes == 1) and (three_yes == 1)):
            messagebox.showinfo("Proceed", "You can go through.")
        else:
            messagebox.showinfo("Cannot proceed", "Sorry, you cannot proceed any further")
        
