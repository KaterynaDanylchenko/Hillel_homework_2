import random
def figure_choice_by_user():
    """This function prints the massage with the list of figures to choose from"""
    print('Оберіть фігуру з перелічених: камінь,ножиці,папір та введіть нижче')
    a=input('>>>>>')



def computer_choice():
    computer_choice = random.choice(['камінь', 'ножиці', 'папір'])
    print(computer_choice)


def figure_game(figure_choice_by_user,computer_choice):
    """This function compares the figure recieved from you with the figure that the computer randomly choose"""
    if figure_choice_by_user==computer_choice:
        print('Нічия')
    elif figure_choice_by_user=='камінь' and computer_choice=='папір':
        print('Ви програли')
    elif figure_choice_by_user=='камінь' and computer_choice=='ножиці':
        print('Ви вийграли')
    elif figure_choice_by_user=='ножиці' and computer_choice=='папір':
        print('Ви вийграли')
    elif figure_choice_by_user=='ножиці' and computer_choice=='камінь':
        print('Ви програли')
    elif figure_choice_by_user=='папір' and computer_choice=='ножиці':
        print('Ви програли')
    elif figure_choice_by_user=='папір' and computer_choice=='камінь':
        print('Ви програли')


figure_choice_by_user=figure_choice_by_user()
computer_choice=computer_choice()
figure_game(figure_choice_by_user,computer_choice)