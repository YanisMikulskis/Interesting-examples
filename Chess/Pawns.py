import string
from chess_field import chess_field
from string import ascii_lowercase as alpha
from typing import Callable


class Pawns:
    def __init__(self, coordinate):
        self.coordinate: list = coordinate
        self.coord_letter: str = self.coordinate[0]
        self.coord_integer: int = self.coordinate[1]
        self.alpha: list = list(alpha[:alpha.index('i')])
        self.up_coord: list = [[self.coord_letter, self.coord_integer - 1],
                               [self.coord_letter, self.coord_integer - 2]]

        self.board: Callable = chess_field(chess_board=[], line=1)

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

                if board[idx][1] in self.up_coord:
                    board[idx][0] = '*'
                if board[idx][1] == self.coordinate:
                    board[idx][0] = 'P'

        idx += 1
        return self.search(board=board, idx=idx)

    def figure_on_the_field(self) -> str:
        """
        Метод окончательных вызовов и вывода шахматного поля с фигурой (с Пешкой)
        """
        result_search: list = self.search(board=self.board, idx=0)
        profit: list = list(map(lambda line: list(map(lambda cell: cell[0], line)), result_search))
        profit: str = '\n'.join([' '.join(i) for i in profit])
        return profit


def pawns_func(coordinate: list) -> Callable:
    """
    Функция создания экземпляра класса и возврата окончательного метода
    """
    pawns: Pawns[list] = Pawns(coordinate)
    return pawns.figure_on_the_field()
