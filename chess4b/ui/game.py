import chess
import pygame

from dataclasses import dataclass


@dataclass
class Square:
    rect: pygame.rect.Rect
    name: str


class GameDisplay:
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.squares: list[Squares] = []

    def show_board(self, board: chess.Board):
        pass

    def highlight(self, field: str, color: tuple[int, int, int] = (255, 165, 0)):
        pass
