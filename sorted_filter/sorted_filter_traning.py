fruits = ['banana', 'apple', 'cherry', 'date']
sorted_fruits = sorted(fruits, reverse=True)


def sort_by_len(element: str) -> int:
    return len(element)


sorted_fruits = sorted(fruits, key=sort_by_len)

if __name__ == '__main__':
    print(sorted_fruits)