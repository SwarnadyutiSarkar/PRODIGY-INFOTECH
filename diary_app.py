import os
from datetime import datetime

# Function to display the menu
def display_menu():
    print("Diary App")
    print("1. Write a new entry")
    print("2. Read an entry")
    print("3. Exit")

# Function to write a new diary entry
def write_entry():
    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Get the diary entry from the user
    entry = input("Enter your diary entry: ")

    # Create a filename with the current date
    filename = now.strftime("%Y-%m-%d") + ".txt"

    # Write the entry to the file
    with open(filename, 'a') as file:
        file.write(f"Date and Time: {timestamp}\n")
        file.write(f"{entry}\n")
        file.write("-" * 40 + "\n")
    
    print("Your entry has been saved.")

# Function to read diary entries
def read_entries():
    # Get the date from the user
    date = input("Enter the date (YYYY-MM-DD) of the entries you want to read: ")
    filename = date + ".txt"

    if not os.path.isfile(filename):
        print(f"No entries found for {date}.")
        return

    # Read the entries from the file
    with open(filename, 'r') as file:
        contents = file.read()
        print("\n" + contents)

# Main function to run the diary app
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1, 2, 3): ")
        if choice == '1':
            write_entry()
        elif choice == '2':
            read_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
