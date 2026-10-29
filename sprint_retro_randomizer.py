import tkinter as tk
from tkinter import ttk
import random

# generate a random choice
def generate_random_choice():
    value = random.choice(["What went well", "What did not go well", "What to improve"])  # list of options
    result.set(value)  # Update the result label
    results_list.insert(tk.END, value)  # Add the value to the listbox

# add manual input to the Listbox
def add_manual_input():
    manual_input = textbox.get()  # Get value from the textbox
    if manual_input:  # Ensure textbox is not empty
        combined_value = f"{result.get()} - {manual_input}"  # Combine random choice and manual input
        results_list.insert(tk.END, combined_value)  # Add combined value to the listbox
        textbox.delete(0, tk.END)  # Clear the textbox

#clear the history in the Listbox
def clear_history():
    results_list.delete(0, tk.END)  # Remove all entries from the Listbox

# Create main window
root = tk.Tk()
root.title("Sprint Retro Random")
root.geometry("400x400")


style = ttk.Style()
style.theme_use("clam")  

# Customize button styles
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("Custom.TButton", background="#4CAF50", foreground="white", borderwidth=1)
style.map("Custom.TButton", background=[("active", "#45A049")])  # Button color when hovered

#  hold the result
result = tk.StringVar()
result.set("Let's Go!")

# label for displaying the current result
result_label = ttk.Label(root, textvariable=result, font=("Arial", 14), anchor="center", padding=10)
result_label.pack(pady=10)

# button for generating random choices
button = ttk.Button(root, text="Feedback Button", command=generate_random_choice, style="Custom.TButton")
button.pack(pady=10)

# Listbox to display all results
results_frame = ttk.Frame(root)
results_frame.pack(pady=10, fill="x", expand=True)
results_label = ttk.Label(results_frame, text="History:", font=("Arial", 12))
results_label.pack(anchor="w")
results_list = tk.Listbox(results_frame, height=10, width=30, font=("Arial", 12))
results_list.pack(pady=5, fill="x")

# textbox for manual input beside the Listbox
textbox_frame = ttk.Frame(root)
textbox_frame.pack(pady=10, fill="x", expand=True)
textbox_label = ttk.Label(textbox_frame, text="Feedback Person - optional:", font=("Arial", 12))
textbox_label.pack(anchor="w")
textbox = tk.Entry(textbox_frame, font=("Arial", 12))
textbox.pack(anchor="w", fill="x", pady=5)

# Add a button to insert textbox input into the Listbox
textbox_button = ttk.Button(root, text="Feedback Person", command=add_manual_input, style="Custom.TButton")
textbox_button.pack(pady=5)

# Add a button to clear history
clear_button = ttk.Button(root, text="Clear History", command=clear_history, style="Custom.TButton")
clear_button.pack(pady=5)

# Run the main loop
root.mainloop()
