import string
from chess_field import chess_field
from string import ascii_lowercase as alpha
from typing import Callable


class Queen:
    def __init__(self, coordinate: list):
        self.coordinate: list = coordinate
        self.coord_letter: str = self.coordinate[0]
        self.coord_integer: int = self.coordinate[1]
        self.alpha: list = list(alpha[:alpha.index('i')])

        self.letters_board: list = [let for let in self.alpha if let != self.coord_letter]

        self.horizontal: list = [[let, self.coord_integer] for let in self.letters_board]
        self.vertical: list = [[self.coord_letter, number] for number in range(1, 9)]

        self.board: list = chess_field([], 1)

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
        return self.places_dia(places=places, vector=1)

    # -------------

    def search(self, board: list, idx: int, diagonals: list) -> list:
        """
        Рекурсивное заполнение клеток по условиям
        Recursive filling of cells according to conditions
        """
        if idx >= len(board):
            return board
        if isinstance(board[idx], list):
            if len(board[idx]) > 2:
                self.search(board=board[idx], idx=0, diagonals=diagonals)
            else:
                boards = [*self.vertical, *self.horizontal, *diagonals]

                if board[idx][1] in boards:
                    board[idx][0] = '*'
                if board[idx][1] == self.coordinate:
                    board[idx][0] = 'Q'

        idx += 1
        return self.search(board=board, idx=idx, diagonals=diagonals)

    def figure_on_the_field(self) -> str:
        """
        Метод окончательных вызовов и вывода шахматного поля с фигурой (с Ферзем)
        """
        diagonals = self.places_dia([], -1)
        result_search = self.search(board=self.board, idx=0, diagonals=diagonals)
        profit = list(map(lambda line: list(map(lambda cell: cell[0], line)), result_search))
        profit = '\n'.join([' '.join(i) for i in profit])
        return profit


def queen_func(coordinate: list) -> Callable:
    """
    Функция создания экземпляра класса и возврата окончательного метода
    """
    queen: Queen[list] = Queen(coordinate)
    return queen.figure_on_the_field()
