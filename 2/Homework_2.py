# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#
#
#
# Попросіть користувача ввести свій вік (можно використати константу або функцію input()).
#
# - якщо користувачу менше 7 - вивести "Де твої батьки?"
#
# - якщо користувачу менше 16 - вивести "Це фільм для дорослих!"
#
# - якщо користувачу більше 65 - вивести "Покажіть пенсійне посвідчення!"
#
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "Який цікавий вік!"
#
# - у будь-якому іншому випадку - вивести "А білетів вже немає!"

user_name = 'Katya'
user_age = 99
result= "I'm {} years old".format(user_age)
print(result)
# print(user_age)
if user_age<7:
    print('Де твої батьки?')
if user_age<16:
    print('Це фільм для дорослих!')
if user_age > 65:
        print('Покажіть пенсійне посвідчення!')

if user_age in (11,22,33,44,55,66,77,88,99):
        print('Який цікавий вік!')
else:
    print('А білетів вже немає')

