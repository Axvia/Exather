import tkinter as tk  
from tkinter import Label, Entry, StringVar, ttk, filedialog, HORIZONTAL
import sys
import os
import time
from time import sleep

####################### Source Path #######################
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        # base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

######################## Placeholder #########################
class EntryWithPlaceholder(Entry):
	def __init__(self, *args, **kwargs):
		self.placeholder = kwargs.pop("placeholder", "")
		super().__init__(*args, **kwargs)

		self.insert("end", self.placeholder)
		self.bind("<FocusIn>", self.remove_placeholder)
		self.bind("<FocusOut>", self.add_placeholder)

	def remove_placeholder(self, event):
		"""Remove placeholder text, if present"""
		if self.get() == self.placeholder:
			self.delete(0, "end")

	def add_placeholder(self,event):
		"""Add placeholder text if the widget is empty"""
		if self.placeholder and self.get() == "":
			self.insert(0, self.placeholder)

######################## Window ##############################
app = tk.Tk()
app.iconbitmap(resource_path('icon/app.ico')) # Copy and paste the icon adress
app.title("Exather") # Name

######################## Design ###############################
GlobalInputBoxwidth = 25
WindowMargin = tk.LabelFrame(app, text="Exather", padx=5, pady=5)
WindowMargin.pack(padx=5, pady=5)

# Command 1
def BrowseFile():
    #### Select Folder ###
    # filename = filedialog.askdirectory()
    # InputBox_toFile.set(filename)
    # print(filename)
    #### Select File ###
    try:
        print('[Browse]: Start Browsing')
        inputFile = filedialog.askopenfile(initialdir="/")
        targetFile = InputBox_toFile.set(inputFile.name)
        print(targetFile)
    except Exception:
        print('[Browse]: Stop Browsing')

def start():
    StartButton['state'] = "disabled" # Disable button once start
    os.system(resource_path(f'software/myApp.exe {InputBox_toFile.get()}'))
    for i in range(1,101,1):
        ProgBar['value'] = i
        app.update_idletasks()
        sleep(0.01)
    ProgBar['value'] == 100
    print("Complete")
    print(InputBox_toFile.get())
    StartButton['state'] = "enable" # Enable button

########### ROW 1 ################
# Label 1
label_toPath = tk.Label(WindowMargin, text="Target: ")
label_toPath.grid(row=1, column=1, sticky=tk.E)
# Input Box 1
InputBox_toFile =   StringVar(None)
InputBox_toPath =   EntryWithPlaceholder(WindowMargin, width=GlobalInputBoxwidth, placeholder="A path to JavaScript file", textvariable=InputBox_toFile)
InputBox_toPath.grid(row=1,column=2)
# Button Box 1
Convert_toExe = ttk.Button(WindowMargin, text = "Browse", command=BrowseFile)
Convert_toExe.grid(row=1,column=3)
############ ROW 2 ###############
# Label 2
label_ProcLab = tk.Label(WindowMargin, text="Process: ")
label_ProcLab.grid(row=2, column=1, sticky=tk.E)
# Progress Bar 1
ProgBar = ttk.Progressbar(WindowMargin,orient=HORIZONTAL, length=153)
ProgBar.grid(row=2,column=2)
StartButton = ttk.Button(WindowMargin, text="Start", command=start)
StartButton.grid(row=2,column=3)

# Keep the window open
app.mainloop()


# targFile = input('Please provide a path to jsFile: ')
# executeFile = os.system(resource_path(f'software/myApp.exe {targFile}'))