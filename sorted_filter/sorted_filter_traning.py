def is_even(n: int) -> bool:
    return n % 2 == 0


numbers = [1, 2, 8, 3, 56, 7, 31, 228]

filtered_numbers = list(filter(is_even, numbers))

if __name__ == '__main__':
    print(type(filtered_numbers))
    print(filtered_numbers)