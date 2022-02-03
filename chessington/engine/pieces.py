"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)
        row = current_square.row
        column = current_square.col
        moves = []

        if self.player == Player.WHITE:
            if row == 1:   
                moves.append(Square((row + 2), column))
            moves.append(Square((row + 1), column))

            if row == 7:
                return []

            diagonal_left = Square(row +1, column - 1)
            diagonal_right = Square(row + 1, column + 1)

            if board.get_piece(diagonal_right) != None:
            if board.get_piece(diagonal_right) == Pawn(Player.BLACK):    
                moves.append(diagonal_right)

            if board.get_piece(diagonal_left) != None:
                moves.append(diagonal_left)

            row_check = row + 1
            square_check = Square(row_check, column)
            if board.get_piece(square_check) != None:
                return []

        else:
            if row == 6:
                moves.append(Square((row - 2), column))
            moves.append(Square((row - 1), column))

            if row == 0:
                return []

            diagonal_left = Square(row - 1, column - 1)
            diagonal_right = Square(row - 1, column + 1)

            if board.get_piece(diagonal_right) != None:
                moves.append(diagonal_right)

            if board.get_piece(diagonal_left) != None:
                moves.append(diagonal_left)

            row_check = row - 1
            square_check = Square(row_check, column)
            if board.get_piece(square_check) != None:
                return []
        return moves

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []