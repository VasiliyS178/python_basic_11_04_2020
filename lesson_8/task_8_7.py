"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real: int, imag: int):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex((self.real + other.real), (self.imag + other.imag))

    def __mul__(self, other):
        return complex((self.real * other.real - self.imag * other.imag),
                       (self.imag * other.real + self.real * other.imag))


test_num_1 = ComplexNumber(5, 7)
test_num_2 = ComplexNumber(50, 70)

assert test_num_1 + test_num_2 == complex(5, 7) + complex(50, 70)
assert test_num_1 * test_num_2 == complex(5, 7) * complex(50, 70)
