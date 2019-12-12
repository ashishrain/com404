from tkinter import *
from tkinter import messagebox

#create class
class Gui(Tk):

    #create constructor
    def __init__(self):
        super().__init__()

        #load resources
        self.default_image = PhotoImage(file="default.gif")

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="#ccc",
                       pady=10,
                       padx=10)
        #how to put padding in the window(1 mark)

        #add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_subheading_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_default_image_label()
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
                                pady=10) #is this the right way to put padding top and bottom?
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     font="Arial 14")

    def __add_subheading_label(self):
        self.subheading_label = Label(self.outer_frame)
        self.subheading_label.grid(row=1,
                                   column=0,
                                   columnspan=3,
                                   pady=10,
                                   padx=10) #is this the right way to put padding all the way round?
        self.subheading_label.configure(text="Please enter your email below to receive our newsletter.",
                                        font="Arial 10",
                                        justify=LEFT)#how do i do text left justified?


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

    def __add_default_image_label(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2,
                                      column=2,
                                      sticky=W,
                                      padx=10,
                                      pady=10)
        self.default_image_label.configure(image=self.default_image,
                                           height=15,
                                           width=15)

    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=3,
                                   column=0,
                                   columnspan=3,
                                   sticky=N+E+S+W)
        self.subscribe_button.configure(text="Subscribe",
                                        font="Arial 10",
                                        bg="#fee")
        #events
        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)

    def __subscribe_button_clicked(self, event):
        messagebox.showinfo("Newsletter", "Subscribed!")

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
