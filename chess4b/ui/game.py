import chess
import pygame

from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (132, 123, 254)
    ORANGE = (255, 165, 0)


@dataclass
class Square:
    rect: pygame.rect.Rect
    name: str
    col: Color
    # piece: str | None

    def __repr__(self):
        return f"{self.name}(x={self.rect.x}, y={self.rect.y})"


class GameDisplay:
    def __init__(self, screen: pygame.Surface, color: chess.Color):
        self.LETTERS = "abcdefgh"
        self.REVERSED_LETTERS = "hgfedcba"

        self.color: bool = color

        self.screen: pygame.Surface = screen
        self.squares: list[list[Squares]] = []

        self.setup_squares()
        self.show_squares()
        self.show_text()

    def setup_squares(self):
        x_start = 100
        y_start = 725
        x = y = 0
        step = 100
        for num in range(1, 8 + 1):
            y = y_start - (step * (num - 1))
            self.squares.append([])
            for ind, letter in enumerate(self.LETTERS):
                x = x_start + (step * ind)
                col = [Color.WHITE if (ind + num) % 2 == 0 else Color.BLACK][0]
                if self.color:
                    letter = self.REVERSED_LETTERS[self.LETTERS.index(letter)]
                    n = 9 - num
                else:
                    n = num
                self.squares[num - 1].append(Square(pygame.Rect(x, y, 100, 100), f"{letter}{n}", col))

        print("\n".join(map(str, self.squares)))

    def show_squares(self):
        self.screen.fill(Color.GREEN.value)
        for row_num, row in enumerate(self.squares, 1):
            for col_num, square in enumerate(row, 1):
                pygame.draw.rect(self.screen, square.col.value, square.rect)
                text = pygame.font.Font(None, 50).render(square.name, True, Color.GREEN.value)
                self.screen.blit(text, text.get_rect(center=square.rect.center))

    def show_text(self):
        for num in range(8, 1 - 1, -1):
            rects = [pygame.Rect(75, 25 + 100 * (8 - num), 25, 100), pygame.Rect(900, 25 + 100 * (8 - num), 25, 100)]
            for rect in rects:
                if self.color:
                    n = 9 - num
                else:
                    n = num
                text = pygame.font.Font(None, 20).render(str(n), True, Color.BLACK.value)
                self.screen.blit(text, text.get_rect(center=rect.center))

        for ind, letter in enumerate(self.REVERSED_LETTERS if self.color else self.LETTERS):
            rects = [pygame.Rect(100 * (ind + 1), 0, 100, 25), pygame.Rect(100 * (ind + 1), 825, 100, 25)]
            for rect in rects:
                text = pygame.font.Font(None, 20).render(letter, True, Color.BLACK.value)
                self.screen.blit(text, text.get_rect(center=rect.center))

    def show_board(self, board: chess.Board):
        self.show_squares()
        self.show_text()
        self.your_turn(board)
        print(self.board_list(board))

    def your_turn(self, board: chess.Board):
        if board.turn == self.color:
            rect = pygame.Rect(0, 0, 1000, 850)
            pygame.draw.rect(self.screen, Color.ORANGE.value, rect, 5)

    def highlight(self, field: str, color: tuple[int, int, int] = Color.ORANGE.value):
        square = self.to_square(field)
        pygame.draw.rect(self.screen, color, square.rect, 5)

    def arrow(self, start: str, end: str, color: tuple[int, int, int] = Color.ORANGE.value):
        start_square = self.to_square(start)
        end_square = self.to_square(end)
        pygame.draw.line(self.screen, color,  start_square.rect.center, end_square.rect.center, width=5)

    def list_coords(self, field: str):
        if self.color:
            return int(field[1]) - 1, self.REVERSED_LETTERS.index(field[0])
        else:
            return int(field[1]) - 1, self.LETTERS.index(field[0])

    def to_square(self, field: str):
        x, y = self.list_coords(field)
        row = [row for row in self.squares if row[0].name.endswith(field[1])][0]
        square = [square for square in row if square.name.startswith(field[0])][0]
        return square

    def board_list(self, board: chess.Board):
        if self.color:
            return [row.split(" ") for row in str(board).split("\n")]
        else:
            rows = str(board).split("\n")
            rows.reverse()
            cols = rows.split(" ")
            cols.reverse()
            return cols
