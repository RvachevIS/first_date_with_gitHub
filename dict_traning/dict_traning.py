person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
person["job"] = "Engineer"

for key, value in person.items():
    print(key, ":", value)

p1 = {
    'city': 'Moscow',
    'age': 31,
    'name': 'Ivan'
}
p2 = {
    'job': 'QA Engineer',
    'married': True,
    'city': 'Vladimir'
}
#p1.update(p2)
#print(p1)
p1 = p1 | p2
print(p1)