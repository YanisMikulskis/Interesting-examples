# На шахматной доске 8 х 8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые
# бьет ферзь. Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте звездочками *,
# остальные клетки заполните точками. Шахматный ферзь может ходить по вертикали, горизонтали и по диагоналям.
#
# Входные данные:
#
# Координаты ферзя на шахматной доске в формате номер столбца (буква от a до h, слева направо) и номер строки
# (цифра от 1 до 8, снизу вверх).
#
# Пример ввода:
#
# c5
#
# Выходные данные:
#
# Программа выводит стилизованное изображение шахматной доски со схемой возможных передвижений ферзя.

# . . * . . . * .
# . . * . . * . .
# * . * . * . . .
# . * * * . . . .
# * * Q * * * * *
# . * * * . . . .
# * . * . * . . .
# . . * . . * . .

# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . * * * . . . .
# . * K * . . . .
# . * * * . . . .
# . . . . . . . .
# . . . . . . . .
import string
from Queen import queen_func
from King import king_func
from Bishop import bishop_func
from Rooks import rooks_func
from Horse import horse_func
from Pawns import pawns_func
from typing import Callable


class Chess:
    def __init__(self, figure: str, coordinate: list):
        self.figure: str = figure
        self.coordinate: list = coordinate

    def queen_placement(self) -> Callable:
        return queen_func(coordinate=self.coordinate)

    def king_placement(self) -> Callable:
        return king_func(coordinate=self.coordinate)

    def bishop_placement(self) -> Callable:
        return bishop_func(coordinate=self.coordinate)

    def rooks_placement(self) -> Callable:
        return rooks_func(coordinate=self.coordinate)

    def horse_placement(self) -> Callable:
        return horse_func(coordinate=self.coordinate)

    def pawns_placement(self) -> Callable:
        return pawns_func(coordinate=self.coordinate)


enter_figure: str = input(f'Введите фигуру ')
enter_cord: str = input(f'Введите клетку фигуры ')
enter_cord: list = [list(enter_cord)[0], int(list(enter_cord)[1])]

if __name__ == '__main__':
    chess: Chess[str, list] = Chess(figure=enter_figure, coordinate=enter_cord)
    chessmen: dict = {
                        'Q': chess.queen_placement(),
                        'K': chess.king_placement(),
                        'B': chess.bishop_placement(),
                        'R': chess.rooks_placement(),
                        'H': chess.horse_placement(),
                        'P': chess.pawns_placement()
                     }
    print(chessmen[enter_figure])
