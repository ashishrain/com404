from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        #self.none_image = PhotoImage(file="none.gif")
        self.yes_image = PhotoImage(file="yes.gif")
        self.no_image = PhotoImage(file="no.gif")
        
        # set window attributes
        self.title("Hotel Check In")
        
        # add components
        self.__add_heading_label()
        self.__add_subheading_label_one()
        self.__add_entry_one()
        self.__add_status_one_label()
        self.__add_subheading_label_two()
        self.__add_entry_two()
        self.__add_status_two_label()
        self.__add_subheading_label_three()
        self.__add_entry_three()
        self.__add_status_three_label()
        self.__add_check_button()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=3)
        #style
        self.heading_label.configure(text="Hotel Check In",
                                     font="Roboto 25")

    def __add_subheading_label_one(self):
        #create
        self.subheading_label_one = Label()
        self.subheading_label_one.grid(row=1, column=0, sticky=W)
        #style
        self.subheading_label_one.configure(text="Name:",
                                            font="Roboto 16")

    def __add_entry_one(self):
        #create
        self.entry_one = Entry()
        self.entry_one.grid(row=1, column=1, padx=20, pady=20)
        #style
        self.entry_one.configure(width=30)
        #events
        self.entry_one.bind("<KeyRelease>", self.__checking_one)

    def __checking_one(self, event):
        name_len = len(self.entry_one.get())
        
        if name_len == 0:
            self.status_one_label.configure(image = self.no_image)
        else:
            self.status_one_label.configure(image = self.yes_image)

    def __add_status_one_label(self):
        #create
        self.status_one_label = Label()
        self.status_one_label.grid(row=1, column=2)
        #style
        self.status_one_label.configure(image=self.no_image,
                                        height=30,
                                        width=30)

    def __add_subheading_label_two(self):
        #create
        self.subheading_label_two = Label()
        self.subheading_label_two.grid(row=2, column=0, sticky=W)
        #style
        self.subheading_label_two.configure(text="Passport Number:",
                                            font="Roboto 16")

    def __add_entry_two(self):
        #create
        self.entry_two = Entry()
        self.entry_two.grid(row=2, column=1, padx=20, pady=20)
        #style
        self.entry_two.configure(width=30)
        #events
        self.entry_two.bind("<KeyRelease>", self.__checking_two)

    def __checking_two(self, event):
        passport_len = len(self.entry_two.get())
             
        if passport_len == 0:
            self.status_two_label.configure(image = self.no_image)
        else:
            self.status_two_label.configure(image = self.yes_image)

    def __add_status_two_label(self):
        #create
        self.status_two_label = Label()
        self.status_two_label.grid(row=2, column=2)
        #style
        self.status_two_label.configure(image=self.no_image,
                                        height=30,
                                        width=30)

    def __add_subheading_label_three(self):
        #create
        self.subheading_label_two = Label()
        self.subheading_label_two.grid(row=3, column=0, sticky=W)
        #style
        self.subheading_label_two.configure(text="No. of nights:",
                                            font="Roboto 16")

    def __add_entry_three(self):
        #create
        self.entry_three = Entry()
        self.entry_three.grid(row=3, column=1, padx=20, pady=20)
        #style
        self.entry_three.configure(width=30)
        #style
        self.entry_three.bind("<KeyRelease>", self.__checking_three)

    def __checking_three(self, event):
        no_of_nights = int(self.entry_three.get())
        no_of_nights_len = len(self.entry_three.get())
            
        if (no_of_nights_len == 0) or (no_of_nights > 365):
            self.status_three_label.configure(image = self.no_image)       
        else:
            self.status_three_label.configure(image = self.yes_image)

    def __add_status_three_label(self):
        #create
        self.status_three_label = Label()
        self.status_three_label.grid(row=3, column=2)
        #style
        self.status_three_label.configure(image=self.no_image,
                                        height=30,
                                        width=30)

    def __add_check_button(self):
        #create
        self.check_button = Button()
        self.check_button.grid(row=4, column=0, columnspan=3, pady=20, ipadx=20)
        #style
        self.check_button.configure(text="Check In",
                                    font="Roboto 16")
        #events
        self.check_button.bind("<Button-1>", self.__checking)

    def __checking(self, event):

        name_len = len(self.entry_one.get())
        passport_len = len(self.entry_two.get())
        no_of_nights = int(self.entry_three.get())
        no_of_nights_len = len(self.entry_three.get())

        if name_len == 0:
            self.status_one_label.configure(image = self.no_image)
        else:
            self.status_one_label.configure(image = self.yes_image)

        if passport_len == 0:
            self.status_two_label.configure(image = self.no_image)
        else:
            self.status_two_label.configure(image = self.yes_image)

        if (no_of_nights_len == 0) or (no_of_nights > 365):
            self.status_three_label.configure(image = self.no_image)       
        else:
            self.status_three_label.configure(image = self.yes_image)

        

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
