import string
from chess_field import chess_field
from string import ascii_lowercase as alpha
from typing import Callable


class Horse:
    def __init__(self, coordinate: list):
        self.coordinate: list = coordinate
        self.coord_letter: str = self.coordinate[0]
        self.coord_integer: int = self.coordinate[1]

        self.alpha: list = list(alpha[:alpha.index('i')])
        letter_index: int = self.alpha.index(self.coord_letter)

        lateral_lines: dict = {
            'a': [None, None, *self.alpha[:letter_index + 3]],
            'b': [None, *self.alpha[letter_index - 1:letter_index + 3]],
            'g': [*self.alpha[letter_index - 2:], None],
            'h': [*self.alpha[letter_index - 2:], None, None]
        }

        if self.coord_letter in ['a', 'b', 'g', 'h']:
            self.point_letter: list = lateral_lines[self.coord_letter]
        else:
            self.point_letter: list = self.alpha[letter_index - 2:letter_index + 3]
        # избавляемся от координаты фигуры в списке рабочих буквенных координат вариантов движения
        self.point_letter.pop(self.point_letter.index(self.coord_letter))

        self.result: list = []
        for i in range(4):
            if self.point_letter[i] is not None:
                if i == 0 or i == 3:
                    self.result.append([
                        [self.point_letter[i], self.coord_integer - 1],
                        [self.point_letter[i], self.coord_integer + 1]
                    ])
                else:
                    self.result.append([
                        [self.point_letter[i], self.coord_integer - 2],
                        [self.point_letter[i], self.coord_integer + 2]
                    ])

        self.board: Callable = chess_field(chess_board=[], line=1)

    def search(self, board: list, idx: int) -> list:
        """
        Рекурсивное заполнение клеток по условиям
        Recursive filling of cells according to conditions
        """
        borders: list = [item for elem in self.result for item in elem]
        if idx >= len(board):
            return board
        if isinstance(board[idx], list):
            if len(board[idx]) > 2:
                self.search(board=board[idx], idx=0)
            else:
                if board[idx][1] in borders:
                    board[idx][0] = '*'
                if board[idx][1] == self.coordinate:
                    board[idx][0] = 'H'
        idx += 1
        return self.search(board=board, idx=idx)

    def figure_on_the_field(self) -> str:
        """
        Метод окончательных вызовов и вывода шахматного поля с фигурой (с Конем)
        """
        result_search: list = self.search(board=self.board, idx=0)
        profit: list = list(map(lambda line: list(map(lambda cell: cell[0], line)), result_search))
        profit: str = '\n'.join([' '.join(i) for i in profit])
        return profit


def horse_func(coordinate: list) -> Callable:
    """
    Функция создания экземпляра класса и возврата окончательного метода
    """
    horse: Horse[list] = Horse(coordinate)
    return horse.figure_on_the_field()
