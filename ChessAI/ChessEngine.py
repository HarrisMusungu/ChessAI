"""
Responsible for stonring all the information about the current state of a chess game. Also responsible for determining the valid moves at the current state. Also keep a move log.
"""
class GameState():
    def __init__(self):
        # board is an 8x8 2d list, each element of the list has 2 characters.
        # The first character represents the color if the piece, b for black and w for white.
        # The second character represents the type of the piece, p for pawn, r for rook, n for knight,etc.
        # "--" represents an empty space with no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],]
        self.whiteToMove = True
        self.movelog = []
        