print('--------------------------------------------6a-Functions--------------------------------------------')
print("Hello how is your day?")

def greet_user():
    """Display a simple greeting."""
    print("Hello")
    
greet_user()

def greet_user(username):
    """Display a sinmple greeting with the perameter 'username'."""
    print(f"Hello {username}")
    
username = input("What is your username? ")
greet_user(username)

def sum(a, b):
    """Sum of 2 values. The 2 values come from the parameters"""
    a = int(a)
    b = int(b)
    
    total = a + b
    print(f"The total is {total}")
    
value_a = input("What is the first value you want to add? ")
value_b = input("What is the second value you want to add? ")

sum(value_a, value_b)

def describe_pet(animal_type, pet_name):
    """Display information about your pet"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('Dog', 'Tim')

def order(item, price):
    """Displays information about your order"""
    print(f"Your {item} is {price}")
    
order("Pen", "$10.99")

describe_pet(pet_name="John", animal_type="Cat")

def describe_pet(pet_name, animal_type="dog"):
    """Display information about your pet"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
describe_pet('Harry')

def get_formatted_name(first_name, last_name):
    """Return a formatted fullname"""
    full_name = f"{first_name.title()} {last_name.title()}"
    
    return full_name

musician = get_formatted_name('jimi', 'hendriz')
print(musician)

def product(a, b):
    """Multiplies 2 values"""
    value = a * b
    
    return value

answer = product(4, 9)
print(answer)

def build_person(first_name, last_name):
    """Returns a dictionary of information about a person"""
    person = {
        'first': first_name,
        'last': last_name
    }
    
    return person

musician = build_person('jimi', 'hendrix')

print(musician.get('first'))
print(musician['last'])

purchased_items = []

number_of_items = input("How many items would you like to add to the list?: ")
number_of_items = int(number_of_items)

def purchase_list(name_of_item):
    """Adds items to the purchased items list"""
    purchased_items.append(name_of_item.lower())
        
    print(f"{name_of_item.title()} has been added to the list of purchesed items.")

number = 0
while number < number_of_items:
    item = input("What item would you like to add to the list?: ")
    
    number = number + 1
    purchase_list(item)
    
print(purchased_items)