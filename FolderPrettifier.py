# Oh Soldier Prettify my Folder
# make a function which takes a path of a folder as string input and then will 
# path = C:/Users/Kabeer Mirza/Desktop/Exercise
# file = Capitalize all files with lowercase first letter
# png/jpg = rename all files as 1.png, 2.png, 3.png

import os
# filename = input("Enter the file name you want to leave as default")
# newfilename = filename.capitalize()


# def contencap(yourfile):
#     with open(yourfile) as f:
#         for text in yourfile:
#             text.capitalize()

def soldier(folder_path, filename, fileformat):
    neww = filename.capitalize()
    default = filename
    os.chdir(folder_path)
    list = os.listdir()
    name = 1
    for f in list:
        new = f.split(".")[1]
        if new == 'txt':
            os.rename(f"{folder_path}/{f}", f"{folder_path}/{f.capitalize()}")
            os.rename(f"{folder_path}/{neww}", f"{folder_path}/{default}")
            
        elif new == fileformat:
                os.rename(f"{folder_path}/{f}", f"{folder_path}/ {name}.{fileformat}")
                name = name + 1

folder_path = input("Enter the path to your folder\n")
filename = input("Enter the filename you want to leave as default\n")
fileformat = input("Enter the fileformat you want to rename from 1 to so on..\n")
soldier(folder_path, filename, fileformat)
# os.chdir("C:/Users/Kabeer Mirza/Desktop/Exercise/")  
# contencap("saboor.txt")