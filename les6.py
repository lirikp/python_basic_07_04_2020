# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
# Класс Transport
import time
from itertools import cycle


class TrafficLight:
    __color = None

    def __init__(self, c='green'):
        TrafficLight.__color = c

    def running(self):
        for color_now, pause_sec in cycle({'red': 7, 'yellow': 2, 'green': 7}.items()):
            print(f'{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())} пауза:{pause_sec}, {self.__color}')
            if not TrafficLight.change_light(self, color=color_now):
                print("Не верная последовательность цветов")
                break
            time.sleep(pause_sec)

    def change_light(self, color):

        if color == 'red' and self.__color == 'green':
            self.__color = 'red'
            return True

        elif color == 'green' and self.__color == 'yellow':
            self.__color = 'green'
            return True

        elif color == 'yellow' and self.__color == 'red':
            self.__color = 'yellow'
            return True

        else:
            return False


x = TrafficLight(c='yellow')
x.running()


# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _lenght = 0
    _width = 0

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def count_weight(self):
        m = self._width * self._lenght * 25
        print(f'на участок в {self._width}м*{self._lenght}м будет использовано {m}киллограмм асфальта')


x = Road(23, 25)
x.count_weight()


# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, wage, bonus, name, surname):
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, wage, bonus, name, surname, position):
        super().__init__(wage, bonus, name, surname)
        self.position = position

    def get_full_name(self):
        print(f"{self.name} {self.surname} {self.position}")

    def get_total_income(self):
        print(f'Total: {self._income["wage"] + self._income["bonus"]}')


worker = Position(101.1, 20.5, 'Вася', 'Пупкин', 'Девелопер')
worker.get_full_name()
worker.get_total_income()


# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'CAR Speed: {self.speed}km/h')

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        self.direction = direction
        print("direction: ", direction)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print('High speed LIMIT')
        print(f'TownCAR Speed: {self.speed}km/h')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'SportCar Speed: {self.speed}km/h')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print('High speed LIMIT')

        print(f'WorkCar Speed: {self.speed}km/h')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'PoliceCar Speed: {self.speed}km/h')


carPolice = PoliceCar(160, 'red', 'Lamborghini Reventon', True)
carPolice.show_speed()
carPolice.go()
carPolice.turn('left')
carPolice.stop()

w_car = WorkCar(100, 'red', 'Ford Focus')
w_car.show_speed()
w_car.go()
w_car.turn('right')
w_car.stop()

s_car = SportCar(300, 'red', 'Ferrary')
s_car.show_speed()
s_car.go()
s_car.turn('straight')
s_car.stop()

t_car = TownCar(10, 'blue', 'Lexus NX')
t_car.show_speed()
t_car.go()
t_car.turn('left')
t_car.stop()


# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}')


pen = Pen('Ручкой')
pen.draw()

pencil = Pencil('Карандашом')
pencil.draw()

handle = Handle('Маркером')
handle.draw()

s = Stationery('Концелярия')
s.draw()