numbers = [2, 3, 6, 8, 20, 91, 4, 0, 74, 3, 3, 5]
for num in numbers:
    if num %2 == 0:
        continue
    print(num)

print('\n')

etc = [1,2,3,4,5,56]
for i in range(len(etc)):
    etc[i] += 1
print(etc)

print('\n')

greetings = 'Hello, World'
indexes = []
count = 0
for i in range(len(greetings)):
    if greetings[i] == 'o':
        count += 1
        indexes.append(i)
print(count)
print(indexes)