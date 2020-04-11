# -*- coding: utf8 -*-

# Практическое задание
# 1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_func(*my_args):
    for tmp in my_args:
        print(100 / tmp)


user_a_str = input('Введите число: a, исключая 0\n')
user_b_str = input('Введите число: b, исключая 0\n')
if user_a_str.isnumeric() and user_b_str.isnumeric() and int(user_b_str) is not 0:
    my_func(int(user_a_str), int(user_b_str))
else:
    print(f'Введённые данные не верны')


# 2 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def printUserInfo(**my_kwargs):
    for key, values_str in my_kwargs.items():
        print(f'{key}-{values_str}', end=', ')


printUserInfo(first_name='Вася',
              last_name='Пупкин',
              birthday_year='1991',
              city='Москва',
              email='neudachnik@gmail.com',
              phone='+7(123)456-7890',
              )


# 3 Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(*my_args):
    my_args_list = list(my_args)
    max_elem = my_args_list.pop(my_args_list.index(max(my_args_list)))
    next_max_elem = my_args_list.pop(my_args_list.index(max(my_args_list)))

    return max_elem + next_max_elem


print(my_func(78, 30, 78))

# 4 Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
x = input('Введите действительное положительное число\n')
y = input('Введите целое отрицательное число\n')

if not (x.isnumeric() and y[0] == '-' and y[1].isnumeric() and int(y) < 0):
    print('Введены неверные данные\n')
    exit(-1)

x_int = int(x)
y_int = int(y)


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    abs_y = abs(y) - 1
    tmp = x
    while abs_y:
        abs_y -= 1
        tmp *= x
    return 1 / (tmp)


print(my_func_1(x_int, y_int))
print(my_func_2(x_int, y_int))


# 5 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def func_init_list(user_str):
    user_list_str = user_str.split()  # NO-BREAK SPACE + SPACE
    user_list = []
    for tmp in user_list_str:
        if tmp.isnumeric():
            user_list.append(int(tmp))
    return user_list


def check_special(user_str):
    if user_str[-1] == 'X':
        return True
    else:
        return False


while True:
    big_sum = 0
    user_list_str = input('Введите список через пробел цифр, если выйти наберите в конце X счёт будет с выходом\n')
    for tmp in func_init_list(user_list_str):
        big_sum += int(tmp)
    print(f'Получившаяся сумма: {big_sum}')

    if check_special(user_list_str):
        break


# 6 Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_funct(user_str):
    return ''.join([user_str[0].upper(), user_str[1:]])


user_str = input('Введите строку с текстом\n')
user_str_list = user_str.split()
for word in user_str_list:
    print(f'{int_funct(word)}', end=' ')
