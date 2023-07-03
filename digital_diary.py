import os
import getpass
import datetime

# Function to add a new diary entry
def add_entry():
    # Get input from the user
    entry = input("Enter your diary entry: ")
    tags = input("Enter tags (comma-separated): ")
    
    # Get current date and time
    now = datetime.datetime.now()
    
    # Create a formatted timestamp
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Append the entry to the diary file
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp}\n{entry}\nTags: {tags}\n\n")
    
    print("Diary entry added successfully.")

# Function to view all diary entries
def view_entries():
    # Check if the diary file exists
    if not os.path.exists("diary.txt"):
        print("No entries found.")
        return
    
    # Read and print the contents of the diary file
    with open("diary.txt", "r") as file:
        entries = file.read()
    
    print(entries)

# Function to search for entries based on tags
def search_entries():
    # Get input from the user
    search_tags = input("Enter tags to search for: ")
    
    # Read the contents of the diary file
    with open("diary.txt", "r") as file:
        entries = file.readlines()
    
    # Search for matching entries
    matching_entries = []
    for i in range(0, len(entries), 4):
        tags = entries[i+2].strip()[6:]
        if search_tags in tags:
            matching_entries.append(entries[i:i+4])
    
    # Print the matching entries
    if matching_entries:
        print("Matching entries found:")
        for entry in matching_entries:
            print("".join(entry))
    else:
        print("No matching entries found.")

# Function to set a reminder
def set_reminder():
    # Get input from the user
    reminder_text = input("Enter reminder text: ")
    reminder_date = input("Enter reminder date (YYYY-MM-DD): ")
    reminder_time = input("Enter reminder time (HH:MM): ")
    
    # Convert the reminder date and time to datetime objects
    reminder_datetime = datetime.datetime.strptime(f"{reminder_date} {reminder_time}", "%Y-%m-%d %H:%M")
    current_datetime = datetime.datetime.now()
    
    # Calculate the time difference in seconds
    time_difference = (reminder_datetime - current_datetime).total_seconds()
    
    # Set the reminder
    if time_difference > 0:
        print("Reminder set successfully.")
        time.sleep(time_difference)
        print("Reminder:", reminder_text)
    else:
        print("Invalid reminder date/time.")

# Function to export the diary
def export_diary():
    # Get input from the user
    export_file = input("Enter the export file name: ")
    
    # Copy the diary file to the export file
    shutil.copyfile("diary.txt", export_file)
    
    print("Diary exported successfully.")

# Function to protect the diary with a password
def protect_diary():
    # Get input from the user
    password = getpass.getpass("Enter a password to protect your diary: ")
    confirm_password = getpass.getpass("Confirm password: ")
    
    # Check if passwords match
    if password == confirm_password:
        # Write the password to a file
        with open("password.txt", "w") as file:
            file.write(password)
        
        print("Diary protected with a password.")
    else:
        print("Passwords do not match.")

# Main program loop
while True:
    print("\n--- Digital Diary ---")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Set Reminder")
    print("5. Export Diary")
    print("6. Protect Diary")
    print("7. Quit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        set_reminder()
    elif choice == "5":
        export_diary()
    elif choice == "6":
        protect_diary()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
