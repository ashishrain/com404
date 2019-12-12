from tkinter import *
from tkinter import messagebox

#create class
class Gui(Tk):

    #create constructor
    def __init__(self):
        super().__init__()

        #load resources
        self.default_image = PhotoImage(file="default.gif")
        self.yes_image = PhotoImage(file="yes.gif")
        self.no_image = PhotoImage(file="no.gif")

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="#ccc",
                       pady=10,
                       padx=10)

        #add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_subheading_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_default_image_label()
        self.__add_type_label()
        self.__add_type_optionmenu()
        self.__add_subscribe_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0,
                              column=0)
        self.outer_frame.configure(bg="#eee")

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0,
                                column=0,
                                columnspan=3,
                                pady=10)
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     font="Arial 14")

    def __add_subheading_label(self):
        self.subheading_label = Label(self.outer_frame)
        self.subheading_label.grid(row=1,
                                   column=0,
                                   columnspan=3,
                                   pady=10,
                                   padx=10)
        self.subheading_label.configure(text="Please enter your email below to receive our newsletter.",
                                        font="Arial 10",
                                        justify=LEFT)


    def __add_email_label(self):
        self.email_label = Label(self.outer_frame)
        self.email_label.grid(row=2,
                              column=0,
                              padx=10,
                              sticky=E)
        self.email_label.configure(text="Email:",
                                   font="Arial 10")

    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2,
                              column=1,
                              sticky=W)
        self.email_entry.configure(fg="#f00",
                                   width=30,
                                   border=2)
        #events
        self.email_entry.bind("<KeyRelease>", self.__checking)

    def __checking(self, event):
        email = len(self.email_entry.get())

        #if statement
        if (email > 0):
            self.default_image_label.configure(image=self.yes_image,
                                               height=15,
                                               width=15)
        elif (email == 0):
            self.default_image_label.configure(image=self.no_image,
                                               height=15,
                                               width=15)
        else:
            self.default_image_label.configure(image=self.default_image,
                                               height=15,
                                               width=15)

    def __add_default_image_label(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2,
                                      column=2,
                                      sticky=W,
                                      padx=10)
        self.default_image_label.configure(image=self.default_image,
                                           height=15,
                                           width=15)

    def __add_type_label(self):
        self.type_label = Label(self.outer_frame)
        self.type_label.grid(row=3,
                             column=0,
                             columnspan=1,
                             sticky=E,
                             padx=10)
        self.type_label.configure(text="Type",
                                  font="Arial 10")

    def __add_type_optionmenu(self):
        self.var_optionmenu = StringVar()
        self.var_optionmenu.set("Weekly")
        self.type_optionmenu = OptionMenu(self.outer_frame, self.var_optionmenu, "Weekly", "Monthly", "Yearly")
        self.type_optionmenu.grid(row=3,
                                  column=1,
                                  columnspan=2,
                                  sticky=W,
                                  pady=10)
        self.type_optionmenu.configure(width=30)
        
        
    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=4,
                                   column=0,
                                   columnspan=3,
                                   sticky=N+E+S+W,
                                   pady=10)
        self.subscribe_button.configure(text="Subscribe",
                                        font="Arial 10",
                                        bg="#fee")
        #events
        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)

    def __subscribe_button_clicked(self, event):
        email_len = len(self.email_entry.get())
        type_chosen = self.var_optionmenu.get()

        #if statements
        if (email_len == 0):
            messagebox.showinfo("Newsletter", "Please enter your email!")
        elif (type_chosen == "Weekly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this every Monday.")
        elif (type_chosen == "Monthly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the monthly newsletter! You will receive this on the first day of each month.")
        elif (type_chosen == "Yearly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the yearly newsletter! You will reeive this at the start of each year.")

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
