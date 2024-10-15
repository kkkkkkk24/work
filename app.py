import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# MongoDB connection setup
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["user_data"]  # Database name
    collection = db["users"]  # Collection name
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

# Function to handle form submission
def submit_data():
    name = entry_name.get()
    email = entry_email.get()

    if not name or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    data = {"name": name, "email": email}
    try:
        collection.insert_one(data)
        messagebox.showinfo("Success", f"Data for {name} saved!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Form")
root.geometry("400x300")
root.config(bg="white")

# Form header (title and subtitle)
header_frame = tk.Frame(root, bg="white")
header_frame.pack(pady=10)

icon_label = tk.Label(header_frame, text="📄", font=("Arial", 24), bg="white")
icon_label.pack()

title_label = tk.Label(header_frame, text="FORM TITLE", font=("Arial", 18, "bold"), bg="white")
title_label.pack()

subtitle_label = tk.Label(header_frame, text="Subtitle or text", font=("Arial", 12), bg="white")
subtitle_label.pack()

# Form fields
form_frame = tk.Frame(root, bg="white")
form_frame.pack(pady=20)

entry_name = tk.Entry(form_frame, width=30, font=("Arial", 12), fg="gray", relief="solid", bd=1)
entry_name.insert(0, "Your name")
entry_name.grid(row=0, column=0, pady=10)

entry_email = tk.Entry(form_frame, width=30, font=("Arial", 12), fg="gray", relief="solid", bd=1)
entry_email.insert(0, "Your e-mail")
entry_email.grid(row=1, column=0, pady=10)

# Submit button
submit_button = tk.Button(
    root, text="SEND FORM", font=("Arial", 12, "bold"), bg="black", fg="white", relief="flat", command=submit_data
)
submit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
client = MongoClient("mongodb://localhost:27017/")
db = client["user_data"]
collection = db["users"]
