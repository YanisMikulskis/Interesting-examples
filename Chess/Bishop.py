import string
from chess_field import chess_field
from string import ascii_lowercase as alpha
from typing import Callable


class Bishop:
    def __init__(self, coordinate: list):
        self.coordinate: list = coordinate
        self.coord_letter: str = self.coordinate[0]
        self.coord_integer: int = self.coordinate[1]
        self.alpha: list = list(alpha[:alpha.index('i')])
        self.board: Callable = chess_field([], 1)

    def places_dia(self, places: list, vector: int) -> list:
        """
        Рекурсивное создание координат диагоналей для текущего положения фигуры
        Recursively creating diagonal coordinates for the current shape position
        """
        if len(places) == 2:  # если обе диагонали заполнены
            places = [cell for line in places for cell in line]  # "склеиваем" их в один список
            return places  # profit
        start = self.coord_integer - len(self.alpha[:self.alpha.index(self.coord_letter)]) * vector
        result = []
        step = 1

        # Цикл заполнения цифр для координат, отталкивающийся от start - разницы между текущей цифрой и длиной
        # [среза alpha (первых 8-ми букв алфавита) до текущей буквы]
        for _ in range(8):
            result.append(start)
            start += step * vector

        def conditions(cell: list) -> bool:
            """
            Функция для "склеивания" только того, что имеет координату от 1 до 8 включительно и не равно исходной
            координате. Нам в шахматных клетках не нужны координаты меньше 1 и больше 8
            A function for "gluing" only what has a coordinate from 1 to 8 inclusive and is not equal to the original
            coordinate. We don’t need coordinates less than 1 and more than 8 in chess cells.
            """
            if 1 <= cell[1] <= 8 and cell != self.coordinate:
                return True

        places.append([cell for cell in list(map(list, list(zip(self.alpha, result)))) if conditions(cell)])
        return self.places_dia(places, 1)

    # -------------

    def search(self, lst: list, idx: int, diagonals: list) -> list:
        """
        Рекурсивное заполнение клеток по условиям
        Recursive filling of cells according to conditions
        """
        if idx >= len(lst):
            return lst
        if isinstance(lst[idx], list):
            if len(lst[idx]) > 2:
                self.search(lst[idx], 0, diagonals)
            else:
                if lst[idx][1] in diagonals:
                    lst[idx][0] = '*'
                if lst[idx][1] == self.coordinate:
                    lst[idx][0] = 'B'

        idx += 1
        return self.search(lst, idx, diagonals)

    def figure_on_the_field(self) -> str:
        diagonals = self.places_dia([], -1)

        result_search = self.search(self.board, 0, diagonals)
        profit = list(map(lambda line: list(map(lambda cell: cell[0], line)), result_search))
        profit = '\n'.join([' '.join(i) for i in profit])
        return profit


def bishop_func(coordinate: list) -> Callable:
    bishop = Bishop(coordinate)
    return bishop.figure_on_the_field()
