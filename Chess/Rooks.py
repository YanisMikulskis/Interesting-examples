import string
from chess_field import chess_field
from string import ascii_lowercase as alpha
from typing import Callable


class Rooks:
    def __init__(self, coordinate: list):
        self.coordinate: list = coordinate
        self.coord_letter: list = self.coordinate[0]
        self.coord_integer: list = self.coordinate[1]
        self.alpha: list = list(alpha[:alpha.index('i')])

        self.letters_board: list = [let for let in self.alpha if let != self.coord_letter]

        self.horizontal: list = [[let, self.coord_integer] for let in self.letters_board]
        self.vertical: list = [[self.coord_letter, number] for number in range(1, 9)]

        self.board: Callable = chess_field([], 1)

    def search(self, board: list, idx: int) -> list:
        """
        Рекурсивное заполнение клеток по условиям
        Recursive filling of cells according to conditions
        """
        if idx >= len(board):
            return board
        if isinstance(board[idx], list):
            if len(board[idx]) > 2:
                self.search(board=board[idx], idx=0)
            else:
                boards = [*self.vertical, *self.horizontal]
                if board[idx][1] in boards:
                    board[idx][0] = '*'
                if board[idx][1] == self.coordinate:
                    board[idx][0] = 'C'
        idx += 1
        return self.search(board=board, idx=idx)

    def figure_on_the_field(self) -> str:
        """
        Метод окончательных вызовов и вывода шахматного поля с фигурой (с Ладьей)
        """
        result_search: list = self.search(board=self.board, idx=0)
        profit: list = list(map(lambda line: list(map(lambda cell: cell[0], line)), result_search))
        profit: str = '\n'.join([' '.join(i) for i in profit])
        return profit


def rooks_func(coordinate: list) -> Callable:
    """
    Функция создания экземпляра класса и возврата окончательного метода
    """
    rooks: Rooks[list] = Rooks(coordinate)
    return rooks.figure_on_the_field()
