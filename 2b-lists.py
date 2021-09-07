print('--------------------------------------------2b-Lists--------------------------------------------')

phones = ['apple', 'samsung', 'lg']
for phone in phones:
    print(f"My new phone is a {phone.title()}")
    print('\n')
    
NAME = 'Jathur'
BEST_FREIND = 'Bob'

names = [NAME, BEST_FREIND]
for name in names:
    if (name == names[1]):
        print(f"{name.title()} is my best freind")
        
name_1 = ['Jathur', 'Vijayakaran']
name_2 = ['John', 'Trump']
name_3 = ['Bill', 'Gates']

name_list = [name_1, name_2, name_3]
print(name_list)

for value in range(1, 26):
    print(value)
    
numbers = list(range(1, 9))
print(numbers)

even_numbers = list(range(4, 17, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    print(squares)

print(min(squares))
print(max(squares))
    
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
    print(cubes)
    
print(cubes[1:5])

dimenstions = (4, 8)
print(dimenstions)