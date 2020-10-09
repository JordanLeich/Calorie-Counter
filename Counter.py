# Created by Jordan Leich on 10/8/2020

# TODO: Add more food items here with the correct calorie amounts please

# Imports
import colors
import restart

# Globals
pizza = 275
apple = 95
banana = 105
calories = 0
total_cals = 0
user_weight = 0


def counter():
    """Main calorie counter that loops based on the number of food items the user has ate"""
    global total_cals, calories
    user_items = int(input('How many different food items have you ate today? '))
    print()

    if user_items <= 0:
        print(colors.red + 'Error! Please enter a valid number!\n', colors.reset)
        counter()

    else:
        i = 0
        while i < user_items:
            food_item = str(input('Enter the name of an item you ate today or type help for a list of valid food '
                                  'names: '))
            print()

            if food_item.lower() == 'help':
                print(colors.yellow + '''pizza = 275 calories
apple = 95 calories
banana = 105 calories\n''', colors.reset)
                counter()

            food_quantity = int(input('Quantity of this item ate: '))
            print()

            i += 1

            if food_item.lower() == 'pizza':
                calories = pizza * food_quantity
                total_cals = total_cals + calories
                print(colors.green + 'Calories total: ' + str(total_cals), '\n', colors.reset)

            elif food_item.lower() == 'apple':
                calories = apple * food_quantity
                total_cals = total_cals + calories
                print(colors.green + 'Calories total: ' + str(total_cals), '\n', colors.reset)

            elif food_item.lower() == 'banana':
                calories = banana * food_quantity
                total_cals = total_cals + calories
                print(colors.green + 'Calories total: ' + str(total_cals), '\n', colors.reset)

            else:
                print(colors.red + 'Invalid food name provided!\n', colors.reset)
                counter()

        print(colors.green + 'Your final calorie total is: ', str(total_cals), '\n', colors.reset)
        restart.restart()


def user_weights():
    """Used to display the avg and recommended amounts of calories to the user"""
    print(colors.green + 'The average and healthy amount of calories for a person is about 2100 calories per day.\n',
          colors.reset)

    if '124' >= str(user_weight) >= '1':
        print('Your recommended amount of calories to consume per day is 1,600 or less calories.\n')
        counter()
    elif str(user_weight) >= '125' or str(user_weight) <= '200':
        print('Your recommended amount of calories to consume per day is 2700 or less calories.\n')
        counter()
    elif str(user_weight) >= '300':
        print('Your recommended amount of calories to consume per day is 3764 or less calories.\n')
        counter()

    else:
        print(colors.red + 'User weight error found! Restarting...\n' + colors.reset)
        restart.restart()


def start():
    """Beginning of the program"""
    user_weight = int(input('How much do you weigh in pounds? '))
    print()

    if user_weight <= 0:
        print(colors.red + 'Error! Please enter a valid weight!\n', colors.reset)
        restart.restart()

    elif user_weight >= 400:
        print(colors.red + 'Sorry! This weight amount is too high to record right now!\n', colors.reset)
        restart.restart()

    else:
        user_weights()


"""starts the beginning of the program"""
start()
