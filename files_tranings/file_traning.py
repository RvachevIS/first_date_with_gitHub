import json

file = open("files/data.json", "r")
loaded_data = json.load(file)
file.close()
print(loaded_data)