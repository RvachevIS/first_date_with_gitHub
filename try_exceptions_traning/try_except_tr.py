def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    try:
        print(find_average(numbers=[1,2,3]))
    except ZeroDivisionError:
        print("The list is empty")
    print('We are here')