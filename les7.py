# -*- coding: utf8 -*-


# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
## Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        [print(' '.join(map(str, _))) for i, _ in enumerate(self.matrix)]

    def __add__(self, other):
        new_matrix = self.matrix.copy()
        for i, _ in enumerate(self.matrix):
            for j, vol in enumerate(_):
                new_matrix[i][j] += other[i][j]

        return Matrix(new_matrix)


mat1 = Matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9], ])
mat1.__str__()
mat2 = mat1.__add__([[100, 200, 300],
                     [400, 500, 600],
                     [700, 800, 900], ]).__str__()

# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:  реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Сlothers(ABC):

    def __init__(self, name, *args, **kwargs):
        self.name = name

    @abstractmethod
    def summ(self, vol):
        pass


class SuitClothers(Сlothers):
    expense_vol = 0

    def __init__(self, height, *args, **kwargs):
        self.height = height
        super().__init__(*args, **kwargs)

    @property
    def expense(self):
        self.expense_vol = 2 * self.height + 0.3
        return self.expense_vol

    def summ(self, vol):
        return self.expense() + vol


class CoatClothers(Сlothers):
    expense_vol = 0

    def __init__(self, size, *args, **kwargs):
        self.size = size
        super().__init__(*args, **kwargs)

    @property
    def expense(self):
        self.expense_vol = self.size / 6.5 + 0.5
        return self.expense_vol

    def summ(self, vol):
        return self.expense_vol + vol


suit = SuitClothers(58, name='Big suit')
print(suit.expense)

coat = CoatClothers(34, name='Small coat')
print(coat.expense)

print(coat.summ(suit.expense))


# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.


class BasicUnit(object):

    def __init__(self, cells, name):
        self.cells = cells
        self.name = name

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        if cells < 0:
            self.__cells = 1
            print(f"Клетка с отрицательным значением ячеек, значение приравниваю к 1")
        else:
            self.__cells = cells

    def __add__(self, second_cell):
        self.cells += second_cell.cells
        return self.cells

    def __sub__(self, second_cell):
        tmp = self.cells - second_cell.cells
        if tmp > 0:
            self.cells = tmp
            return self.cells
        else:
            return f'При вычитании разница между клетками отрицательная'

    def __mul__(self, second_cell):
        self.cells *= second_cell.cells
        return self.cells

    def __truediv__(self, second_cell):
        self.cells //= second_cell.cells
        return self.cells

    def __del__(self):
        print(f'Клетка {self.name} уничтожается!')

    def make_order(self, num):
        remains, d = (self.cells % num , self.cells // num)
        string_cells = []
        for _ in range(0, d):
            string_cells.append(''.join(['*' for i in range(0, num)]) + '\n')
        string_cells.append(''.join(['*' for i in range(0, remains)]))
        for _ in string_cells:
            print(_, end='')



c = BasicUnit(3, 'basic')

print(c.__add__(BasicUnit(23, 'other1')))
print(c.__truediv__(BasicUnit(2, 'other2')))

c.make_order(3)
