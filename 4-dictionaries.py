print('--------------------------------------------4-Dictionaries--------------------------------------------')
alien_0 = {'color': 'green', 'points': 5, 'map': 'ocean'}

print(alien_0['color'].title())
print(alien_0['points'])

print(f"Alien is the color {alien_0['color']} with the points of {alien_0['points']}")

alien_0['points'] = alien_0['points'] + 5
print(alien_0['points'])

alien_0['x_position'] = 65
alien_0['y_position'] = 0

print(alien_0['x_position'])
print(alien_0['y_position'])

print(alien_0)

student_list = {}

student_list[1] = 'Jathur'
student_list[2] = 'Sajan'
student_list[3] = 'Jayita'
student_list[4] = 'Jenitha'

print(student_list)

fav_lanugages = {
    'jathur': 'javascript',
    'bob': 'python',
    'robert': 'html'
}

print(f"Bobs favourite programming language is {fav_lanugages['bob']}")

del alien_0['map']
print(alien_0)

alien_1 = {
    'color': 'green',
    'speed': 'slow',
}

print_value = alien_1.get('points', 'No poiunt value assigned')
print(print_value)
 
user_0 = {
    'username': 'KingJathur',
    'first_name': 'Jathur',
    'last_name': 'Vijayakaran'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")
    
for key, value in user_0.items():
    print(f"\nKey: {key}, Value: {value}")
    
friends_age = {
    'bob': 12,
    'tim': 10,
    'kim': 15
}

for age in friends_age.items():
    print(age)

alien_1 = { 'color': 'green', 'speed': 'slow', 'points': 12}
alien_2 = {'color': 'green', 'points': 5}
alien_3 = {'color': 'red', 'points': 10}
alien_4 = {'color': 'yellow', 'points': 15}

aliens = [alien_0, alien_1, alien_2, alien_3, alien_4]

for alien in aliens:
    print(alien)

sum = 0
for alien in aliens:
    print(alien['points'])
    sum = sum + alien['points']
    
print(f"Sum is {sum}")

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein'
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie'
    }
}

print(users['aeinstein'])
print(users['aeinstein']['first'])