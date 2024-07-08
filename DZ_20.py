#  Задание 1
class Device:
    def __init__(self, brand, model, power):
        self.__brand = brand
        self.__model = model
        self.__power = int(power)

    def __str__(self):
        return f'Устройство {self.__brand} {self.__model}, мощностью {self.__power}'
    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, new_power):
        self.__power = int(new_power)


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, types_coffee):
        super().__init__(brand, model, power)
        self.__types_coffee = types_coffee

    def __str__(self):
        return f'Кофемашина {super().brand} {super().model}, мощностью {super().power}, готовит кофе - {self.__types_coffee}'

    @property
    def types_coffee(self):
        return self.__types_coffee

    @types_coffee.setter
    def types_coffee(self, new_types_coffee):
        self.__types_coffee = new_types_coffee


class Blender(Device):
    def __init__(self, brand, model, power, types_blender):
        super().__init__(brand, model, power)
        self.__types_blender = types_blender

    def __str__(self):
        return f'Блендр {super().brand} {super().model}, мощностью {super().power}, {self.__types_blender}'

    @property
    def types_blender(self):
        return self.__types_blender

    @types_blender.setter
    def types_blender(self, new_types_blender):
        self.__types_blender = new_types_blender


class MeatGrinder(Device):
    def __init__(self, brand, model, power, reverse):
        super().__init__(brand, model, power)
        self.__reverse = bool(reverse)

    def __str__(self):
        if self.__reverse:
            reverse = 'Да'
        else:
            reverse = 'Нет'
        return f'Мясорубка {super().brand} {super().model}, мощностью {super().power}, наличие реверса - {reverse}'

    @property
    def reverse(self):
        return self.__reverse

    @reverse.setter
    def reverse(self, new_reverse):
        self.__reverse = bool(new_reverse)


my_coffee = CoffeeMachine('DeLonghi', 'ETAM 29.660.SB', 1450, 'cappuccino, espresso, latte')
print(my_coffee)
my_blender = Blender('Tuvio', 'THB01PBS', 1300, 'погружной')
print(my_blender)
my_meatgrinder = MeatGrinder('REDMOND', 'RMG-1246', 1340, True)
print(my_meatgrinder)

# Задание 2
# Создайте класс Ship, который содержит информацию о корабле. С помощью механизма наследования, реализуйте класс Frigate (содержит
# информацию о фрегате), класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.
class Ship:
    def __init__(self, name, year, country):
        self.__name = name
        self.__year = int(year)
        self.__country = country

    def __str__(self):
        return f'"{self.__name}", {self.__year} года, страна - {self.__country}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = int(new_year)

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        self.__country = new_country


class Frigate(Ship):
    def __str__(self):
        return f'Фрегат "{super().name}", {super().year} года, страна - {super().country}'


class Destroyer(Ship):
    def __str__(self):
        return f'Эсминец "{super().name}", {super().year} года, страна - {super().country}'


class Cruiser(Ship):
    def __str__(self):
        return f'Крейсер "{super().name}", {super().year} года, страна - {super().country}'


my_frigate = Frigate('Надежда', 1991, 'Россия')
print(my_frigate)
my_destroyer = Destroyer('Новик', 1926, 'Россия')
print(my_destroyer)
my_cruiser = Cruiser('Аврора', 1896, 'Россия')
print(my_cruiser)

# Задание 3
class Money:
    def __init__(self, units, cents):
        self.__units = int(units)
        self.__cents = int(cents)

    def __str__(self):
        return f'Сумма - {self.__units} рублей {self.__cents} копеек'

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, new_units):
        self.__units = int(new_units)

    @property
    def cents(self):
        return self.__cents

    @cents.setter
    def cents(self, new_cents):
        self.__cents = int(new_cents)


my_money = Money(100, 50)
print(my_money)