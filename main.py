import os
import shutil
import send2trash

download_dir = '/Users/brandenfrancis/Downloads'


# Move files
def move_file(location):
    files = os.listdir(download_dir)
    file_start = input("What does the file you want to move start with? ")
    file_end = input("And what does it end with? ")

    for file in files:
        if file.startswith(file_start) and file.endswith(file_end):
            file_path = download_dir + '/' + file
            shutil.move(file_path, location)
            print(f"Moving {file} ...")

    return 0


# Add file to a folder
def add_to_folder():
    files = os.listdir(download_dir)

    file_start = input("What does the file you want to move start with? ")
    file_end = input("And what does it end with? ")
    folder_name_location = input("Name and location of folder?(/Users/your username/Location/Name of Folder) ")

    for file in files:
        if file.startswith(file_start) and file.endswith(file_end):
            file_path = os.path.join(download_dir, file)
            if not os.path.exists(folder_name_location):
                os.makedirs(folder_name_location)
            shutil.move(file_path, os.path.join(folder_name_location, file))
            print(f"Moving {file} to folder ...")


# Delete a file
def delete_file():
    files = os.listdir(download_dir)

    file_start = input("What does the file you want to delete(send to trash) start with? ")
    file_end = input("And what does it end with? ")

    for file in files:
        if file.startswith(file_start) and file.endswith(file_end):
            file_path = os.path.join(download_dir, file)
            send2trash.send2trash(file_path)
            print(f"Sending {file} to trash... ")


def main():
    while True:
        print("------------------------------")
        print("A: Move files")
        print("B: Add files  to folder")
        print("C: Delete a file(send to trash) ")
        print("X: EXIT")
        print("------------------------------")

        option = input("Choose an option: ")
        if option == "X":
            break
        elif option == "A":
            location = input("Where would you like to move your file to?(/Users/yourname/location) ")
            move_file(location)
        elif option == "B":
            add_to_folder()
        elif option == "C":
            delete_file()


main()
