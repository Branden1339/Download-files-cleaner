
File Management Utility:
This Python script provides a simple file management utility to help organize files in a specified directory. It allows users to move files, add files to folders, and delete files (sent to trash).

Features:
Move Files: Move files from a specified directory to another location.
Add Files to Folder: Create a folder (if it doesn't exist) and move files into it.
Delete Files: Send files to trash for deletion.

Usage:
Run the Script: Execute the Python script to start the file management utility.

python file_management.py
Choose an Option: Select an option from the menu:

A: Move files
B: Add files to a folder
C: Delete a file (sent to trash)
X: Exit the program
Follow the Prompts: Depending on the option chosen, follow the prompts to specify file criteria and destination locations.

Example:

def main():
    while True:
        print("------------------------------")
        print("A: Move files")
        print("B: Add files to folder")
        print("C: Delete a file (send to trash) ")
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

Contributing:
Contributions are welcome! If you have any suggestions or improvements for this project, feel free to fork the repository and submit a pull request.

