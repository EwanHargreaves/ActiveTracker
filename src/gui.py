from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = self.start_window()

        self.main_frame = self.create_main_frame()

        self.button_frame = self.create_button_frame()

        self.git_reminder_check = False
        self.Option_frame = self.create_options_frame()

        self.root.mainloop()
    
    def start_window(self):
        root = Tk()
        root.title("Activity Tracker")
        return root
    
    def create_main_frame(self):
        main_frame = ttk.Frame(self.root, padding="20 20 10 10")
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        main_frame.columnconfigure(0,weight=1)
        main_frame.rowconfigure(0,weight=1)
        return main_frame
    
    def create_button_frame(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        button_frame.columnconfigure(0,weight=1)
        button_frame.rowconfigure(0,weight=1)

        start_btn = ttk.Button(button_frame, width=10, text="Start", command=self.test_buttnon)
        start_btn.grid(column=0,row=0, sticky=(W,E))

        stop_btn = ttk.Button(button_frame, width = 10, text="Stop", command=self.test_buttnon)
        stop_btn.grid(column=1,row=0,sticky=(W,E))

        data_btn = ttk.Button(button_frame, width = 10, text="Data", command=self.test_buttnon)
        data_btn.grid(column=0,row=1,sticky=(W,E))

        Chart_btn = ttk.Button(button_frame, width = 10, text="Chart", command=self.test_buttnon)
        Chart_btn.grid(column=1,row=1,sticky=(W,E))

        for child in button_frame.winfo_children():
            child.grid_configure(padx=10, pady=5)

        return button_frame

    def test_buttnon(self):
        print("Button Pressed")
    
    def create_options_frame(self):
        options_frame = ttk.Frame(self.main_frame)
        options_frame.grid(column=0,row=1, sticky=(N, W, S))
        options_frame.columnconfigure(0,weight=1)

        git_reminder_label = ttk.Label(options_frame, text="Git Reminder")
        git_reminder_label.grid(row=0, column=0, padx=5, pady=5,sticky=(W))

        git_reminder_checkbox = ttk.Checkbutton(options_frame, variable=self.git_reminder_check)
        git_reminder_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky=(W))

        return options_frame