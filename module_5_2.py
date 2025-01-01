class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Purple', 'Cyan']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def get_owner(self):
        return f'Владелец: {self.owner}'

    def print_info(self):
        return print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\n{self.get_owner()}')

    def set_color(self, new_color):
        self.__COLOR_VARIANTS = [i.lower() for i in self.__COLOR_VARIANTS]

        if new_color.lower() in self.__COLOR_VARIANTS:
                self.__color = new_color
        if new_color.lower() not in self.__COLOR_VARIANTS:
                print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_passengers_limit(self):
        return print(f'Лимит пассажиров: {self.__PASSENGERS_LIMIT}')
    pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II',  500, 'blue')
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
vehicle1.get_passengers_limit()