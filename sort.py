import os
import json
import time 

from custom import use_custom

with open('folders.json') as json_file:
    folders = json.load(json_file)

for filename in os.listdir(folders["meTerminal"]):
      src = folders["meTerminal"] + "/" + filename
      if use_custom(src):
        print("pass")
      else:
        try:
          new_folder = folders[filename.split('.')[-1]]
        except KeyError:
          new_folder = folders["default"]
        new_destination = new_folder + "/" + filename
        os.rename(src, new_destination)