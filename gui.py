import tkinter
import mover
from tkinter import filedialog


def folder_selector():
    selcted_path = filedialog.askdirectory(initialdir=initial_directory,title="Please select a file directory")
    mover.main_function(selcted_path)


initial_directory = r"C:\Users\Yuga\Desktop"
caption_title = "This is a application to sort files according to their extensions."
root = tkinter.Tk()

root.title("File Organizer")
root.configure(bg="#132226")
root.resizable(False, False)
caption = tkinter.Label(root,text=caption_title,bg="#132226",fg="#1187a8",font=("Roboto Mono",10))
button_1 = tkinter.Button(root, text="Select Folder", command=folder_selector,bg="#132226", fg="#1187a8",font=("Roboto Mono",8))

caption.pack()
button_1.pack()

root.mainloop()