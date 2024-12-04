import random
import string
import tkinter as tk
from tkinter import messagebox


# Password generation function
def gen_passwrd(length=20, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation    
    all_chars = ''
    if include_lowercase:
        all_chars += lowercase
    if include_uppercase:
        all_chars += uppercase
    if include_digits:
        all_chars += digits
    if include_special_chars:
        all_chars += special_chars
# Display error if no checkbox has been selected      
    if not all_chars:
        messagebox.showerror("Error", "Please at least mark one checkbox")
        return ''
    
# Generate a random password using the options from the checkboxes    
    password = random.choices(all_chars, k=length)
    random.shuffle(password) # For random generation
    return ''.join(password)

# Password strength function
def password_strength(password):
    score = 0 # Base password score
    if len(password) <= 5: # If password length is greater or equal than 5, add 3 points to total score
        score += -3  
    if len(password) >= 13: # If password length is less or equal than 13, only add 2 points
        score += 2  
          
# Add 1 point to total score per checkbox marked        
    if any(i.islower() for i in password):  
        score += 1         
    if any(i.isupper() for i in password):
        score += 1
    if any(i.isdigit() for i in password):
        score += 1
    if any(i in string.punctuation for i in password):
        score += 1
        
# Measure password strength     
    if score <= 2:
        return "weak", "#FF0000" # Red text if password is weak
    elif score == 3:
        return "medium", "#FFA500" # Yellow text if is medium
    elif score == 4:
        return "strong", "#008000" # Green If is strong
    elif score >= 5:
        return "super strong", "#800080" # Purple if is super strong

# Function to generate the password when button is clicked
def btn_gen_password():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Password length needs to be greater than 0") # Error if user inserted "0" as password length
    except ValueError as e:
        messagebox.showerror("Invalid Data", f"Enter a number to use as password length\n{e}") # Error if user does not insert a number to use as password length
        return
    
# Use the characters that are marked by a checkbox
    include_lower = var_lower.get()
    include_upper = var_upper.get()
    include_digits = var_digits.get()
    include_special = var_special.get()
    
    password = gen_passwrd(length, include_lower, include_upper, include_digits, include_special)
    if password:
        strength, color = password_strength(password)
        label_result.config(text=f"Your password is: {password}") # Display the password generated
        label_strength.config(text=f"{strength}", fg=color) # Display the strength of the password generated and it's color

# Function to copy the password
def btn_copy_password():
    password = label_result.cget("text").replace("Your password is: ", "") # Get the password generated
    if password:
        root.clipboard_clear() 
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Password Copied", "Password copied successfully!") # Display alert if a generated password was copied
    else:
        messagebox.showwarning("Cannot Copy", "Create a password first!") # Display an error if the user failed to generate a password before pressing the copy button

# UI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("700x500")
root.configure(bg="#2e2e2e") # UI background color

# Create a frame to hold the main content and center it
frame = tk.Frame(root, bg="#3a3a3a")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Password length input
label_length = tk.Label(frame, text="Insert password length:", font=("Arial", 12), bg="#3a3a3a", fg="white")
label_length.grid(row=0, column=0, pady=5)

entry_length = tk.Entry(frame, bg="#5a5a5a", fg="white")
entry_length.grid(row=1, column=0, pady=5)

"""Checkbox options"""

# Lowercase
var_lower = tk.BooleanVar(value=True)
checkbox_lower = tk.Checkbutton(frame, text="Include lowercase", variable=var_lower, bg="#3a3a3a")
checkbox_lower.grid(row=2, column=0, pady=5)

# Uppercase
var_upper = tk.BooleanVar(value=True)
checkbox_upper = tk.Checkbutton(frame, text="Include uppercase", variable=var_upper, bg="#3a3a3a")
checkbox_upper.grid(row=3, column=0, pady=5)

# Numbers
var_digits = tk.BooleanVar(value=True)
checkbox_digits = tk.Checkbutton(frame, text="Include digits", variable=var_digits, bg="#3a3a3a")
checkbox_digits.grid(row=4, column=0, pady=5)

# Special characters
var_special = tk.BooleanVar(value=True)
checkbox_special = tk.Checkbutton(frame, text="Include special characters", variable=var_special, bg="#3a3a3a")
checkbox_special.grid(row=5, column=0, pady=5)

""""""

# Button to generate password
button_generate = tk.Button(frame, text="Generate", command=btn_gen_password)
button_generate.grid(row=6, column=0, pady=10)

# Label to display the generated password
label_result = tk.Label(frame, text="Your password is: ", font=("Arial", 12), bg="#3a3a3a", fg="white")
label_result.grid(row=7, column=0, pady=5)

# Label to display the password strength
label_strength = tk.Label(frame, text="Strength: ", font=("Arial", 12), bg="#3a3a3a")
label_strength.grid(row=8, column=0, pady=5)

# Button to copy the password to clipboard
button_copy_password = tk.Button(frame, text="Copy to clipboard", command=btn_copy_password)
button_copy_password.grid(row=9, column=0, pady=10)

root.mainloop()