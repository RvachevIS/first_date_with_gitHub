def sort_by_len(element: str) -> int:
    return len(element)


sort_by_len_lambda = lambda element: len(element)


fruits = ['avocado', 'strawberry', 'mango']
sorted_fruits = sorted(fruits, key=lambda element: len(element))
longest_word = max(fruits, key=lambda element: len(element))



if __name__ == '__main__':
    print(sort_by_len("avocado"))
    print(sort_by_len_lambda("peach"))
    print(sorted_fruits)
    print(longest_word)