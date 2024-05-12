import json

data = {"name": "Ivan", "age": 31, "city": "Vladimir"}
file = open("files/data.json", "w")
json.dump(data, file, indent=4)

file.close()