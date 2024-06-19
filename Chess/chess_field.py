from string import ascii_lowercase as alphabet
def chess_field(chess_board: list, line: int) -> list:
    """
    Рекурсивное создание шахматного поля вида [точки, координата точки]
    Recursively creating a chessboard [points, point coordinates]
    """
    if line > 8:
        return chess_board
    chess_board.append([['.', [alphabet[j], line]] for j in range(8)])
    line += 1
    return chess_field(chess_board, line)
