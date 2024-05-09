people = [
    {"name": "Alice", "age": 18},
    {"name": "Peter", "age": 12},
    {"name": "Sergey", "age": 23},
    {"name": "Vanya", "age": 41},
    {"name": "Pisya", "age": 55},
    {"name": "Hui", "age": 80},
    {"name": "Vagia", "age": 13}
]


def is_adult(person: dict) -> bool:
    return person["age"] >= 18

filtered_people = list(filter(is_adult, people))


if __name__ == '__main__':
    print(filtered_people)