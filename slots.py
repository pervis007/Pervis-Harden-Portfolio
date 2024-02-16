import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime
from pyqt5 import *

# Create the main application window
window = tk.Tk()
window.title("Planner")

# Function to save a document
def save_document():
    document_text = document_textbox.get("1.0", tk.END)
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        try:
            with open(filename, 'w') as file:
                file.write(document_text)
            messagebox.showinfo("Success", "Document saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the document:\n{str(e)}")

# Function to create a reminder
def create_reminder():
    reminder_text = reminder_textbox.get()
    reminder_time = reminder_time_entry.get()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if reminder_time < current_time:
        messagebox.showwarning("Warning", "The reminder time cannot be in the past!")
        return
    messagebox.showinfo("Reminder Created", f"A reminder has been set for {reminder_time}:\n{reminder_text}")

# Create the notebook tabs
notebook = tk.ttk.Notebook(window)

# Planning Tab
planning_frame = tk.Frame(notebook)
notebook.add(planning_frame, text="Planning")

# Note-taking Tab
notes_frame = tk.Frame(notebook)
notebook.add(notes_frame, text="Notes")

# Calendar Tab
calendar_frame = tk.Frame(notebook)
notebook.add(calendar_frame, text="Calendar")

# Add the notebook to the window
notebook.pack()

# Document Saving Section
document_label = tk.Label(planning_frame, text="Document:")
document_label.pack()

document_textbox = tk.Text(planning_frame, height=10, width=50)
document_textbox.pack()

save_document_button = tk.Button(planning_frame, text="Save Document", command=save_document)
save_document_button.pack()

# Reminder Section
reminder_label = tk.Label(planning_frame, text="Reminder:")
reminder_label.pack()

reminder_textbox = tk.Entry(planning_frame, width=50)
reminder_textbox.pack()

reminder_time_label = tk.Label(planning_frame, text="Reminder Time (HH:MM:SS):")
reminder_time_label.pack()

reminder_time_entry = tk.Entry(planning_frame, width=20)
reminder_time_entry.pack()

create_reminder_button = tk.Button(planning_frame, text="Create Reminder", command=create_reminder)
create_reminder_button.pack()

window.mainloop()