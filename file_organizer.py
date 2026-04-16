import os
import shutil

path = input("Enter folder path: ")

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)

    if extension:
        folder = extension[1:].upper() + "_files"
        folder_path = os.path.join(path, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files organized successfully!")
