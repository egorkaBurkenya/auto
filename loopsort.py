from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time 

with open('folders.json') as json_file:
    folders = json.load(json_file)


class MyHandler(FileSystemEventHandler):
  def on_modified(self, event):
    for filename in os.listdir(folders["folder_to_track"]):
      src = folders["folder_to_track"] + "/" + filename
      try:
        new_folder = folders[filename.split('.')[-1]]
      except KeyError:
        new_folder = folders["default"]
      new_destination = new_folder + "/" + filename
      os.rename(src, new_destination)
      
event_handler = MyHandler()
observer = Observer()

observer.schedule(event_handler, folders["folder_to_track"], recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()
observer.join()

