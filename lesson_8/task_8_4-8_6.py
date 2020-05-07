"""
8.4.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
8.5.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
8.6.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self, warehouse_name: str, location: str, capacity: int):
        self.__warehouse_name = warehouse_name
        self.__location = location
        self.__capacity = capacity
        self.__register = {}
        self.__shipments = {}

    def get_equipment(self, office_equipment, count: int):
        if isinstance(office_equipment, OfficeEquipmentAbstract) and type(count) == int and count > 0:
            equipment_name = office_equipment.name
            if equipment_name in self.__register:
                self.__register[equipment_name] += count
            else:
                self.__register[equipment_name] = count
            self.__capacity -= count
        else:
            print("Wrong equipment's type or count")
        return self.__register

    def dispatch_equipment(self, office_equipment, count: int, department: str):
        if isinstance(office_equipment, OfficeEquipmentAbstract) and type(count) == int and count > 0:
            equipment_name = office_equipment.name
            if equipment_name in self.__register:
                access_count = self.__register[equipment_name]
                if access_count >= count:
                    self.__register[equipment_name] -= count
                    self.__capacity += count
                    if department in self.__shipments:
                        self.__shipments[department] += count
                    else:
                        self.__shipments[department] = count
                else:
                    print(f"There are only {access_count} {equipment_name} at the warehouse")
            else:
                print(f"There are not {equipment_name} at the warehouse")
        else:
            print("Wrong equipment's type or count")
        return self.__register

    @property
    def register(self):
        return self.__register

    @property
    def shipments(self):
        return self.__shipments

    @property
    def current_capacity(self):
        return self.__capacity


class OfficeEquipmentAbstract(ABC):
    def __init__(self, equipment_name: str, manufacturer: str, model: str):
        self._equipment_name = equipment_name
        self._manufacturer = manufacturer
        self._model = model

    @abstractmethod
    def name(self):
        pass


class Printer(OfficeEquipmentAbstract):
    def __init__(self, equipment_name: str, manufacturer: str, model: str, printing_speed: int, printer_type: str):
        super().__init__(equipment_name, manufacturer, model)
        self.__printing_speed = printing_speed
        self.__printer_type = printer_type

    @property
    def name(self):
        return f"{self._equipment_name} {self._manufacturer} {self._model} {self.__printer_type}"


class Scanner(OfficeEquipmentAbstract):
    def __init__(self, equipment_name: str, manufacturer: str, model: str, scanner_type: str):
        super().__init__(equipment_name, manufacturer, model)
        self.__scanner_type = scanner_type

    @property
    def name(self):
        return f"{self._equipment_name} {self._manufacturer} {self._model} {self.__scanner_type}"


class Copier(OfficeEquipmentAbstract):
    def __init__(self, equipment_name: str, manufacturer: str, model: str, copier_type: str, copier_format: str):
        super().__init__(equipment_name, manufacturer, model)
        self.__copier_type = copier_type
        self.__copier_format = copier_format

    @property
    def name(self):
        return f"{self._equipment_name} {self._manufacturer} {self._model} {self.__copier_type}"


if __name__ == '__main__':
    my_wh = Warehouse("WH1", "SPB, Piskarevskaya str., 178", 1500)
    printer = Printer("Printer", "HP", "1320", 10, "LJ")
    scanner = Scanner("Scanner", "Epson", "SC111", "A4")
    copier = Copier("Copier", "Xerox", "SCX4100", "Speed", "A3")

    print(printer.name)
    print(scanner.name)
    print(copier.name)
    print(my_wh.get_equipment(printer, "r"))
    print(my_wh.get_equipment(scanner, 50))
    print(my_wh.get_equipment(copier, 10))
    print(my_wh.dispatch_equipment(printer, 3, "Dep1"))
    print(my_wh.dispatch_equipment(scanner, 3, "Dep2"))
    print(my_wh.dispatch_equipment(copier, 3, "Dep3"))

    print(0)