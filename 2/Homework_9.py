from random import randint


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
    max_attempts = 3
    available_attempts = 0
    if available_attempts <= max_attempts:
        available_attempts+1
        print(available_attempts)
        while True:
            try:
                return int(input(f'Enter int, but remember that you have {max_attempts} attempts: '))
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
        print('return True')
        return True


def game():
    number_to_guess = get_random_number()

    while True:
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            break

    print('You WIN!!!!')


game()
