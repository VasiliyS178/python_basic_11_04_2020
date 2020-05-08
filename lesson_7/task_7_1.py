"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, itm_list):
        self.itm_list = itm_list

    def __str__(self):
        result_string = ""
        for itm_1 in self.itm_list:
            for itm_2 in itm_1:
                result_string += f"{itm_2} "
            result_string += "\n"
        return result_string

    def __add__(self, other):
        result_list = []
        row_list = []
        for i in range(len(self.itm_list)):
            for j in range(len(self.itm_list[i])):
                row_list.append(self.itm_list[i][j] + other.itm_list[i][j])
                j += 1
            result_list.append(row_list[:])
            row_list.clear()
            i += 1
        return Matrix(result_list)


test_matrix_1 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
test_matrix_2 = Matrix([[90, 80, 70], [60, 50, 40], [30, 20, 10]])

test_matrix_3 = Matrix([[10, 20, 30], [40, 50, 60]])
test_matrix_4 = Matrix([[90, 80, 70], [60, 50, 40]])

test_matrix_5 = Matrix([[10, 20], [30, 40], [50, 60]])
test_matrix_6 = Matrix([[90, 80], [70, 60], [50, 40]])

print(test_matrix_1)
print(test_matrix_2)
print(test_matrix_1 + test_matrix_2)
print(test_matrix_3)
print(test_matrix_4)
print(test_matrix_3 + test_matrix_4)
print(test_matrix_5)
print(test_matrix_6)
print(test_matrix_5 + test_matrix_6)
