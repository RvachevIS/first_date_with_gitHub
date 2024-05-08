def introduce(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

person = {
    "city": "New York",
    "age": 31,
    "name": "Ivan"
}
introduce(**person)