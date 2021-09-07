print('--------------------------------------------5-User Input & While Loops--------------------------------------------')
message = input("Tell me something, and I will repeat is back to you😀: ")
print(message)

homework_status = input('Did you finish your homework: ')

if homework_status == 'yes' or homework_status == 'Yes':
    print('Good! You are now free to play games.')
elif homework_status == 'no' or homework_status =='No':
    print('Please finish your homework.')
else:
    print('Please respond with "yes" on "no".')
    
height = input("How old are you?: ")
height = int(height)

if height >= 40:
    print("You are tall enough to ride")
else:
    print('Your will be able to ride when your are a little taller.')

number = input('Enter a number, and I will tell you if it is even or odd: ')
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd")

number_to_count_to = input('What number do you want me to count to?: ')
number_to_count_to = int(number_to_count_to)

current_number = 1
while current_number <= number_to_count_to:
    print(current_number)
    current_number += 1
    
prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

message = ''
while message != 'quit':
    message = input(prompt)
    print(message)