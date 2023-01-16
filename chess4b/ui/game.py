import chess
import pygame


class GameDisplay:
    def __init__(self, screen: pygame.Surface, color: chess.Color):

        self.color: chess.Color = color

        self.screen: pygame.Surface = screen
        self.squares: list[list] = []

        self.display_field()
        self.setup_squares()

    def setup_squares(self):
        # Create rects to be able to check if the mouse pointer collides with a field
        pass

    def display_field(self):
        # Display the playing field including the text
        pass

    def show_board(self, board: chess.Board):
        # Display the board onto the field
        # Also mark if it's the player turn
        pass

    def highlight(self, field: str, color: tuple[int, int, int] = (255, 165, 0)):
        # Highlight a field with an orange border
        pass

    def arrow(self, start: str, end: str, color: tuple[int, int, int] = (255, 165, 0)):
        # Draw a line from one field to another
        pass
