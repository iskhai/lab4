import math

class Point_n:
    """
    Клас для представлення точки на площині з атрибутами:
    - координати x і y
    - кількість створених екземплярів класу
    """

    __instances_count = 0  # Змінна класу для підрахунку екземплярів

    def __init__(self, x=0, y=0):
        """
        Конструктор класу. Приймає координати точки.
        """
        self.__x = 0
        self.__y = 0
        self.x = x  # Використовуємо сеттер
        self.y = y  # Використовуємо сеттер
        Point_n.__instances_count += 1

    def __del__(self):
        """
        Деструктор класу. Зменшує кількість екземплярів та виводить повідомлення.
        """
        Point_n.__instances_count -= 1
        print("Об'єкт з координатами ({self.__x}, {self.__y}) було видалено.")

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x."""
        self.__x = value if -100 <= value <= 100 else 0

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y."""
        self.__y = value if -100 <= value <= 100 else 0

    @classmethod
    def get_instance_count(cls):
        """
        Метод класу для отримання кількості екземплярів.
        """
        return cls.__instances_count

    def move(self, dx, dy):
        """
        Метод для зміщення точки на dx та dy.
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        Метод для обчислення відстані до іншої точки.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
