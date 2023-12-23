"""
Driver file. Responsible for handling user input and displaying the current GameState object
"""


import pygame as p

from ChessAI import ChessEngine

WIDTH = HEIGHT = 512 # or 400
DIMENSION = 8 #Dimension of a chess board 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animation
IMAGES = {}

'''
Initialize a global dictionary of images. Will be called exactly once in the main.
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES [piece] = p.image.load("images/" + piece + ".png")
    #We can access an image by saying 'IMAGES['wp']'
        
'''
Main driver. Handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() #only do this once
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGamestate(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
Responsible for all the graphics within a current game state
'''

def drawGamestate(screen, gs):
    drawBoard(screen) #draw squares on the board
    drawPieces(screen, gs.board)#drams pieces on top of those squares

'''
Draw the squares on the board.
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the pieces on the board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()