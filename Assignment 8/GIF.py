import os
import imageio

File_List = sorted(os.listdir("images"))

IMAGES = []

for FileName in File_List:
    File_Path = "images/" + FileName
    image = imageio.imread(File_Path)
    IMAGES.append(image)

imageio.mimsave("images/GIF.gif", IMAGES)