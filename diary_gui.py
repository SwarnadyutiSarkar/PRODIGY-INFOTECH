import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import os

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diary App")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Frame for entry
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(padx=10, pady=10)

        self.entry_label = tk.Label(self.entry_frame, text="Write your diary entry:")
        self.entry_label.pack()

        self.entry_text = tk.Text(self.entry_frame, height=10, width=50)
        self.entry_text.pack()

        self.save_button = tk.Button(self.entry_frame, text="Save Entry", command=self.save_entry)
        self.save_button.pack(pady=5)

        # Frame for reading entries
        self.read_frame = tk.Frame(self.root)
        self.read_frame.pack(padx=10, pady=10)

        self.date_label = tk.Label(self.read_frame, text="Enter the date (YYYY-MM-DD) to read entries:")
        self.date_label.pack()

        self.date_entry = tk.Entry(self.read_frame)
        self.date_entry.pack(pady=5)

        self.read_button = tk.Button(self.read_frame, text="Read Entries", command=self.read_entries)
        self.read_button.pack(pady=5)

        # Text area for displaying entries
        self.display_text = tk.Text(self.root, height=15, width=80)
        self.display_text.pack(padx=10, pady=10)

    def save_entry(self):
        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Get the diary entry from the user
        entry = self.entry_text.get("1.0", tk.END).strip()

        if not entry:
            messagebox.showwarning("Warning", "Diary entry cannot be empty.")
            return

        # Create a filename with the current date
        filename = now.strftime("%Y-%m-%d") + ".txt"

        # Write the entry to the file
        with open(filename, 'a') as file:
            file.write(f"Date and Time: {timestamp}\n")
            file.write(f"{entry}\n")
            file.write("-" * 40 + "\n")

        self.entry_text.delete("1.0", tk.END)  # Clear the entry text box
        messagebox.showinfo("Info", "Your entry has been saved.")

    def read_entries(self):
        date = self.date_entry.get().strip()
        if not date:
            messagebox.showwarning("Warning", "Date cannot be empty.")
            return

        filename = date + ".txt"

        if not os.path.isfile(filename):
            messagebox.showwarning("Warning", f"No entries found for {date}.")
            return

        with open(filename, 'r') as file:
            contents = file.read()

        self.display_text.delete("1.0", tk.END)  # Clear the display text box
        self.display_text.insert(tk.END, contents)

def main():
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
