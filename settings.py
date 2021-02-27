import json

print("Settings 💻\n")

with open('folders.json') as json_file:
    folders = json.load(json_file)

for i in folders:
  print(f"{i} - {folders[i]}")

change_path_key = input("\nif u want to change some path write it`s name: ")
folders_keys = list(folders.keys())

if change_path_key in folders_keys:
  new_path = input(f"\nnew path for {change_path_key}: ")
  folders[change_path_key] = new_path
  with open('folders.json', 'w') as outfile:
    json.dump(folders, outfile)
else: 
  answer = input("\nu want to add new path ? Y/N ")
  if answer.lower() == "y":
    new_path = input(f"\nnew path for {change_path_key}: ")
    folders[change_path_key] = new_path
    with open('folders.json', 'w') as outfile:
      json.dump(folders, outfile)
  elif answer.lower == "n":
    pass
