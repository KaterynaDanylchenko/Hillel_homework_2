import random
def figure_choice():
    """This function prints the massage with the list of figures to choose from"""
    user_massage = 'Оберіть фігуру з перелічених: камінь,ножиці,папір та введіть нижче'
    print(user_massage)



def figure_game(figure):
    """This function compares the figure recieved from you with the figure that the computer randomly choose"""
    variation_list = ['камінь', 'ножиці', 'папір']
    computer_choice = random.choice(variation_list)
    print('Computer_choice is'+ ' '+computer_choice)
    if figure==computer_choice:
        print ('Нічия')
    elif figure=='камінь' and computer_choice=='папір':
        print ('Ви програли')
    elif figure=='камінь' and computer_choice=='ножиці':
        print ('Ви вийграли')
    elif figure=='ножиці' and computer_choice=='папір':
        print ('Ви вийграли')
    elif figure=='ножиці' and computer_choice=='камінь':
        print ('Ви програли')
    elif figure=='папір' and computer_choice=='ножиці':
        print ('Ви програли')
    elif figure=='папір' and computer_choice=='камінь':
        print ('Ви програли')


