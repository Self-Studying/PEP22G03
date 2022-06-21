# !/usr/bin/env python
import shutil
import os
from termcolor import colored

fpath = "/home/phoenix/LICENTA"
cwd = os.getcwd()
cpath = "/home/phoenix/PEP22G03/Modul3/cube.py"
print(os.listdir(cwd))
spath = "/home/phoenix/PEP22G03/Modul3"
rpath = os.path.relpath(fpath, spath)
path = "/home/phoenix/LICENTA/"  # path to the directory

"""for (root, directory, file) in os.walk(path):  # os.walk will return 3 elements ,root, directory and the files
        print(root)
        print(directory)
        print(file)
        print("[+++++++++++++++++++++++++++++++++]")"""
for (root, directory, files) in os.walk("/home/phoenix/python/rep.py"):
    for file in files:
        new_path = os.path.join(root, directory)
        print("The path of the file is : ", new_path)
        print(dir(os.walk("/home/phoenix")))
        filestatus = os.stat(path)
        filesize = filestatus.st_size
        print("The path of the file is :", new_path, "\t", filesize, "bites.")
dpath = "/tmp"
shutil.move(spath, dpath, )
print(colored("Your file has been successfully moved!", 'cyan'))
path_to_archive = "/home/phoenix/Documents"

if len(path_to_archive) == 0:
    path_to_archive = os.getcwd()
else:
    if not os.path.isdir(path_to_archive):
        print("You have chosen the wrong path!")
    else:
        os.chdir(path_to_archive)

lp = os.path.join(path_to_archive, "log")
os.mkdir(lp)

mp = os.path.join(lp, "metadata.txt")

fd = os.open(mp, os.O_APPEND | os.O_CREAT | os.O_RDWR)
n = int(input("Enter the size of the file needs to be zipped:"))
n = n * 1024

print("\n\t\*****\t*****\n")
print("List of te fils and directories zipped: ")

for roots, dirs, files in os.walk("/home/phoenix/python/"):
    for f in files:
        print(os.new_path.join(roots, f))

print("\n\t\*****\t*****\n")
print("\nFiles that are being moved to log directory: ")
print("\nFile name\t\tSize")

for roots, dirs, files in os.walk("/home/phoenix/python"):
    for f in files:
        if roots != lp:
            fil = os.path.join(roots, f)
            filestatus = os.stat(fil)
            fs = filestatus.st_size
            if fs > n:
                print(fil, ":", fs / 1024, "kb")
            relativepath = str.encode(os.path.relpath(fil, new_path) + "\n")
            os.write(fd(relativepath))
            shutil.move(fil, lp)

os.close()
shutil.make_archive("logbackup", "zip", lp)

shutil.rmtree(lp)

print("\n\t*****\t*****\n")

print("List of files and directories after zipping: ")
for roots, dirs, files in os.walk("/home/phoenix/python"):
    for f in files:
        print(os.path.join(roots, f))
