import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = 'contacts.json'

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, 'r') as f:
                self.contacts = json.load(f)

    def save_contacts(self):
        with open(CONTACTS_FILE, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({
            'name': name.strip(),
            'phone': phone.strip(),
            'email': email.strip(),
            'address': address.strip()
        })
        self.save_contacts()

    def get_all_contacts(self):
        return self.contacts

    def search_contacts(self, keyword):
        keyword = keyword.lower()
        return [c for c in self.contacts if keyword in c['name'].lower() or keyword in c['phone']]

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
        self.save_contacts()

    def update_contact(self, old_name, new_contact):
        for i, c in enumerate(self.contacts):
            if c['name'] == old_name:
                self.contacts[i] = new_contact
                break
        self.save_contacts()

class ContactApp:
    def __init__(self, root):
        self.book = ContactBook()
        self.root = root
        self.root.title(" Contact Book")
        self.root.geometry("500x500")
        
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Name").pack()
        tk.Entry(self.root, textvariable=self.name_var).pack()

        tk.Label(self.root, text="Phone").pack()
        tk.Entry(self.root, textvariable=self.phone_var).pack()

        tk.Label(self.root, text="Email").pack()
        tk.Entry(self.root, textvariable=self.email_var).pack()

        tk.Label(self.root, text="Address").pack()
        tk.Entry(self.root, textvariable=self.address_var).pack()

        tk.Button(self.root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).pack(pady=5)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).pack(pady=5)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).pack(pady=5)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        self.book.add_contact(name, phone, email, address)
        messagebox.showinfo("Success", "Contact added!")
        self.clear_fields()

    def view_contacts(self):
        contacts = self.book.get_all_contacts()
        if not contacts:
            messagebox.showinfo("Contacts", "No contacts found.")
            return

        info = ""
        for c in contacts:
            info += f"{c['name']} - {c['phone']}\n"

        messagebox.showinfo("All Contacts", info)

    def search_contact(self):
        keyword = simpledialog.askstring("Search", "Enter name or phone:")
        if not keyword:
            return
        results = self.book.search_contacts(keyword)
        if not results:
            messagebox.showinfo("Search", "No matching contact found.")
            return

        info = ""
        for c in results:
            info += f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n\n"
        messagebox.showinfo("Search Results", info)

    def update_contact(self):
        old_name = simpledialog.askstring("Update", "Enter name to update:")
        if not old_name:
            return

        matches = self.book.search_contacts(old_name)
        if not matches:
            messagebox.showerror("Error", "No such contact.")
            return

        c = matches[0]
        name = simpledialog.askstring("New Name", "Name:", initialvalue=c['name'])
        phone = simpledialog.askstring("New Phone", "Phone:", initialvalue=c['phone'])
        email = simpledialog.askstring("New Email", "Email:", initialvalue=c['email'])
        address = simpledialog.askstring("New Address", "Address:", initialvalue=c['address'])

        updated = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }

        self.book.update_contact(c['name'], updated)
        messagebox.showinfo("Updated", "Contact updated!")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter name to delete:")
        if not name:
            return

        matches = self.book.search_contacts(name)
        if not matches:
            messagebox.showinfo("Delete", "No matching contact found.")
            return

        confirm = messagebox.askyesno("Confirm", f"Delete contact: {matches[0]['name']}?")
        if confirm:
            self.book.delete_contact(matches[0]['name'])
            messagebox.showinfo("Deleted", "Contact deleted!")

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()