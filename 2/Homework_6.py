

# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.

def function(arg_1):
    result=float(arg_1)
    print(result)
    return result
function(10)

#
# Напишіть функцію, що приймає два аргументи. Функція повинна:
# а) якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# b) якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# c) якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# d) у будь-якому іншому випадку повернути кортеж з цих аргументів



def function_final(arg_1,arg_2):
   if type(arg_1)==str and type(arg_2)==str:
       res_str=arg_1+' '+arg_2
       print(res_str)
   elif type(arg_1) == str and type(arg_2) != str:
       res_dict={arg_1:arg_2}
       print(res_dict)
   elif type(arg_1)==int or type(arg_1)==float:
       if type(arg_2)==int or type(arg_2)==float:
           res=arg_1*arg_2
           print(res)
       else:
           tuple_from_elements = (arg_1, arg_2)
           print(tuple_from_elements)
   else:
       tuple_from_elements=(arg_1,arg_2)
       print(tuple_from_elements)
       return(res_str)

function_final(10,'10')

