new_list = [0, 1, 2, 3, 4, 5]

reverse_list = new_list[::-1]
print(reverse_list)

new_list.reverse()
print(new_list)

new_reverse_list = list(reversed(new_list))
print(type(new_reverse_list))
print(new_reverse_list)