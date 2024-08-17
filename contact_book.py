import tkinter as tk
from tkinter import messagebox, simpledialog

# Main application class
class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.frame, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(self.frame, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone:
            self.contacts[phone] = {"name": name, "email": email, "address": address}
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields!")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
            return

        contact_list = "\n".join([f"{v['name']} - {k}" for k, v in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if not search_term:
            return

        found_contacts = [f"{v['name']} - {k}" for k, v in self.contacts.items() if search_term in v['name'] or search_term in k]

        if found_contacts:
            messagebox.showinfo("Search Results", "\n".join(found_contacts))
        else:
            messagebox.showinfo("No Results", "No contacts found.")

    def update_contact(self):
        phone = simpledialog.askstring("Update", "Enter the phone number of the contact to update:")
        if not phone or phone not in self.contacts:
            messagebox.showwarning("Warning", "Contact not found.")
            return

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name:
            self.contacts[phone]['name'] = name
        if email:
            self.contacts[phone]['email'] = email
        if address:
            self.contacts[phone]['address'] = address

        messagebox.showinfo("Success", "Contact updated successfully!")
        self.clear_entries()

    def delete_contact(self):
        phone = simpledialog.askstring("Delete", "Enter the phone number of the contact to delete:")
        if not phone or phone not in self.contacts:
            messagebox.showwarning("Warning", "Contact not found.")
            return

        del self.contacts[phone]
        messagebox.showinfo("Success", "Contact deleted successfully!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
