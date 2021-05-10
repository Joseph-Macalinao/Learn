def car_game():
    print("Welcome to the car game.")
    decide = True
    while decide == True:
        decision = str(input("What would you like to do: \n1. Start car \n2. Stop car \n3. Quit \n"))
        if decision.lower() == '1':
            print('The car is now started!')
        elif decision.lower() == '2':
            print('The car is now stopped')
        elif decision.lower() == '3':
            decide = False
        else:
            print('Input not accepted: please enter a 1, 2, or 3')
    print('Thanks for playing')
car_game()