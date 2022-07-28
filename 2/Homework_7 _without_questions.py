# Знову апишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свсвій вік.
#
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
#
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
#
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
#
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
#
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
#
#
#
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
#
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
#
# Наприклад :
#
# "Тобі ж 5 років! Де твої батьки?"
#
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
#
# "О, вам 33 роки! Який цікавий вік!"
#
#
#
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
#
# Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду.

def year_conjugation(arg_1):
    """ This function selects the required form of the word рік depending on the last digit in the quantity and the number of digits in the argument string."""
    age_dict = {'0': 'років', '1': 'рік', '2': 'роки', '3': 'роки', '4': 'роки', '5': 'років', '6': 'років',
                '7': 'років', '8': 'років', '9': 'років', '10': 'років', '11': 'років'}
    user_age = arg_1
    user_age_final = int(user_age)
    age_declension_for_1 = user_age[-1]
    for key in age_dict:
        if key == age_declension_for_1 and len(user_age) >= 4:
            result='років'
            return result
        else:
            if key == age_declension_for_1 and len(user_age) <= 4:
                res_alternative=age_dict.get(age_declension_for_1)
                return res_alternative



form_of_word_year=year_conjugation('21')

user_age='23'
user_age_final = int(user_age)
chek_num=(user_age[0])
res=user_age.count(chek_num)
age_chek=len(user_age)
if user_age_final<0:
    print('  ')
elif user_age_final==0:
    print('   ')
elif user_age_final<=7:
    print('Тобі ж {} {}! Де твої батьки?'.format(user_age,form_of_word_year))
elif user_age_final <= 10:
    print('Тобі лише {} {}, а це є фільм для дорослих!'.format(user_age, form_of_word_year))
elif res == age_chek:
    print('О, вам {} {}! Який цікавий вік!'.format(user_age,form_of_word_year))
elif user_age_final <= 16:
    print('Тобі лише {} {}, а це є фільм для дорослих!'.format(user_age,form_of_word_year))
elif user_age_final > 65:
        print('Вам {} {}? Покажіть пенсійне посвідчення!'.format(user_age,form_of_word_year))
else:
    print('Незважаючи на те, що вам {} {}, білетів всеодно нема!'.format(user_age,form_of_word_year))
