import tkinter as tk
from tkinter import filedialog , messagebox

# main Window
root = tk.Tk()
root.title("Note APP")
root.geometry("800x600")

# create Text 
text = tk.Text(
    root,
    wrap = tk.WORD,
    font= ("Roboto",18)
)
text.pack(expand=True , fill=tk.BOTH)

# main Logic +.

# open New File 
def new_File():
    text.delete(1.0,tk.END)

def open_File():
    file_path = filedialog.askopenfilename(
        defaultextension = ".txt",
        filetypes= [("Text File ", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END , file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        filetypes= [("Text File ", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0 , tk.END))

    messagebox.showinfo("Info", "File Save Successfully")

# Create Menu Bar
menu = tk.Menu(root)
root.config(menu = menu)
file_menu = tk.Menu(menu)

menu.add_cascade(label = "file" , menu = file_menu)
file_menu.add_command(label = "New", command = new_File)
file_menu.add_command(label = "Open", command = open_File)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)



# This use for open GUI 
root.mainloop()
