#Text Editor App. Note Application.
# tkinter module and library - collection for creating GUI apps

import tkinter as tk
from tkinter import filedialog,messagebox

# Main Window code
root = tk.Tk()
root.title("Simple view Editor")
root.geometry("800x600")

# Create Text area
text= tk.Text(
    root,
    wrap=tk.WORD,      #text wrap by wrod (Not character)
    font=("Arial",18)
)
text.pack(expand=True,fill=tk.BOTH)

# Main Logic starts now

#Function 1 - to create a new file
def new_file():
    text.delete("1.0", tk.END)

#Function 2 - to open a new file
def open_file():
    # open file dialogue
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text File","*.txt")]
    )
    if file_path:
        # open file
        with open(file_path, "r" , encoding="utf-8") as file:
            # clear old text
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())


# function 3 - Save the file - write operation must perform
def save_file():
    #open save file dialogue
    file_path= filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File","*.txt")]
    )
    if file_path:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(text.get("1.0", tk.END))

    messagebox.showinfo("Info","File Saved Successfully Done")

# Menu Bar
menu = tk.Menu(root)
root.config(menu= menu)

file_menu = tk.Menu(menu)

#New, open , Save, Exit
#add filemenu to menu bar
menu.add_cascade(label="File", menu=file_menu)



file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)



#Starts and keeps the window open
root.mainloop()
