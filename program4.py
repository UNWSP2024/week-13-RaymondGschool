import sqlite3

def connect() -> sqlite3.Connection:
    return sqlite3.connect('phone_book.db')

def display() -> None:
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('select * from Contacts')
    rows = cursor.fetchall()
    print(f"{'ID':<5} {'Name':<20} {'Phone Number':<15} {'Email':<25}")
    print("=" * 65)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<25}")
    connection.close()

def update() -> None:
    display()
    contact_id = input("Enter the ID of the contact to update: ")
    name = input("Enter the new name (or press Enter to keep current): ")
    phone = input("Enter the new phone number (or press Enter to keep current): ")
    email = input("Enter the new email (or press Enter to keep current): ")
    
    connection = connect()
    cursor = connection.cursor()

    if name:
        cursor.execute('update Contacts set name = ? where id = ?', (name, contact_id))
    if phone:
        cursor.execute('update Contacts set phone_number = ? where id = ?', (phone, contact_id))
    if email:
        cursor.execute('update Contacts set email = ? where id = ?', (email, contact_id))

    connection.commit()
    connection.close()

def delete() -> None:
    display()
    contact_id = input("Enter the ID of the contact to delete: ")

    connection = connect()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Contacts WHERE id = ?', (contact_id,))
    connection.commit()
    connection.close()
    print("Contact deleted successfully.")

def main_menu() -> None:
    while True:
        print("\nPhone Book Menu:")
        print("1. Display all contacts")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display()
        elif choice == '2':
            update()
        elif choice == '3':
            delete()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()