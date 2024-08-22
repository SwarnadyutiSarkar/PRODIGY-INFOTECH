import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        self.contacts_file = 'contacts.json'
        self.contacts = self.load_contacts()

        # Create and place the widgets
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Phone Number:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="View Contacts", command=self.view_contacts).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(root, text="Edit Contact", command=self.edit_contact).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).grid(row=4, column=1, padx=10, pady=10)
    
    def load_contacts(self):
        if os.path.exists(self.contacts_file):
            with open(self.contacts_file, 'r') as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open(self.contacts_file, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        if not name or not phone or not email:
            messagebox.showwarning("Input Error", "All fields are required.")
            return
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts available.")
            return
        contacts_str = "\n".join([f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}" 
                                  for name, info in self.contacts.items()])
        messagebox.showinfo("Contacts", contacts_str)

    def edit_contact(self):
        name = simpledialog.askstring("Edit Contact", "Enter the name of the contact to edit:")
        if name not in self.contacts:
            messagebox.showwarning("Not Found", "Contact not found.")
            return
        phone = simpledialog.askstring("Edit Contact", "Enter new phone number:")
        email = simpledialog.askstring("Edit Contact", "Enter new email address:")
        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        self.save_contacts()
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
