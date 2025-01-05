import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in new_sides))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        if len(sides) == 1:
            self.__sides = [sides[0]]
        else:
            self.__sides = [1]

        self.__radius = (self.__sides[0] / (2 * math.pi) )

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12
                                                 # вначале пытался ввести self.__sides = sides, но проверка из
    def __init__(self, color, *sides):           # родительского класса все равно выводила 12 единиц
        super().__init__(color, *sides)    # долго ломал голову сам, потом мучил нейросеть,
        if len(sides) == 1:                      # а к такому простому решению пришли далеко не сразу
            # Устанавливаем все 12 сторон равными переданному значению
            self.set_sides(*([sides[0]] * self.sides_count))
        else:
            self.set_sides(1)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(cube1.get_volume())
print(circle1.get_sides())
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triangle = Triangle((200, 200, 100), 10, 6)
print(triangle.get_sides())
triangle.set_sides(2,3,4)

print(triangle.__len__())

print(triangle.get_sides())
