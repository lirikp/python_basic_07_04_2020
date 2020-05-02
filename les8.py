# -*- coding: utf8 -*-

# 1 Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class DateClass:

    @classmethod
    def to_int_DMY(cls, date_str: str) -> tuple:
        try:
            d, m, y = (int(date_str[:2]), int(date_str[2:4]), int(date_str[4:]),)
        except ValueError:
            print(f'Не могу преобразовать {date_str}')
        except Exception as e:
            print(f'Ошибка {e}')
        else:
            return d, m, y

    @staticmethod
    def date_validate(*args) -> bool:
        d, m, y = args[0]
        if (d < 0 and d > 31) or (m > 0 and m > 12) or (y < 1970 and y > 2100):
            print(f'Ошибка с датой {d}-{m}-{y}')
            return False

        print(f"Правильная дата {d}-{m}-{y}")
        return True


print(DateClass.to_int_DMY('3040202D'))  # Вызов метода через название класса
x = DateClass()
x.date_validate(DateClass.to_int_DMY('30402020'))
x.date_validate(DateClass.to_int_DMY('30122020'))

# 2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self, string_message):
        self.message = string_message

    def ZeroDivisionError(self):
        print(self.message)


inp_data = input("Введите число: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise MyZeroDivisionError("Что за лошпед ввёл число равное 0!!!")
except ValueError:
    print("Вы ввели не число")
except MyZeroDivisionError as err:
    print(err)
else:
    print(f"Урра! Ваше число: {inp_data}")


# 3 Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class IntError(Exception):
    def __init__(self, string_message):
        self.message = string_message

big_data = []
while True:
    inp_data = input(f'Введите "stop" или число:\n')
    if inp_data == 'stop':
        break;
    try:
        if not inp_data.isnumeric():
            raise IntError(f'Не целое число!\n')
        value_int = int(inp_data)
    except IntError as e:
        print(e)

    else:
        big_data.append(value_int)


# 4 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class OfficeEquipment():
    type = str()

    def __init__(self, equipment_name: str, scale: str, list_per_minute=1, net=False, voltage=220, ):
        self.equipment_name = equipment_name  # Название техники по документам
        self.voltage = voltage  # Сетевое питание
        self.scale = scale  # Рабочее разрешение
        self.list_per_minute = list_per_minute  # Количество обрабатываемых листов в минуту
        self.net = net  # Возможность подключение к Ethernet

    @property
    def get_info_type(self):
        return self.type


class WareHouse():
    ware_house_data = {}

    def __init__(self):
        pass

    def to_ware_house(self, obj: object):
        if self.ware_house_data.get(obj.get_info_type) is not None:
            count = len(self.ware_house_data[obj.get_info_type]) if len(
                self.ware_house_data[obj.get_info_type]) else 0  # получаем следующий ключ
            count += 1
            self.ware_house_data[obj.get_info_type][count] = []  # Дурацкая система с предварительным добавлением ключа
            self.ware_house_data[obj.get_info_type][count].append(obj)
        else:
            self.ware_house_data[obj.get_info_type] = {}  # Дурацкая система с предварительным добавлением словаря
            self.ware_house_data[obj.get_info_type][1] = [obj]

    def to_departament(self, type_to_give: str) -> tuple:
        if self.ware_house_data.get(type_to_give) is not None:
            return self.ware_house_data[type_to_give].popitem()
        else:
            print(f'Склад пуст')
            return None

    def get_remains(self):
        return self.ware_house_data  # Получаем полностью склад


class Scaner(OfficeEquipment):
    type = 'scaner'

    def __init__(self, type_scan: str, equipment_name, scale, *args, **kwargs):
        self.type_scan = type_scan  # Ручной сканер, планшетный сканер
        super().__init__(equipment_name, scale, *args, **kwargs)


class Printer(OfficeEquipment):
    type = 'printer'

    def __init__(self, print_type, equipment_name, scale, *args, **kwargs):
        self.print_type = print_type  # Струйный, лазерный, матричный
        super().__init__(equipment_name, scale, *args, **kwargs)


class Сopier(OfficeEquipment):
    type = 'copier'

    def __init__(self, time_to_first_copy, equipment_name, scale, *args, **kwargs):
        self.time_to_first_copy = time_to_first_copy  # Время выхода первой копии
        super().__init__(equipment_name, scale, *args, **kwargs)


scanner1 = Scaner('ручной', 'Canon CanoScan LiDE300', 'A4', voltage=110)
scanner2 = Scaner('планшет', 'Samsung idsA2', 'A2', voltage=110)
scanner3 = Scaner('ручной', 'Epson ASASA', 'A3', voltage=110)

prn1 = Printer('струйник', 'HP', 'A2', net=True)
prn2 = Printer('лазерный', 'Canon', 'A4')
prn3 = Printer('матричный', 'Samsung', 'A4')

co1 = Сopier(1, 'HP', 'A2')
co2 = Сopier(10, 'Canon', 'A1')
co3 = Сopier(3, 'Samsung', 'A4', net=True)


# 5 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
wh = WareHouse()
wh.to_ware_house(scanner1)
wh.to_ware_house(scanner2)
wh.to_ware_house(scanner3)
wh.to_ware_house(prn1)
wh.to_ware_house(prn2)
wh.to_ware_house(prn3)
wh.to_ware_house(co1)
wh.to_ware_house(co2)
wh.to_ware_house(co3)

id, obj = wh.to_departament('printer')

print(obj[0].equipment_name)


# 6 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class VoltageError(Exception):
    def __init__(self, string_message):
        self.message = string_message



while True:
    #scanner1 = Scaner('ручной', 'Canon CanoScan LiDE300', 'A4', voltage=110)
    type_obj = input(f'Введите тип объекта scaner,copier,printer или "stop":\n')
    if type_obj == 'stop':
        break;
    elif type_obj == 'scaner':
        type_scan = input(f'Введите тип сканирования ручной, планшетный :\n')
        name = input(f'Введите тип объекта scaner,copier,printer или "stop":\n')
        format = input(f'Введите формат А1,А2,А3 итд. или "stop":\n')
        voltage = input(f'Введите величину напряжения 220 или 110 или "stop":\n')

    try:
        if voltage is not '220' or voltage is not '110':
            raise VoltageError(f'Введено не 220 и не 110\n')
        value_int = int(inp_data)
    except VoltageError as e:
        print(e)

    else:
        wh.to_ware_house(Scaner(type_scan,name,format,voltage=voltage))

#    elif type_obj == 'copier':
#    elif type_obj == 'printer':


# 7 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber():
    def __init__(self, c):
        self.complex = c

    def __add__(self, other):
        return self.complex + other

    def __mul__(self, other):
        return self.complex * other

c1 = ComplexNumber((1+2j))
c2 = ComplexNumber((1-5j))
print(c1 + c2.complex)
print(c1 * c2.complex)