# Script to print every file inside of a folder
import os # Import the os module to interact with file system
# Ask user for input, folder path to process
folder_name = input("Enter folder path: ")
# List all files in the specified folder
print("Files found:")
for root, dirs, files in os.walk(folder_name):
    for file in files:
        print(os.path.join(root, file))
