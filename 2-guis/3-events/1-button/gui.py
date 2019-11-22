from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0,
                                column=0,
                                sticky="N")
        #style
        self.heading_label.configure(text="Entrance Ticket",
                                           fg="#000110",
                                           font="#Ariel 25")
        
    def __add_instruction_label(self):
        #create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1,
                                    column=0,
                                    sticky=N,
                                    pady=20)
        #style
        self.instruction_label.configure(text="How many tickets are needed:",
                                               font="Ariel 16",
                                               fg="#000110")
        
    def __add_tickets_entry(self):
        #create
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2,
                                column=0,
                                pady=20)
        #style
        #self.__add_tickets_entry.configure()
        
    def __add_buy_button(self):
        #create
        self.buy_button = Button()
        self.buy_button.grid(row=3,
                            column=0,
                            pady=20)
        #style
        self.buy_button.configure(text="Submit",
                                        font="Ariel 16",
                                        fg="#000110")
        #events
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        #get the amount from self.tickets_entry of __add_tickets_entry()
        no_of_tickets =  int(self.tickets_entry.get())

        #display using  if statement
        if (no_of_tickets == 1):
            messagebox.showinfo("Purchased!", "You have purchased 1 ticket!")
        elif (no_of_tickets > 1):
            messagebox.showinfo("Purchased!", "You have purchased " + str(no_of_tickets) + " tickets!")
        else:
            messagebox.showinfo("Error!", "Invalid amount. Please try again.")        

        
