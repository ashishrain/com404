from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.first_cactus_image = PhotoImage(file="cacto.gif")
        self.second_cactus_image = PhotoImage(file="cacti.gif")
        
        # set window attributes
        self.title("Cactus Flipping")
        
        # add components
        self.__add_heading_label()
        self.__add_cactus_image_label()
        self.__add_flip_button()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, pady=20)
        #style
        self.heading_label.configure(text="Cactus",
                                     font="Ariel 25",
                                     fg="#008080")

    def __add_cactus_image_label(self):
        #create
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        #style
        self.cactus_image_label.configure(image=self.first_cactus_image,
                                    height=500,
                                    width=500)

    def __add_flip_button(self):
        #create
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0, ipadx=100, pady=20)
        #style
        self.flip_button.configure(text="Flip",
                                    font="Ariel 16",
                                   fg="#ffffff",
                                   bg="#008080")
        #events
        self.flip_button.bind("<Button-1>", self.__left_mouse_clicked)
        self.flip_button.bind("<Button-3>", self.__right_mouse_clicked)
        

    def __left_mouse_clicked(self, event):
        #display
        self.cactus_image_label.configure(image = self.second_cactus_image)
        self.heading_label.configure(text="")
        

    def __right_mouse_clicked(self, event):
        #display
        self.cactus_image_label.configure(image = self.first_cactus_image)
        self.heading_label.configure(text="Cactus")
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
