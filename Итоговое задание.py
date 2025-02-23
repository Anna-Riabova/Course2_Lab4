if __name__ == "__main__":
    # Write your solution here
    pass
class Human:
    def __init__(self, name: str, age: int, pressure: int):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: имя
        :param age: возраст
        :param pressure: нормальное давление

        Примеры:
        >>> Vasya = Human("Vasya",27, 120)  # инициализация экземпляра класса
        """
        if not isinstance(name, (str)):
            raise TypeError("У человека должно быть имя")
        self.name = name

        if not isinstance(age, (int)):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")
        self.age = age

        if not isinstance(pressure, (int)):
            raise TypeError("Давление должен быть целым числом")
        if pressure < 0:
            raise ValueError("Давление не может быть отрицательным числом")
        self.pressure = pressure

    def is_teenager(self) -> bool:
        """
        Функция которая проверяет является ли человек подростком

        :return: Является ли человек подростком

        Примеры:
        >>> Vasya = Human("Vasya",27, 120)
        >>> Vasya.is_teenager()
        """

        if not self.is_teenager():
            raise ValueError("Применимо только к подросткам")

    def change_name(self, new_name: "str") -> None:
        """
        Смена имени.

        :param new_name: новое имя
        :raise TypeError: Если имя введено не корректно.


        Примеры:
        >>> Vasya = Human("Vasya",16, 120)
        >>> Vasya.change_name("Moshe")
        """
    def __str__(self) -> str:
        return f'Имя "{self.name}"'

    def __repr__(self) -> str:
        return f'Human(name={self.name!r})'  # Например, для строк важно указать !r

class Sportsmen(Human):

    def sport_pressure(self, pressure: int):
        """ Переводим норму человеческого давления к нормальному давлению под нагрузками.

        :return: Измененная норма давления

        Примеры:
        >>> Vasya = Sportsmen("Vasya", 16, 120)
        >>> Vasya.sport_pressure()

        """
        self.port_pressure = pressure + 40
        return None

    def __str__(self) -> str:
        return f'Имя "{self.name}"'

    def __repr__(self) -> str:
        return f'Human(name={self.name!r})'  # Например, для строк важно указать !r
