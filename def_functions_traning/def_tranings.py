numbers_1 = [1,2,3,4,5]
numbers_2 = [4,5,6,3,7]


def find_average(nums):
    average = sum(nums) / len(nums)
    return average


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)


def count_vowels(string):
    VOWELS = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1

    return count


def nothing():
    pass


#функция заглушка
nothing()


def format_date(*, day: int, month: str) -> str:
    return f'The date is {day} of {month}'


if __name__ == '__main__':
    print(average_1)
    print(average_2)

    print(count_vowels('Hello, World'))
    print(format_date(month='October', day='1'))