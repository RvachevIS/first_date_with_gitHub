import csv


persons = [
        {"name": "Olga", "age": 64, "occupation": "Mother"}
]

file = open("files/persons.csv", "a")
fields = ["name", "age", "occupation"]
csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
csv_dict_writer.writerows(persons)

file.close()