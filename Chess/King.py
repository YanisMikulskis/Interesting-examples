from chess_field import chess_field
from string import ascii_lowercase as alphabet
from typing import Callable


class King:
    def __init__(self, coordinate: list):
        self.coordinate: list = coordinate
        self.coord_letter: str = self.coordinate[0]
        self.coord_integer: int = self.coordinate[1]

        self.alpha: list = list(alphabet[:alphabet.index('i')])
        index_letter: int = self.alpha.index(self.coord_letter)

        self.left_coord: list = [self.alpha[index_letter - 1], self.coord_integer] if self.coord_letter != 'a' else ...
        self.right_coord: list = [self.alpha[index_letter + 1], self.coord_integer] if self.coord_letter != 'h' else ...

        self.up_coord: list = [self.coord_letter, self.coord_integer - 1] if self.coord_integer > 1 else ...
        self.down_coord: list = [self.coord_letter, self.coord_integer + 1] if self.coord_integer < 8 else ...

        self.board: Callable = chess_field(chess_board=[], line=1)

    def places_dia(self, places: list, vector: int) -> list:
        """
        Рекурсивное создание координат диагоналей для текущего положения фигуры
        Recursively creating diagonal coordinates for the current shape position
        """
        if len(places) == 2:  # если обе диагонали заполнены
            places: list = [cell for line in places for cell in line]  # "склеиваем" их в один список
            return places  # profit
        start: int = self.coord_integer - len(self.alpha[:self.alpha.index(self.coord_letter)]) * vector
        result: list = []
        step: int = 1
        # ниже цикл заполнения цифр для координат, отталкивающийся от start - разницы между текущей цифрой и длиной
        # [среза alpha (первых 8-ми букв алфавита) до текущей буквы]
        for _ in range(8):  # цикл заполнения цифрами, опирающимися на start
            result.append(start)
            start += step * vector

        def conditions(cell: list) -> bool:
            """
            Функция для "склеивания" только того, что имеет координату от меньше или больше исходной координаты на 1
            (король ходит только на одну клетку) включительно и не равно исходной
            координате. Нам в шахматных клетках не нужны координаты меньше 1 и больше 8
            A function for "gluing" only what has a coordinate from 1 to 8 inclusive and is not equal to the original
            coordinate. We don’t need coordinates less than 1 and more than 8 in chess cells.
            """
            if cell != self.coordinate:
                if cell[1] - 1 <= self.coordinate[1] <= cell[1] + 1:
                    return True

        places.append([cell for cell in list(map(list, list(zip(self.alpha, result)))) if conditions(cell)])
        return self.places_dia(places=places, vector=1)

    # -------------

    def search(self, board: list, idx: int, diagonals: list) -> list:
        """
        Рекурсивное заполнение клеток по условиям
        Recursive filling of cells according to conditions
        """
        borders: list = [self.left_coord,
                         self.right_coord,
                         self.up_coord,
                         self.down_coord,
                         *diagonals]
        if idx >= len(board):
            return board
        if isinstance(board[idx], list):
            if len(board[idx]) > 2:
                self.search(board=board[idx], idx=0, diagonals=diagonals)
            else:
                if board[idx][1] in borders:
                    board[idx][0] = '*'

                if board[idx][1] == self.coordinate:
                    board[idx][0] = 'K'

        idx += 1
        return self.search(board=board, idx=idx, diagonals=diagonals)

    def figure_on_the_field(self) -> str:
        """
        Метод окончательных вызовов и вывода шахматного поля с фигурой (с Королем)
        """
        diagonals: list = self.places_dia(places=[], vector=-1)
        result_search: list = self.search(board=self.board, idx=0, diagonals=diagonals)
        profit: list = list(map(lambda line: list(map(lambda cell: cell[0], line)), result_search))
        profit: str = '\n'.join([' '.join(i) for i in profit])
        return profit


def king_func(coordinate: list) -> Callable:
    """
    Функция создания экземпляра класса и возврата окончательного метода
    """
    king: King[list] = King(coordinate=coordinate)
    return king.figure_on_the_field()
