from importlib.resources import path
import os

directory = "/Users/justin/Documents/Python/yoco-python-course/Duplicate Files"
file_list = os.listdir(directory)
print(file_list)

for file in file_list:
    # Assuming duplicate files follow the format text.txt, text(1).txt
    if "(1)" not in file:
        continue
    original_file_name = file.replace("(1)", "")
    if not os.path.exists(os.path.join(directory, original_file_name)):
        continue
    os.remove(os.path.join(directory, file))
