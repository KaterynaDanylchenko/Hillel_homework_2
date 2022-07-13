# 1. Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
#
# 2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

# 3. Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.


#Task №1

word= input('Введіть слово')
num= input('Введіть число')
word_split=word.split()
word_without_extra_character=''.join(word_split)
num_split=num.split()
num_without_extra_character=''.join(num_split)
int_num=int(num_without_extra_character)
word_count_number=len(word_without_extra_character)
conversation_false="Введіть число від -{} до {}".format(word_count_number,word_count_number)
if int_num<=word_count_number:
    print("The {} symbol in {} is {}".format(num,word_without_extra_character,word_without_extra_character[int_num]))
else:
    print(conversation_false)

#Task №2

str=input('Введіть строку')
result= len(str.split())
print(result)

#Task №3

lst_input= [1,2.3,'Katya']
lst_output=[ ]
for i in lst_input:
    if type(i)==int or type(i)==float:
        lst_output.append(i)
        print(lst_output)


