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


user_age='77777777777'
user_age_final = int(user_age)
chek_num=(user_age[0])
res=user_age.count(chek_num)
age_chek=len(user_age)
if user_age_final<0:
    print('  ')
elif user_age_final==0:
    print('   ')
elif user_age_final<=7:
    print('Де твої батьки?')
elif user_age_final <= 10:
    print('Це фільм для дорослих!')
# elif res<2:
#     print(' ')
elif res == age_chek:
    print('Який цікавий вік!')
elif user_age_final <= 16:
    print('Це фільм для дорослих!')
elif user_age_final > 65:
        print('Покажіть пенсійне посвідчення!')
else:
    print('А білетів вже немає')
result= "I'm {} years old".format(user_age)
if user_age_final>0:
    print(result)
else:
    print('  ')