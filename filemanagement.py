import os

def create_file():
    name = input("Enter file name: ")

    if os.path.exists(name):
        print("File already exists.")
    else:
        with open(name, "w") as f:
            f.write("")
        print("File created successfully.")

def write_file():
    name = input("Enter file name: ")

    if os.path.isfile(name):
        content = input("Enter content: ")

        with open(name, "a") as f:
            f.write(content + "\n")

        print("Content added successfully.")
    else:
        print("File not found.")

def read_file():
    name = input("Enter file name: ")

    if os.path.isfile(name):
        with open(name, "r") as f:
            print(f.read())
    else:
        print("File not found.")

def rename_file():
    old = input("Enter old file name: ")
    new = input("Enter new file name: ")

    if os.path.isfile(old):
        if not os.path.exists(new):
            os.rename(old, new)
            print("File renamed successfully.")
        else:
            print("New file name already exists.")
    else:
        print("File not found.")

def delete_file():
    name = input("Enter file name: ")

    if os.path.isfile(name):
        confirm = input("Confirm delete (yes/no): ")

        if confirm.lower() == "yes":
            os.remove(name)
            print("File deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("File not found.")

def list_files():
    files = [
        x for x in os.listdir(".")
        if os.path.isfile(x)
    ]

    if files:
        for file in files:
            print(file)
    else:
        print("No files found.")

while True:
    print("\nFILE MANAGEMENT SYSTEM")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Rename File")
    print("5. Delete File")
    print("6. List Files")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()
    elif choice == "2":
        write_file()
    elif choice == "3":
        read_file()
    elif choice == "4":
        rename_file()
    elif choice == "5":
        delete_file()
    elif choice == "6":
        list_files()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")