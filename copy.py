#! bin/python

import os, glob, shutil

NEW_FOLDER = "."

folder_list = os.listdir(".")

for folder in folder_list:
    move_list = glob.glob(os.path.join(folder, "**"))
    for item in move_list:
        shutil.copy(item, NEW_FOLDER)