from random import randint
import timeit


def get_random_number():
    """
    Returns:
        (int)
    """
    number = randint(1, 101)
    return number


def get_number_from_user():
    """
    Returns:
        (int)
    """
    while True:
        try:
            return int(input(f'Enter int, but remember that you have 3 attempts: '))
        except:
            print('It\'s not int')
        else:
            print("You don't have available attempts")


def check_numbers(to_guess, user_number):
    """

    Args:
        to_guess (int):
        user_number (int):

    Returns:
        (bool):
    """
    print(f'--->  {to_guess}')

    substruction = abs(user_number - to_guess)

    if substruction in range(1, 5):
        print('Its warm')
        return False
    elif substruction in range(5, 11):
        print('Its hot')
        return False
    elif substruction > 10:
        print('Its so cold')
        return False
    elif to_guess == user_number:
        return True


def game():
    """This function takes user and computer values and compares them. Allows the user to make three attempts to
    enter """
    a = get_random_number()
    for i in range(1, 4):
        b = get_number_from_user()
        if check_numbers(a, b) is True:
            print('You WIN!!!!')
            break


game()


def time_func():
    """This function measures the running time in seconds of the game"""
    game_time = timeit.timeit()
    return game_time


#
def decorator(func):
    """This decorator contains a message about the game time in seconds"""

    def user_notification():
        print(f'Часи виконання гри {func()} секунд')

    return user_notification


d = decorator(time_func)
d()
