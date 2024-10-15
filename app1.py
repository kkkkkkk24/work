import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["user_data"]  # Database name
    collection = db["user_entries"]  # Collection name
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

# Function to handle form submission
def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    gender = gender_var.get()

    if not name or not email or not phone or not address or not gender:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Data to store in MongoDB
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "gender": gender,
    }

    try:
        collection.insert_one(data)
        messagebox.showinfo("Success", f"Data for {name} saved!")
        clear_form()  # Clear the form after submission
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

# Function to clear form inputs
def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    gender_var.set(None)

# Create the main Tkinter window
root = tk.Tk()
root.title("User Data Entry Form")
root.geometry("400x400")
root.config(bg="white")

# Header section
header_frame = tk.Frame(root, bg="white")
header_frame.pack(pady=10)

icon_label = tk.Label(header_frame, text="📋", font=("Arial", 24), bg="white")
icon_label.pack()

title_label = tk.Label(header_frame, text="User Entry Form", font=("Arial", 18, "bold"), bg="white")
title_label.pack()

# Form fields
form_frame = tk.Frame(root, bg="white")
form_frame.pack(pady=10)

# Name field
tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, sticky="w")
entry_name = tk.Entry(form_frame, width=30, font=("Arial", 12))
entry_name.grid(row=0, column=1, pady=5)

# Email field
tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, sticky="w")
entry_email = tk.Entry(form_frame, width=30, font=("Arial", 12))
entry_email.grid(row=1, column=1, pady=5)

# Phone field
tk.Label(form_frame, text="Phone:", font=("Arial", 12), bg="white").grid(row=2, column=0, pady=5, sticky="w")
entry_phone = tk.Entry(form_frame, width=30, font=("Arial", 12))
entry_phone.grid(row=2, column=1, pady=5)

# Address field
tk.Label(form_frame, text="Address:", font=("Arial", 12), bg="white").grid(row=3, column=0, pady=5, sticky="w")
entry_address = tk.Entry(form_frame, width=30, font=("Arial", 12))
entry_address.grid(row=3, column=1, pady=5)

# Gender field (Radio buttons)
tk.Label(form_frame, text="Gender:", font=("Arial", 12), bg="white").grid(row=4, column=0, pady=5, sticky="w")
gender_var = tk.StringVar()
tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", bg="white", font=("Arial", 12)).grid(row=4, column=1, sticky="w")
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", bg="white", font=("Arial", 12)).grid(row=5, column=1, sticky="w")

# Submit button
submit_button = tk.Button(
    root, text="Submit", font=("Arial", 12, "bold"), bg="black", fg="white", relief="flat", command=submit_data
)
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
client = MongoClient("mongodb://localhost:27017/")
db = client["user_data"]  # Database
collection = db["user_entries"]  # Collection
