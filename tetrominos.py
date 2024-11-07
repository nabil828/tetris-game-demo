import pygame
from colors import Colors
from command import Command


class Tetromino:
    def __init__(self):
        self.state = 0
        self.row_offset = 0
        self.col_offset = 3

    def draw(self, screen, ui_x_offset=0, ui_y_offset=0):
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            (col_index + self.col_offset) * 30 + ui_x_offset,
                            (row_index + self.row_offset) * 30 + ui_y_offset,
                            30 - 1,
                            30 - 1,
                        ),
                    )

    def update(self, command, grid, game):
        def out_of_boundaries():
            for row_index, row in enumerate(self.blocks[self.state]):
                for col_index, block in enumerate(row):
                    if block:
                        if (
                            row_index + self.row_offset > 19
                            or col_index + self.col_offset > 9
                            or col_index + self.col_offset < 0
                        ):
                            return True
            return False

        def check_for_completed_rows_and_clear(grid):
            number_of_cleared_rows = 0
            for row_index, row in enumerate(grid.blocks):
                if all(row):
                    number_of_cleared_rows += 1
                    grid.blocks.pop(row_index)
                    grid.blocks.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            return number_of_cleared_rows

        def lock_tetromino(grid, game):
            """
            carbon copy the tetromino into the grid
            """
            for row_index, row in enumerate(self.blocks[self.state]):
                for col_index, block in enumerate(row):
                    if block:
                        grid.blocks[row_index + self.row_offset][
                            col_index + self.col_offset
                        ] = self.color
            number_of_cleared_rows = check_for_completed_rows_and_clear(grid)
            game.score += number_of_cleared_rows * 100

        def collides_with_other_tetrominos(grid):
            for row_index, row in enumerate(self.blocks[self.state]):
                for col_index, block in enumerate(row):
                    if block:
                        if grid.blocks[row_index + self.row_offset][
                            col_index + self.col_offset
                        ]:
                            return True
            return False

        if command == Command.LEFT:
            self.col_offset -= 1
            if out_of_boundaries():
                self.col_offset += 1
            if collides_with_other_tetrominos(grid):
                self.col_offset += 1

        if command == Command.RIGHT:
            self.col_offset += 1
            if out_of_boundaries():
                self.col_offset -= 1
            if collides_with_other_tetrominos(grid):
                self.col_offset -= 1

        if command == Command.DOWN:
            self.row_offset += 1
            if out_of_boundaries():
                self.row_offset -= 1
                lock_tetromino(grid, game)
                game.spawn_new_tetromino()
                return
            if collides_with_other_tetrominos(grid):
                self.row_offset -= 1
                if self.row_offset == 0:
                    game.game_over = True
                    print("Game Over!")
                lock_tetromino(grid, game)
                game.spawn_new_tetromino()

        if command == Command.UP:
            self.state = (self.state + 1) % len(self.blocks)
            if out_of_boundaries():
                self.state = (self.state - 1) % len(self.blocks)


class ZTetromino(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = Colors.BLUE.value
        self.blocks = [
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0],
            ],
        ]


class JTetromino(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = Colors.RED.value
        self.blocks = [
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0],
            ],
        ]


class TTetromino(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = Colors.CYAN.value
        self.blocks = [
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]


class LTetromino(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = Colors.GREEN.value
        self.blocks = [
            [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0],
            ],
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0],
            ],
        ]


class STetromino(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = Colors.PURPLE.value
        self.blocks = [
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [1, 1, 0],
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]


class OTetromino(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = Colors.YELLOW.value
        self.blocks = [
            [
                [1, 1],
                [1, 1],
            ],
        ]


class ITetromino(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = Colors.ORANGE.value
        self.blocks = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
            ],
        ]
