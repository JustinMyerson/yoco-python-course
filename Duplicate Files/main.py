from importlib.resources import path
import os
import os.path
import hashlib
from tkinter.filedialog import askdirectory
from tkinter import Tk

hash_list = []

Tk().withdraw()
directory = askdirectory(title="Directory")


def rm(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file = os.path.join(root, file_name)
            current_file_hash = hashlib.md5(
                open(file, "rb").read()).hexdigest()  # rb opens the binary file in read format
            if current_file_hash in hash_list:
                os.remove(file)
                print(f"Duplicate {file} has been removed")
            else:
                hash_list.append(current_file_hash)


if __name__ == "__main__":
    rm(directory)
