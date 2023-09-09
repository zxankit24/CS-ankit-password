import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create the length label and entry
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Create the complexity label and radio buttons
complexity_label = tk.Label(window, text="Password Complexity:")
complexity_label.pack()

complexity_var = tk.IntVar()
complexity_var.set(1)

complexity_radio1 = tk.Radiobutton(window, text="Letters", variable=complexity_var, value=1)
complexity_radio1.pack()

complexity_radio2 = tk.Radiobutton(window, text="Letters + Digits", variable=complexity_var, value=2)
complexity_radio2.pack()

complexity_radio3 = tk.Radiobutton(window, text="Letters + Digits + Special Characters", variable=complexity_var, value=3)
complexity_radio3.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create the password label
password_label = tk.Label(window, text="Generated Password: ")
password_label.pack()

# Start the main loop
window.mainloop()
