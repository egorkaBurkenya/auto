import os
import json
import time 

with open('folders.json') as json_file:
    folders = json.load(json_file)

for filename in os.listdir(folders["folder_to_track"]):
      src = folders["folder_to_track"] + "/" + filename
      try:
        new_folder = folders[filename.split('.')[-1]]
      except KeyError:
        new_folder = folders["default"]
      new_destination = new_folder + "/" + filename
      os.rename(src, new_destination)