student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 21,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 22,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
student_2={
    'Katya Danylchenko': {
        'Пошта': 'ekaterynadanilchenko@ukr.net',
        'Вік': 30,
        'Номер телефону': '+380987771221',
        'Середній бал': 100
    },
}
student['Kateryna Danylchenko']= {'Пошта': 'ekaterynadanilchenko@ukr.net', 'Вік': 30, 'Номер телефону': '+380987771221','Середній бал': 100}
print(student)
student_lst=student.values()
# print(student_lst)
Student_list=student.keys()
# print(Student_list)
# if i in student ==
Value_list=[]
# for i.value in student:
#     if 'Номер телефону'==' ':
#     student['Номер телефону'] = {'0444869248'}
#     print(student)
for i in student_lst:
    додаток=Value_list.append(i.values())
# print(Value_list)
Середній_бал_кожного_студента=[]
for i in Value_list:
    seredniy_ball=list(i)[-1]
    # print(seredniy_ball)
    Середній_бал_кожного_студента.append(seredniy_ball)
# print(Середній_бал_кожного_студента)
Середній_бал_по_групі=sum(Середній_бал_кожного_студента)/len(Середній_бал_кожного_студента)
print('Cередній бал по групі>>>>>', Середній_бал_по_групі)
for stud in student:
    if student[stud]['Середній бал']>90:
        print(stud,student[stud]['Середній бал'])