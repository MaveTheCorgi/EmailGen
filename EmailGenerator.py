import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
import os.path
import random
from randomword import RandomWord

root = tk.Tk()
root.title("Email Generator")
root.iconbitmap("C:/Users/MaveTheCorgi/PycharmProjects/EmailGenerator/HadesLogo.ico")
root.configure(background='black')
frame = tk.Frame(root, padx=5, pady=5, bg="black")
s = ttk.Style()
rw = RandomWord()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red', troughcolor="black", bordercolor="red", lightcolor="red", darkcolor="red")
emailInput = tk.Entry(frame, width=50, bg="black", fg="red", justify="center")
emailInput.configure(insertbackground='red')
emailInput.grid(row=1, column=0, columnspan=3, padx=15, pady=0)
fileInput = tk.Entry(frame, width=50, bg="black", fg="red")
fileInput.configure(insertbackground='red')
fileInput.grid(row=3, column=0, columnspan=2, padx=15, pady=0)
index = 0
emailAmount = 0
usePass = tk.IntVar()
emailLabel = tk.Label(frame, text="Amount of emails:", bg="black", fg="red").grid(row=0, column=0)
fileLabel = tk.Label(frame, text="Text file to store emails:", bg="black", fg="red").grid(row=2, column=0)
passLabel = tk.Label(frame, text="Email password", bg="black", fg="red")
passInput = tk.Entry(frame, width=28, bg="black", fg="red")
passInput.configure(insertbackground='red')


def update_pass_fields():
    if usePass.get() == 1:
        passLabel.grid(row=4, column=1, sticky="w")
        passInput.grid(row=5, column=1, sticky="w")
    else:
        passLabel.grid_forget()
        passInput.grid_forget()


progress = ttk.Progressbar(frame, style="red.Horizontal.TProgressbar", orient="horizontal", mode="determinate")
usePassCheckbutton = tk.Checkbutton(frame, text="Add password", variable=usePass, command=update_pass_fields, bg="black", fg="red", activebackground="black", activeforeground="red").grid(row=5, column=0, sticky="w")


def generate_emails():
    global index
    global emailAmount
    global progress
    global rw

    if emailAmount > index:
        index = index + 1
        root.title("Email Generator: Generating " + str(index) + " out of " + str(emailAmount) + " emails...")

        progress.step(0.999999999999)
        result = rw.get()
        result2 = rw.get()
        email = result['word'] + str(random.randint(0, 1000)) + "." + result2['word'] + str(random.randint(0, 1000)) + "@hotmail.com"

        if usePass.get() == 1:
            fileLine = email + ":" + passInput.get() + "\n"
        else:
            fileLine = email + "\n"

        file1 = open(fileInput.get(), "a")
        file1.write(fileLine)
        file1.close()

        root.after(1, generate_emails)
    else:
        root.title("Email Generator")
        messagebox.showinfo(" Emails successfully generated!",
                            "You have successfully generated " + str(emailAmount) + " emails!")


def start_gen_phase():
    global emailAmount
    global index
    global progress
    try:
        emailAmount = int(emailInput.get())

        if os.path.isfile(fileInput.get()):
            index = 0
            progress = ttk.Progressbar(frame, style="red.Horizontal.TProgressbar", orient="horizontal", maximum=emailAmount, mode="determinate")
            progress.grid(row=6, column=0, columnspan=4, sticky="w, e")
            root.after(1, generate_emails)
        else:
            messagebox.showerror("Something went wrong!", "The file you specified doesn't exist!")
    except ValueError:
        if emailInput.get() != "":
            messagebox.showerror("Something went wrong!", "The value '" + emailInput.get() + "' is not a number!")
        else:
            messagebox.showerror("Something went wrong!", "Please fill in the amount of emails you want generated!")


def browse():
    root.filename = filedialog.askopenfilename(initialdir="./", title="Select email save file", filetypes=[("text files", "*.txt")])
    if root.filename != "":
        fileInput.insert(0, root.filename)


progress.grid(row=6, column=0, columnspan=4, sticky="w, e")
fileButton = tk.Button(frame, text="Browse", bg="black", fg="red", command=browse).grid(row=3, column=3)
frame.pack(padx=10, pady=10)
generateButton = tk.Button(frame, text="Generate Emails", command=start_gen_phase, bg="black", fg="red", pady=5).grid(row=5, column=3, pady=5, sticky="e")

root.mainloop()


