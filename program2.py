import sqlite3

def display_city_data() -> None:
    connection = sqlite3.connect('cities.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Cities')
    rows = cursor.fetchall()

    print(f"ID\t\tName     \t\tCountry      \t\tPopulation")
    print("=" * 80)
    for row in rows:
        print(f"{row[0]}\t\t{row[1]}   \t\t{row[2]}      \t\t{row[3]}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    display_city_data()
