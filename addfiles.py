
import os

# For captilalizing content in your text file:
def contencap(yourfile):
    with open(yourfile) as f:
        for text in yourfile:
            text.capitalize()

# For prettifying your specified folder:
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
            os.rename(f"{folder_path}/{f}",
                      f"{folder_path}/ {name}.{fileformat}")
            name = name + 1

# For adding a Note in every folder starting with 'K':
def addnote(path, Note):
    cwd = os.chdir(path)
    ls = os.listdir(cwd)
    t = 0
    for subdir in ls:

        if subdir[0] == 'k' and os.path.isdir(f"{path}{r'/'}{subdir}"):
            os.chdir(f"{path}{r'/'}{subdir}")
            with open("Note.txt", "a") as w:
                w.write(Note)
            t =+ 1

        elif subdir[0] == 'K' and os.path.isdir(f"{path}{r'/'}{subdir}"):
            os.chdir(f"{path}{r'/'}{subdir}")
            with open("Note.txt", "a") as w:
                w.write(Note)
            t += 1

        elif subdir[0] == 'k' or subdir[0] == 'K' and os.path.isfile(f"{path}{r'/'}{subdir}"):
            pass
    print(f"Executed Successfully on {t} folders. ")

# For removing all the files that were created by the previous function.
def remnote(path, name):
    cwd = os.chdir(path)
    ls = os.listdir(cwd)
    t = 0
    for subdir in ls:

        if subdir[0] == 'k' and os.path.isdir(f"{path}{r'/'}{subdir}"):
            os.chdir(f"{path}{r'/'}{subdir}")
            pat = (f"{path}{r'/'}{subdir}")
            os.remove(f"{pat}{r'/'}{name}")

        elif subdir[0] == 'K' and os.path.isdir(f"{path}{r'/'}{subdir}"):
            os.chdir(f"{path}{r'/'}{subdir}")
            pat = (f"{path}{r'/'}{subdir}")
            os.remove(f"{pat}{r'/'}{name}")   

        elif subdir[0] == 'k' or subdir[0] == 'K' and os.path.isfile(f"{path}{r'/'}{subdir}"):
            pass


if __name__ == '__main__':
    while True:
        ans = int(input(
            "This program performs two services:\n1. Prettify your folder 2. Creates a directory in every folder\n[1] Prettify\n[2] Create Directory\n"))
        if ans == 1:
            folder_path = input("Enter the path to your folder\n")
            filename = input("Enter the filename you want to leave as default\n")
            fileformat = input(
                "Enter the fileformat you want to rename from 1 to so on..\n")
            soldier(folder_path, filename, fileformat)

        elif ans == 2:
            Note = "You can change this note to whatever you want!"
            path = input("Enter the Path")
            addnote(path, Note)
        
        last =  str(input("Do you want to remove all the Note.txt files that were created before??\nNo\nYes\n")).lower()

        if last == "no":
            break
        elif last == "yes":
            remnote(path, "Note.txt")
            break
        else:
            print("Please type 'yes' or 'no' in the given field.")
            break
        







