import csv

rows = [['name', 'age', 'occupation'],
        ['Ivan', 31, 'QA Engineer'],
        ['Mary', 25, 'Nail Master']]
file = open("files/persons.csv", "w")
csv_writer = csv.writer(file)
csv_writer.writerows(rows)

file.close()