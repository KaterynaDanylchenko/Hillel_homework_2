"критерієм перевірки буде проходження всіх ассертів"

##############################################################################
############                                                     #############
############                      TASK 1                         #############
############                                                     #############
##############################################################################


"""
написати декоратор wrap_validate, який не приймає жодних параметрів
його задача - перевірити, що функція, яку він задекорував, обовязково отримала
в своїх аргументах параметр 'password' (згадуємо про * в написанні аргументів функції)
значення 'password' повинне бути стрічкою, довжиною не менше 10 символів,
та містити в собі латинські літери (регістр не принципово), арабські цифри та знак '!"

кожну з перевірок отриманого значення паролю виконуємо в ОКРЕМІЙ функції, функції робимо
універсальними, називаємо їх (з опційними параметрами)
- is_valid_length(length=10)
- has_any_symbols(symbols='qwertyuiopasdfghjklzxcvbnm') (це приклад для латинських букв, повертає тру, якщо хоч
один символ в стрічці, аналогічно зробити для цифр та знаку оклику (у вас буде 3 виклики функції в середині декоратора
з різними параметрами)
- is_string()

якщо  'password'  відсутній - викликаємо помилку
raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

якщо  'password'  не задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': False,
}

якщо  'password'  задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': True,
}

зауважте, що str(func(*args, **kwargs)) МАЄ бути довжиною не більше 100 символів
якщо даний результат буде довшим за 100 символів, то стрічка має бути обрізана до 100 символів, причому останні
три символи мають бути ... (трьома крапками)
тут ви вже й самы здогадалися написати функцію на виконання даної роботи (тут вже без підказок)
"""


def is_string(input_data):
    if type(input_data) == str:
        return True
    return False


def has_any_symbols(symbols='', password=''):
    return any([symb in str(password.lower()) for symb in symbols.lower()])


def is_valid_length(length=10, string=''):
    if len(str(string)) >= length:
        return True
    return False


def get_result_msg(info):
    if len(info) > 100:
        info = info[:97] + "..."
    return info


def wrap_validate(func):
    def inner(*args, **kwargs):
        if 'password' not in kwargs and len(args) < 4:
            raise AttributeError(f'no parameter "password" in arguments of function {func.__name__}')
        if kwargs.get('password', None) is not None:
            password = kwargs['password']
        else:
            password = args[3]
        is_password_valid = False
        if is_string(password):
            if is_valid_length(length=10, string=password):
                if (has_any_symbols(symbols='qwertyuiopasdfghjklzxcvbnm', password=password) and
                        has_any_symbols(symbols='1234567890', password=password) and
                        has_any_symbols(symbols='!', password=password)):
                    is_password_valid = True
        return {'result': get_result_msg(str(func(*args, **kwargs))),
                'is_secure': is_password_valid}

    return inner


##############################################################################
############                                                     #############
############                      TASK 2                         #############
############                                                     #############
##############################################################################
"""
написати функцію registration, яка приймає
- позиційний аргумент id, стрічка або число - не важливо,  значення за замовчуванням - відсутнє
- позиційний або іменований аргумент login, тип даних - не важливий, значення за замовчуванням - відсутнє
- позиційний або іменований аргумент notes, тип даних - не важливий, значення за замовчуванням - відсутнє
- password - тип даних - не важливий, значення за замовчуванням - відсутнє

в середині функції вставити код (зназок для отримання даних прописаний нижче)
date = datetime.date.today()

результат робити функції - стрічка
f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

задекоруйте написаним в завданні 1 декоратором
"""
import datetime


@wrap_validate
def registration(id: str or int, login, notes, password):
    date = datetime.date.today()
    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'


##############################################################################
############                                                     #############
############                      TASK 3                         #############
############                                                     #############
##############################################################################
"""
створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)
в цій умові створіть assert на всі створені функції (окрім декоратора), викликайте функції з різними параметрами 
(довжина слів, різні текстовки....)
на кожну функцію, що використовується в декораторі, має бути мінімум 3 ассерта,

функцію registration перевіряйте з огляду на роботу декоратора (ключі, значення). обовязково перевірте кількість ключів, 
тип даних в значеннях, назви ключів, значення отриманого результату в залежності від переданих даних   

ВАЖЛИВО 
функцію registration ассертимо ТІЛЬКИ при передачі їй валідних даних (поля паролю)
"""

