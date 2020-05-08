"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****
"""


class Cell:
    __total_count = 0

    def __init__(self, count):
        self.count = count
        Cell.__total_count += count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        return Cell(self.count - other.count) if self.count - other.count > 0 else print("Subtraction cannot "
                                                                                         "be performed")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count if other.count else print("Division cannot be performed"))

    def make_order(self, count_cells_in_row: int):
        rows_count = self.count // count_cells_in_row if count_cells_in_row else 0
        i = 1
        while i <= rows_count:
            if i != rows_count:
                print(f"{'*' * count_cells_in_row}")
            else:
                print(f"{'*' * count_cells_in_row}")
            i += 1
        print("*" * (self.count % count_cells_in_row))


test_cell_1 = Cell(15)
test_cell_2 = Cell(12)

print(f"test_cell_1 + test_cell_2: {(test_cell_1 + test_cell_2).count}")
print(f"test_cell_1 - test_cell_2: {(test_cell_1 - test_cell_2).count}")
print(f"test_cell_1 * test_cell_2: {(test_cell_1 * test_cell_2).count}")
print(f"test_cell_1 / test_cell_2: {(test_cell_1 / test_cell_2).count}")

test_cell_1.make_order(5)
test_cell_2.make_order(5)
