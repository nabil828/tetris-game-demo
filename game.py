import random
import pygame

from command import Command
from grid import Grid
from tetrominos import *
from ui import UI


class Game:
    def __init__(self):
        pygame.init()
        # Block size of 30px. 10 columns and 20 rows.
        self.screen = pygame.display.set_mode((500, 620))
        self.game_over = False
        self.score = 0

        # objects
        self.grid = Grid()
        self.ui = UI()
        self.tetromino = random.choice(
            [
                ZTetromino(),
                JTetromino(),
                TTetromino(),
                LTetromino(),
                STetromino(),
                OTetromino(),
                ITetromino(),
            ]
        )
        self.next_tetromino = random.choice(
            [
                ZTetromino(),
                JTetromino(),
                TTetromino(),
                LTetromino(),
                STetromino(),
                OTetromino(),
                ITetromino(),
            ]
        )

    def run(self):
        running = True

        MY_CUSTOM_EVENT = pygame.USEREVENT + 1

        # Set a timer to trigger the custom event every 1000 milliseconds (1 second)
        pygame.time.set_timer(MY_CUSTOM_EVENT, 200)  # Interval in ms

        while running:
            command = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_over = False
                        self.__init__()
                    if event.key == pygame.K_LEFT and not self.game_over:
                        command = Command.LEFT
                    if event.key == pygame.K_RIGHT and not self.game_over:
                        command = Command.RIGHT
                    if event.key == pygame.K_DOWN and not self.game_over:
                        command = Command.DOWN
                        self.score += 1
                    if event.key == pygame.K_UP and not self.game_over:
                        command = Command.UP
                if event.type == MY_CUSTOM_EVENT and not self.game_over:
                    command = Command.DOWN

            self.update(command)
            self.draw()

    def update(self, command):
        self.tetromino.update(command, self.grid, self)

    def draw(self):
        self.ui.draw(self.screen, self)
        self.grid.draw(self.screen, 10, 10)
        self.tetromino.draw(self.screen, 10, 10)
        pygame.display.update()

    def spawn_new_tetromino(self):
        self.tetromino = self.next_tetromino
        self.next_tetromino = random.choice(
            [
                ZTetromino(),
                JTetromino(),
                TTetromino(),
                LTetromino(),
                STetromino(),
                OTetromino(),
                ITetromino(),
            ]
        )
