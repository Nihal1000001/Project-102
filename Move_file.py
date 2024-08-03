import os
import shutil

from_dir="C:\Users\lenovo\Desktop\Python\Project 102"
to_dir="C:\Users\lenovo\Desktop\Document_Files"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)

if extension == '':
    continue
if extension in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/' + "image_files"
    path3 = to_dir + '/' + "image_files" + '/' + file_name

path1 = from_dir + "/" + "Document_Files"
path2 = to_dir + "/" + "Document_Files"
path3 = to_dir + "/Document_Files" + '/' + file_name

if os.path.exists(path2):
    print("Moving" + file_name + ".....")

    shutil.move(path1,path2)
else:
    os.makedirs(path2)
    print("Moving" + file_name + ".....")
    shutil.move(path1,path3)

