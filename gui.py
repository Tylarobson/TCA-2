from tkinter import *

class part_a(Tk):
    def __init__(self):
        super().__init__()

        self.title("Newsletter")
        self.configure(bg="#eee", height=200, width=360, pady=10)

        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.place (x=10, y=10, relheight = 0.84, relwidth=0.94)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.place(x=20, y=10)
        self.heading_label.configure(   bg="#eee", 
                                        font="Arial 14", 
                                        text="RECIEVE OUR NEWSLETTER")
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.place(x=10, y=43)
        self.instruction_label.configure (bg="#eee",
                                            justify=LEFT,
                                            pady=10,
                                            text="Please enter your email below to recieve our newsletter")
    def __add_email_label(self):
        self.email_label = Label(self.outer_frame)
        self.email_label.place(x=10, y=102)
        self.email_label.configure( text="Email:")
    
    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.place(x=60, y=102)
        self.email_entry.configure(width=30)

    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.place(x=0, y=140)
        self.subscribe_button.configure(bg="#fee", 
                                            text="Subscribe",
                                            width=47)
                                         