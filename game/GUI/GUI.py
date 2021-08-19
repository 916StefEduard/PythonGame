import pygame
from Board.Board import Board
from Player.Player import Player
from Circle.Circle import Circle
from AI.AI import AI
import math
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE=(255,255,255)
GRAY=(127,127,127)

class GUI:

    def draw_game(self,screen, Human,Computer,board, SQUARESIZE):
        RADIUS = int(SQUARESIZE / 2 - 5)
        for cols in range(7):
            for rows in range(6):
                pygame.draw.rect(screen, BLACK, (cols * SQUARESIZE, rows * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                if board.get_move(rows,cols) == '⬤':
                    pygame.draw.circle(screen, GRAY, (
                    int(cols * SQUARESIZE + SQUARESIZE / 2), int(rows * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board.get_move(rows,cols) == Human.get_circle():
                    pygame.draw.circle(screen, RED, (
                    int(cols * SQUARESIZE + SQUARESIZE / 2), int(rows * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board.get_move(rows,cols) ==Computer.get_circle():
                    pygame.draw.circle(screen, YELLOW, (
                    int(cols * SQUARESIZE + SQUARESIZE / 2), int(rows * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    def create_gui(self):
        board = Board()
        first_circle = Circle('red')
        second_circle = Circle('blue')
        human_turn=1
        Human=Player(first_circle)
        Computer = AI(second_circle, first_circle, 4)
        pygame.init()
        SQUARESIZE = 100
        width = 7 * SQUARESIZE
        height = 7 * SQUARESIZE
        RADIUS = int(SQUARESIZE / 2 - 5)
        size = (width, height)
        screen = pygame.display.set_mode(size)
        self.draw_game(screen,Human,Computer,board, SQUARESIZE)
        pygame.display.update()
        font = pygame.font.SysFont("monospace", 40)
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if human_turn == 1:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        posx = event.pos[0]
                        if human_turn == 1:
                            col = int(math.floor(posx / SQUARESIZE))
                            board.move(int(col),Human.get_circle())
                            self.draw_game(screen,Human,Computer, board, SQUARESIZE)
                        else:
                            col = int(Computer.search_move(board))
                            board.move(int(col),Computer.get_circle())
                            self.draw_game(screen,Human,Computer, board, SQUARESIZE)
                        if board.is_game_won()==True:
                            done=True
                        if board.is_game_draw()==True:
                            done = True
                        human_turn=(-1)*human_turn