if __name__ == '__main__':
    print("-" * 50)
    print('Start tests:')

    print('Test is_string func ...')
    assert is_string(input_data='password') == True
    assert is_string(input_data='') == True
    assert is_string(input_data=1234) == False
    assert is_string(input_data={'password': 'secretpswd'}) == False

    print('Test has_any_symbols func ...')
    assert has_any_symbols(symbols='abc', password='aklf2bdah!fasc1') == True
    assert has_any_symbols(symbols='ABC', password='aklf2bdah!fasc1') == True
    assert has_any_symbols(symbols='Abc', password='sometext') == False
    assert has_any_symbols(symbols='109', password='aklf2bdah!fasc1') == True
    assert has_any_symbols(symbols='109', password='aklf2bdah!fasc3') == False
    assert has_any_symbols(symbols='!', password='aklf2bdah!fasc3') == True
    assert has_any_symbols(symbols='!', password='aklf2bdah?fasc3') == False

    print('Test is_valid_length func ...')
    assert is_valid_length(length=10, string='aklf2bdah?fasc3') == True
    assert is_valid_length(length=10, string='aklf2bd') == False
    assert is_valid_length(length=0, string='aklf2bd') == True
    assert is_valid_length(length=0, string='') == True

    print('Test get_result_msg func ...')
    assert get_result_msg(
        info="створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)") == 'створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)'
    assert get_result_msg(
        info="створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте) в цій умові") == 'створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте) в цій...'
    assert len(get_result_msg(
        info="створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте) в цій умові")) == 100
    assert get_result_msg(info="") == ''

    print('Test registration func ...')
    date = datetime.date.today()
    assert list(registration(id=1, login='example@gmail.com', notes='some note', password='pswd12!pswd').keys()) == ['result', 'is_secure']
    assert len(registration(id=1, login='example@gmail.com', notes='some note', password='pswd12!pswd').keys()) == 2
    assert type(registration(id=1, login='example@gmail.com', notes='some note', password='pswd12!pswd')['result']) == str
    assert type(registration(id=1, login='example@gmail.com', notes='some note', password='pswd12!pswd')['is_secure']) == bool
    assert registration(id=1, login='example@gmail.com', notes='some note', password='pswd12!pswd')['is_secure'] == True
    assert registration(id=1, login='example@gmail.com', notes='some note', password='PSWD12!PSWD')['is_secure'] == True
    assert registration(id=1, login='example@gmail.com', notes='some note', password='pswd12pswd')['is_secure'] == False
    assert registration(id=1, login='example@gmail.com', notes='some note', password='pswd12!p')['is_secure'] == False
    assert registration(id=1, login='example@gmail.com', notes='some note', password='')['is_secure'] == False
    assert registration(id=1, login='example@gmail.com', notes='some note', password='somepassword123!?')['result'] == f'User example@gmail.com created account on {date} with password "somepassword123!?". Additiona...'
    assert registration(id=1, login='example@gmail.com', notes='some note', password='s12?')['result'] == f'User example@gmail.com created account on {date} with password "s12?". Additional information...'
    assert registration(id=1, login='ex@gm.com', notes='note', password='s12?')['result'] == f'User ex@gm.com created account on {date} with password "s12?". Additional information: note'
    assert registration(id=1, login='ex@gm.com', notes='note', password='s12?') == {'result': f'User ex@gm.com created account on {date} with password "s12?". Additional information: note', 'is_secure': False}
    assert registration(id=1, login='ex@gm.com', notes='note', password='pswd12!pswd') == {'result': f'User ex@gm.com created account on {date} with password "pswd12!pswd". Additional information:...', 'is_secure': True}

##############################################################################
############                                                     #############
############                      TASK 4                         #############
############                     HAVE FUN                        #############
############                                                     #############
##############################################################################
