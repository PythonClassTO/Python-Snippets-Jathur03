print('--------------------------------------------2a-Lists--------------------------------------------')

bicycles = ['trek', 'connodale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])

# This prints the last item on the list
print(bicycles[-1]) 

message = f"My first bicycle was a {bicycles[3].title()}"
print(message)

names = ['jathur', 'bob', 'robert', 'john']
new_name = input('What is your name? ')

names.append(new_name)
print(names)

bicycles[0] = 'ducati'
print(bicycles)

bicycles.append('yamaha')
print(bicycles)

bicycles = []
bicycles.append('ducati')
bicycles.append('yamaha')
bicycles.append('suzuki')
print(bicycles)

bicycles.insert(0, 'honda')
print(bicycles)

# Removing Itmes
del bicycles[0]
print(bicycles)

popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

first_owned = bicycles.pop(0)
print(f"My first was {first_owned}")

bicycles.remove('yamaha')
print(bicycles)


# Sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print('\ncars')
cars.sort(reverse = True)
print(cars)

print(cars)
print(sorted(cars))
print(cars)

cars.reverse()
print(cars)

print(len(cars))