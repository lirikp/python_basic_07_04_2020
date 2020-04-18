# -*- coding: utf8 -*-

# Как сделать tuple SET комприхейшен
#
# Практическое задание
# 1 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("data_file.txt", 'w') as f:
    while True:
        my_str = input("Введите строку для заброски в файл:\n")
        if my_str != ' ':
            f.write(my_str + '\n')
        else:
            break

# 2 Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("data_file.txt", "r") as f:
    for num_line, my_str in enumerate(f):
        print(f"(строка {num_line}, "
              f"количество символов {len(my_str)}, "
              f"количество слов {len(my_str.split())}) СТРОКА: {my_str}")

# 3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

list_less_20 = []
sum_salary = float()
with open('salary.txt', 'r', encoding='utf-8') as f:
    for i, item_str in enumerate(f):
        item_name, item_salary = item_str.split()
        item_salary_float = float(item_salary)
        if item_salary_float < 20000:
            list_less_20.append(item_name)

        sum_salary += item_salary_float
    avg_salary = sum_salary / (i + 1)

print('Сотрудники за чертой бедности: ', list_less_20, f"Средняя ЗП: {avg_salary.__round__(2)}")

# 4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_nums_russian = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('nums.txt', 'r') as f:
    for i, item_str in enumerate(f):
        item_text, item_digit = item_str.split(' - ')
        with open('new_nums.txt', 'a', encoding='utf-8') as nf:
            nf.write(dict_nums_russian[int(item_digit)] + ' - ' + item_digit)

# 5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

list_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open('sum_digits.txt', 'w') as f:
    f.write(' '.join(map(str, list_digits)) + '\n')

with open('sum_digits.txt') as f:
    print(sum(map(int, f.read().split())))


# 6 Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def make_object(tmp):
    dict_object["lesson"] += int(tmp[1]) if tmp[1] != '' else 0
    dict_object["practice"] += int(tmp[2]) if tmp[2] != '' else 0
    dict_object["labs"] += int(tmp[3]) if tmp[3] != '' else 0
    return dict_object


dict_object = {"lesson": 0, "practice": 0, "labs": 0}
with open("study.txt", encoding="utf-8") as f:
    for _ in (tmp.rstrip() for tmp in f.readlines()):
        dict_object = make_object(_.split("|"))

# 7 Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

to_awg_profit_list = []
with open("firm_data.txt", encoding="utf-8") as f:
    for i, _ in enumerate(f):
        tmp = _.rstrip().split('|')
        profit = int(tmp[2]) - int(tmp[3])
        if profit > 0:
            to_awg_profit_list.append(profit)
awg_profit = sum(to_awg_profit_list) / (i + 1)

print(to_awg_profit_list, awg_profit)
