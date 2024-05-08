def add_all(*args):
    summary = 0
    for i in args:
        summary += i
    return summary


values = [23, 6, 3]
other_values = [1, 4, 191]


if __name__ == '__main__':
#    print(add_all(1, 2, 3))
    print(add_all(*values, *other_values))