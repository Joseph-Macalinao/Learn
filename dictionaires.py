'''
Name: John Smith
Email: john@gmail.com
Phone: 123456

Each item has a key(name, email, phone) and values attached to those keys
'''
customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
#both below are ways to get a value from a key in a dictionary
print(customer['name'])
print(customer.get('name'))

#updating keys
customer['name'] = 'Jack Smith'
print(customer['name'])

#adding new keys and values
customer['birthdate'] = 'Jan 1 1980'
print(customer['birthdate'])

#translate numbers into their words


numbers = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
'8': 'eight', '9': 'nine', '0': 'zero'}
phone = input("What is your number:\n")
for numb in phone:
    print(numbers.get(numb))

