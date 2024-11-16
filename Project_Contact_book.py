class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        found_contacts = [
            contact for contact in self.contacts
            if query.lower() in contact.name.lower() or query in contact.phone
        ]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        try:
            contact = self.contacts[index - 1]
            contact.name = name if name else contact.name
            contact.phone = phone if phone else contact.phone
            contact.email = email if email else contact.email
            contact.address = address if address else contact.address
            print("Contact updated successfully.")
        except IndexError:
            print("Invalid contact index.")

    def delete_contact(self, index):
        try:
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        except IndexError:
            print("Invalid contact index.")

    def menu(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Quit")

            choice = input("Choose an option: ")
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == "4":
                self.view_contacts()
                try:
                    index = int(input("Enter the contact number to update: "))
                    print("Leave a field blank to keep it unchanged.")
                    name = input("Enter new name: ") or None
                    phone = input("Enter new phone number: ") or None
                    email = input("Enter new email: ") or None
                    address = input("Enter new address: ") or None
                    self.update_contact(index, name, phone, email, address)
                except ValueError:
                    print("Invalid input.")
            elif choice == "5":
                self.view_contacts()
                try:
                    index = int(input("Enter the contact number to delete: "))
                    self.delete_contact(index)
                except ValueError:
                    print("Invalid input.")
            elif choice == "6":
                print("Exiting Contact Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()