people = [
    {"name": "Alice", "age": 25},
    {"name": "Peter", "age": 23},
    {"name": "Sergey", "age": 23},
    {"name": "Vanya", "age": 31}
]


def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element["age"], element["name"]


sorted_people = sorted(people, key=sort_by_age_name)

if __name__ == '__main__':
    print(sorted_people)