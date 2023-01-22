import chess
import pygame


class GameDisplay:
    def __init__(self, screen: pygame.Surface, color: chess.Color):

        self.color: chess.Color = color

        self.screen: pygame.Surface = screen
        self.squares: dict={}

        self.display_field()
        self.setup_squares()

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def setup_squares(self):

        #colors
        turquoise = (52, 78, 91)
        #white = (255, 255, 255)

        X = 1200
        Y = 800
        screen = pygame.display.set_mode([X, Y])
        pygame.display.set_caption('Game Window')
        screen.fill(turquoise)



        color_rect = ('white')
        color_rect_2 = (0, 0, 0)
        font = pygame.font.Font('AGENCYR.ttf', 32)
        TEXT_COL = ('white')
        # Create rects to be able to check if the mouse pointer collides with a field

        var = "ABCDEFGH"
        for num in range(1, 9):
            for char in var:
                a = pygame.Rect(130 + (var.index(char)) * 50, 100 + num * 50 , 50, 50)
                self.squares[f"{num}{char}"] = a



                #checks if field is even or odd | even = white | odd = black

                if num%2:
                    pygame.draw.rect(self.screen, color_rect, a)

                else:
                    pygame.draw.rect(self.screen, color_rect_2, a)

        pass
        print(self.squares)

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
