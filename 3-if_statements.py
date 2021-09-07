print('--------------------------------------------3-If Statements--------------------------------------------')

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print('This is not a bmw')
        
car = 'Audi'
print(car.lower() == 'audi')

requested_topping = 'mushrooms'
if requested_topping != 'anchovie':
    print("Hold the anchovies!")

answer = input('What do you thing is the answer? ')

answer = int(answer)

if answer != 28:
    print('Your answer is wrong 🔴 ')
else:
    print('Your answer is correct 🟢 ')

banned_users = ['Robbert', 'Jonh']

user = input('What is your username? ')
if user not in banned_users:
    print(f"You can post a message if you want.")
else:
    print('You are a banned user you may not post a message.')
    
number_1 = 6
number_2 = 2

if number_1 == number_2 and number_2 == number_1:
    print('Both numbers are equal')
else: 
    print('The numbers are not equal')
    
game_active = True
can_edit = False

print(game_active and can_edit)

age_a = 44
age_b = 33

print(age_a >= 40 or age_b >= 40)

age = 20

if age < 30:
    print('low')
elif age == 20:
    print('equal')
elif age > 10:
    print('greater')
else:
    print('I dont know')