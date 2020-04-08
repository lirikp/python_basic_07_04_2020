# -*- coding: utf8 -*-

# Практическое задание
# 1.Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

var_int = 111
var_str_prompt_name = 'Сообщите своё имя, например: Миша'
print(f'{type(var_int)}:{var_int}')
print(f'{type(var_str_prompt_name)}:{var_str_prompt_name}')

var_str_prompt_sex = 'Сообщите свой пол, например: мужской'
var_int_prompt_age = 'Сообщите свой возраст в годах, например: 25'
var_int_prompt_waight = 'Сообщите свой вес в киллограммах, например: 120'
user_name = input(f'{var_str_prompt_name}\n')
user_sex = input(f'{var_str_prompt_sex}\n')
user_age = input(f'{var_int_prompt_age}\n')
user_waight = input(f'{var_int_prompt_waight}\n')

print(f'Вы сообщили что ваше имя: {user_name}, '
      f'ваш пол: {user_sex}, '
      f'ваш возраст: {user_age}, '
      f'и ваш вес: {user_waight}\n')

# 2.Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_seconds_str = input('Ведите количество секунд, например: 1123\n')
if time_seconds_str.isnumeric():
    time_seconds_int = int(time_seconds_str)
    hour = time_seconds_int // 3600
    hour_part = time_seconds_int % 3600
    minute = hour_part // 60
    second = hour_part % 60
    time_to_format_HH_MM_SS = 0
    print('{:02}:{:02}:{:02}'.format(hour, minute, second))
else:
    print('Введённое время не корректно!')

# 3.Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num_user_str = input('Ведите число, например: 2\n')
if num_user_str.isnumeric():
    num_pair = num_user_str + num_user_str
    num_trio = num_pair + num_user_str
    num_sum = int(num_user_str) + int(num_pair) + int(num_trio)
    print('Считаем {} + {} + {} = {}'.format(num_user_str, num_pair, num_trio, num_sum))
else:
    print('Введённое число не корректно!')

# 4.Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# num_user_str = 165734332
num_user_str = input('Ведите число, например: 12363\n')
if num_user_str.isnumeric() and int(num_user_str) > 0:
    num_user_int = int(num_user_str)
    more_num = 0
    while num_user_int > 0:
        num = num_user_int % 10
        num_user_int //= 10
        if num > more_num:
            more_num = num
else:
    print('Введённое число не корректно!')

# 5.Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue_str = input('Ведите число выручки, например: 100000\n')
profit_str = input('Ведите число прибыли, например: 500\n')

if revenue_str.isnumeric() and profit_str.isnumeric():
    revenue_int = int(revenue_str)  # Выручка
    profit_int = int(profit_str)  # Прибыль
    loss_int = revenue_int - profit_int  # Убыток

    if profit_int > revenue_int and loss_int > revenue_int:
        print(f'Ваша компания говно, работает в убыток!')
    else:
        print(f'Ваша компания говно, но работаете хорошо!')
        profitability = profit_int / revenue_int
        print(f'Прикинула вашу рентабельность, получается что она: {profitability}')
        workers_str = input('А, ну ка... Скажи сколько у тебя сотрудников?:\n')
        if workers_str.isnumeric():
            profitability_per_workers = profitability / int(workers_str)
            print(f'Получается, что у тебя на одного сотрудника: {profitability_per_workers} денег')
        else:
            print(f'Введённое число не корректно')
else:
    print(f'Введённые числа не корректны')

'''
6.Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который результат спортсмена составит не менее b километров. 
Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат: 
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

first_day_result_str = '2'  # input('Введите результат для первого дня в километрах, например 2:')
finish_day_result_str = '7'  # input('Введите желаемый результат в километрах, например 7:')

if first_day_result_str.isnumeric() and finish_day_result_str.isnumeric():
    first_day_result_int, new_day_result = (int(first_day_result_str) for _ in range(2))
    finish_day_result_int = int(finish_day_result_str)
    i = 0
    while new_day_result <= finish_day_result_int:
        i += 1
        new_day_result *= 1.1
        #print('{:}-день: {:02}'.format(i, new_day_result))

    print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {finish_day_result_int} км.')
else:
    print(f'Введённые числа не корректны')

