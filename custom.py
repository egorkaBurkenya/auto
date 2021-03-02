import os 
import json

with open('custom.json') as json_file:
  custom = json.load(json_file)

def get_customs_names():
  return list(custom.keys())

def get_custom_tags(custom):
  return list(custom.keys())

def use_custom(filename: str) -> bool:
  cutoms = get_customs_names()
  for i in cutoms:
    if i in filename:
      filename_name = filename.replace(i, '')
      cutom_tegs = get_custom_tags(custom[i])
      print(cutom_tegs)
      if 'move' in cutom_tegs:
        new_path = custom[i]['move'] + '/' + filename_name.split('/')[-1]
        os.rename(filename, new_path)
      return True
  return False