"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self._income = is_police

    def go(self):
        print(f"The {self.name} is moving")

    def stop(self):
        self.speed = 0
        print("The car stopped")

    def turn(self, direction):
        print(f"The car turned {direction}")

    def show_speed(self):
        print(f"Car's speed now is: {self.speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police, speed_limit=60):
        super().__init__(speed, color, name, is_police)
        self.__speed_limit = speed_limit

    def show_speed(self):
        if self.speed > self.__speed_limit:
            print("The speed limit is broken")
        print(f"{self.name}'s speed now is: {self.speed}")


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police, speed_limit=40):
        super().__init__(speed, color, name, is_police)
        self.__speed_limit = speed_limit

    def show_speed(self):
        if self.speed > self.__speed_limit:
            print("The speed limit is broken")
        print(f"{self.name}'s speed now is: {self.speed}")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


if __name__ == '__main__':
    town_car_1 = TownCar(59, "red", "Minivan", False)
    work_car_1 = WorkCar(50, "grey", "Lorry", False)

    town_car_1.go()
    town_car_1.show_speed()
    town_car_1.turn("left")
    town_car_1.stop()
    town_car_1.show_speed()

    work_car_1.go()
    work_car_1.show_speed()
    work_car_1.turn("right")
    work_car_1.stop()
    work_car_1.show_speed()