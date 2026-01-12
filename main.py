from pathlib import Path
import shutil
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def CreateFolder():
    try:
        name = input("Enter the name of the folder: ")
        p = Path(name)
        os.mkdir(p)
        print("Folder created")
    except:
        print("Folder already exists")


def ReadFolder():
    try:
        p = Path()
        items = list(p.rglob("*"))
        for i, v in enumerate(items):
            print(f"{i+1} : {v}")
    except:
        print("File does not exist")


def updateFolder():
    try:
        ReadFolder()
        old_name = input("Enter the name of the file: ")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("Enter the new name of the file: ")
            p.rename(new_name)
            print("File name updated")
        else:
            print("File does not exist")
    except:
        print("File does not exist")


def createFile():
    try:
        ReadFolder()
        name = input("Enter the name of the file: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter the data: ")
                fs.write(data)
            print("File created")
        else:
            print("File already exists")

    except:
        print("File already exists")


def readFile():
    try:
        ReadFolder()
        name = input("Enter the name of the file: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
        else:
            print("File does not exist")
    except:
        print("File does not exist")


def deletFolder():
    try:
        ReadFolder()
        name = input("Enter the name of the folder you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("Folder deleted")
        else:
            print("Folder does not exist")

    except Exception as err:
        print(f"Folder does not {err}")


def updateFile():
    try:
        ReadFolder()
        old_name = input("Enter the name of the file: ")
        p = Path(old_name)
        if p.exists() and p.is_file():
            print(
                f"1. Update the name of the file\n2. Update the data of the file\n3. Overwrite the data of the file"
            )
            option = int(input("Enter the option: "))
            if option == 1:
                new_name = input("Enter the name of the file: ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("File name updated")
                else:
                    print("File already exists")
            elif option == 2:
                with open(p, "a") as fs:
                    data = input("Enter the data: ")
                    fs.write(" " + data)
                print("File updated")
            elif option == 3:
                with open(p, "w") as fs:
                    data = input("Enter the data: ")
                    fs.write(data)
                print("File updated")
            else:
                print("Invalid option")
        else:
            print("File does not exist")
    except:
        print("File does not exist")

def deletFile():
    try:
        ReadFolder()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted")
        else:
            print("File does not exist")
    except:
        print("File does not exist")

while True:
    clear_screen()
    print("""
====================================
🗂️  FILE & FOLDER MANAGEMENT SYSTEM
====================================

1. Create Folder
2. View Files & Folders
3. Rename Folder
4. Delete Folder
5. Create File
6. Read File
7. Update File
8. Exit

====================================
    """)

    choice = input("👉 Enter your choice: ")

    clear_screen()

    if choice == "1":
        CreateFolder()
    elif choice == "2":
        ReadFolder()
    elif choice == "3":
        updateFolder()
    elif choice == "4":
        deletFolder()
    elif choice == "5":
        createFile()
    elif choice == "6":
        readFile()
    elif choice == "7":
        updateFile()
    elif choice == "8":
        print("👋 Exiting... Thank you!")
        break
    else:
        print("❌ Invalid choice")

    input("\n🔁 Press Enter to continue...")