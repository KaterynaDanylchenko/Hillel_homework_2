# Напишіть гру "Камінь ножиці папір". Схема роботи така:
# користувачу виводиться повідомлення зі списком фігур.
# користувач обриає якусь фігуру, програма випадковим чином обирає свою.
# визначається переможець
from Homework_8_functions import figure_choice,figure_game
figure_choice()
user_massage=input('>>>>>')
figure_game(user_massage)
