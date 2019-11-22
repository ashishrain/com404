from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Song Makers")

        #add components
        self.__add_heading_label()
        self.__add_subheading_label()
        self.__add_lyrics_frame()
        self.__add_lyrics_entry()
        self.__add_add_button()
        self.__add_subheading_two_label()
        self.__add_lyrics_display()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0,
                                column=0,
                                padx=50)
        #style
        self.heading_label.configure(text="Song Maker",
                                     font="Ariel 25")

    def __add_subheading_label(self):
        #create
        self.subheading_label = Label()
        self.subheading_label.grid(row=1,
                                   column=0,
                                   pady=10,
                                   sticky=W)

        #style
        self.subheading_label.configure(text="Lyric to add:",
                                        font="Ariel 16")

    def __add_lyrics_frame(self):
        #create
        self.lyrics_frame = Frame()
        self.lyrics_frame.grid(row=2,
                               column=0,
                               pady=10)

    def __add_lyrics_entry(self):
        #create
        self.lyrics_entry = Entry(self.lyrics_frame)
        self.lyrics_entry.pack(side=LEFT)
        #style
        self.lyrics_entry.configure(width=30)
        #events
        self.lyrics_entry.bind("<Return>", self.__add_button_clicked)

    def __add_add_button(self):
        #create
        self.add_button = Button(self.lyrics_frame)
        self.add_button.pack(side=RIGHT,
                             padx=10)
        #style
        self.add_button.configure(text="Add",
                                  font="Ariel 16")
        #events
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    def __add_subheading_two_label(self):
        #create
        self.subheading_two_label = Label()
        self.subheading_two_label.grid(row=3,
                                 column=0,
                                 sticky=W,
                                 pady=10)
        #style
        self.subheading_two_label.configure(text="Lyrics",
                                      font="Ariel 16")

    def __add_lyrics_display(self):
        #create
        self.lyrics_display = Listbox()
        self.lyrics_display.grid(row=4,
                                 column=0,
                                 pady=10)
        #style
        self.lyrics_display.configure(width=40)

    def __add_button_clicked(self, event):
        #get the lyrics from self.lyrics_entry() of __add_lyrics_entry()
        lyrics = self.lyrics_entry.get()

        #display
        self.lyrics_display.insert(END, lyrics)