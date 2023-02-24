# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:
# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png


import os

# files = os.listdir("clutteredFolder")
# for file in files:
#     print(file)

# os.rename("clutteredFolder/file.txt", "clutteredFolder/6.txt")

# for file in files:
#     if file.endswith(".png"):
#         print(file)

files = os.listdir("clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
        i = i + 1