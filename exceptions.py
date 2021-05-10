#what to do with code so that a single error won't crash program
#try: and except: are what you need to use
'''
try:
    code block here

except ErrorType:
    return/result
'''

#example
try:
    age = int(input('Age:'))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age must be > 0')
except ValueError: #if input type isn't an int, it will do this
    print('Invalid Value')
