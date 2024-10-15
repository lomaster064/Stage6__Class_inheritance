import math

class Figure:
    sides_count = 0

    def __init__(self, *args):
        sid = []
        for i in args:
            if isinstance(i, tuple):
                self.__color = list(i)
            elif isinstance(i, bool):
                self.filled = i
            elif isinstance(i, int):
                sid.append(i)

        self.__sides = sid

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        # else:
        #     print('Введены некорректные параметры цвета')

    def __is_valid_sides(self, *args):
        flag = True
        for i in args:
            if not isinstance(i, int):
                flag = False

        if flag and len(args) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def check_sides(self):
        posled = []
        if isinstance(self, Cube) and len(self.get_sides()) == 1:
            side = self.get_sides()[0]
            for i in range(self.sides_count):
                posled.append(side)
        elif len(self.get_sides()) != self.sides_count:
            for i in range(self.sides_count):
               posled.append(1)

        self.set_sides(*posled)




class Circle(Figure):
    sides_count = 1

    def __init__(self, *args):
        super().__init__(*args)

        self.check_sides()

        self.__radius = round(self.get_sides()[0] / (2 * math.pi), 2)

    def get_square(self):
        # s = pi * r^2
        return round(math.pi * self.__radius ** 2, 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args):
        super().__init__(*args)

        self.check_sides()

    def get_square(self):
        # s = sqrt(p (p - a) (p - b) (p - c)
        p = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, *args):
        super().__init__(*args)

        self.check_sides()

    def get_volume(self):
        # V = a^3
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

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