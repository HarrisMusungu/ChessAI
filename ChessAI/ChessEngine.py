"""
Responsible for stonring all the information about the current state of a chess game. Also responsible for determining the valid moves at the current state. Also keep a move log.
"""
class GameState():
    def __init__(self):
        # board is a 8x8 2d list, each element of the list has 2 characters.
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
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.moveFunction = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves, 'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}

        self.whiteToMove = True
        self.movelog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.movelog.append(move)
        self.whiteToMove = not self.whiteToMove # swap players

    def undoMove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteTomove = not self.whiteToMove

    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    '''
    All moves without considering checks
    '''
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): #number of columns
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunction[piece](r, c, moves)
        return moves

    '''
    Get all the pawn moves for the pawn located at row, col and add these moves to the list
    '''
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove: #white pawn moves
            if self.board[r-1][c] == "--": #one square advance
                moves.append(Move((r,c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--": #Two square pawn move
                    moves.append(Move((r,c), (r-2, c), self.board))
            if c-1 >= 0: #Capture on the left
                if self.board[r-1][c-1][0] == 'b': #enemy piece to capture
                    moves.append(Move((r,c), (r-1, c-1), self.board))
            if c+1 <= 7: #captures on the right
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r,c), (r-1, c+1), self.board))
        else: #black pawn moves
            if not self.whiteToMove:
                if self.board[r + 1][c] == "--":
                    moves.append(Move((r, c), (r+1, c), self.board))
                    if r == 1 and self.board[r+2][c] == "--":
                        moves.append(Move((r, c), (r+2, c), self.board))
                    if c - 1 >= 0:
                        if self.board[r+1][c-1][0] == 'w':
                            moves.append(Move((r, c), (r+1, c-1), self.board))
                        if c+1 <= 7:
                            if self.board[r+1][c+1][0] == 'w':
                                moves.append(Move((r, c), (r+1, c+1), self.board))
    '''
    Get all the rook moves for the pawn located at row, col and add these moves to the list
    '''
    def getRookMoves(self, r, c, moves):
        pass
    '''
   Get all the knight moves for the pawn located at row, col and add these moves to the list
   '''
    def getKnightMoves(self, r, c, moves):
        pass
    '''
   Get all the bishop moves for the pawn located at row, col and add these moves to the list
   '''
    def getBishopMoves(self, r, c, moves):
        pass
    '''
   Get all the queen moves for the pawn located at row, col and add these moves to the list
   '''
    def getQueenMoves(self, r, c, moves):
        pass
    '''
   Get all the king moves for the pawn located at row, col and add these moves to the list
   '''
    def getKingMoves(self, r, c, moves):
        pass

class Move():

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    '''
    Overriding the equals method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
        