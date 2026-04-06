import json, os

FILE = "contacts.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add(contacts, name, phone, email):
    if not name.strip():
        print("Error: Name cannot be empty!")
        return
    contacts.append({"name": name.strip(), "phone": phone.strip(), "email": email.strip()})
    save(contacts)
    print(f"✅ Contact '{name}' added successfully!")

def search(contacts, name):
    results = [c for c in contacts if name.lower() in c["name"].lower()]
    if not results:
        print(f"No contacts found matching '{name}'.")
    else:
        print(f"Found {len(results)} contact(s) matching '{name}':")
        for c in results:
            print(f"  - Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    return results

def delete(contacts, name):
    original_len = len(contacts)
    contacts[:] = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(contacts) < original_len:
        save(contacts)
        print(f"✅ Deleted contact(s) matching '{name}'.")
    else:
        print(f"No contacts found to delete matching '{name}'.")

def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts yet. Add some!")
    else:
        print(f"📖 Your Contacts ({len(contacts)} total):")
        for i, c in enumerate(contacts, 1):
            print(f"{i}. Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

contacts = load()
print("👋 Welcome to your Contact Book!")

while True:
    print("\n" + "="*30)
    print("📋 Menu:")
    print("1. ➕ Add Contact")
    print("2. 👀 View All Contacts")
    print("3. 🔍 Search Contact")
    print("4. 🗑️  Delete Contact")
    print("5. 🚪 Quit")
    print("="*30)
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        add(contacts, name, phone, email)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        name = input("Enter name to search: ").strip()
        if name:
            search(contacts, name)
        else:
            print("Please enter a name to search.")
    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name:
            confirm = input(f"Are you sure you want to delete contacts matching '{name}'? (y/n): ").strip().lower()
            if confirm == "y":
                delete(contacts, name)
            else:
                print("Delete cancelled.")
        else:
            print("Please enter a name to delete.")
    elif choice == "5":
        print("👋 Goodbye! Your contacts are saved.")
        break
    else:
        print("❌ Invalid choice. Please select 1-5.")
