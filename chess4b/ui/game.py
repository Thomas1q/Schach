import chess
import pygame


class GameDisplay:
    def __init__(self, screen: pygame.Surface, color: chess.Color):

        self.color: chess.Color = color
        self.font = pygame.font.Font('AGENCYR.ttf', 32)
        self.text_col = 'white'

        self.screen: pygame.Surface = screen
        self.squares: dict={}

        self.display_field()
        self.setup_squares()

    def setup_squares(self):

        #colors
        turquoise = (52, 78, 91)
        white = (255, 255, 255)

        X = 1200
        Y = 800
        screen = pygame.display.set_mode([X, Y])
        pygame.display.set_caption('Game Window')
        screen.fill(turquoise)




        # Create rects to be able to check if the mouse pointer collides with a field

        var = "ABCDEFGH"
        for num in range(1, 9):
            for char in var:
                a = pygame.Rect(130 + (var.index(char)) * 50, 100 + num * 50, 50, 50)
                self.squares[f"{num}{char}"] = a

        pass
        print(self.squares)

    def display_field(self):

        img = self.font.render("PRESS ESC TO PAUSE", True, self.text_col)
        self.screen.blit(img, (500, 750))

        # Display the playing field including the text
        for i in range (1,9):
            if self.color:
                text = 'ABCDEFGH'

                img = self.font.render(text, True, self.text_col)
                self.screen.blit(img, (i * 50 + 150, 50))
            else:
                text_r = 'HGFEDCBA'

                img = self.font.render(text_r, True, self.text_col)
                x = (i * (-50)) + 900
                self.screen.blit(img, (x, 50))
        color_rect = 'white'
        color_rect_2 = 'black'

        # checks if field is even or odd | even = white | odd = black

        for num in range(1, 8 + 1):
            if num % 2:
                pygame.draw.rect(self.screen, color_rect, self.squares)

            else:
                pygame.draw.rect(self.screen, color_rect_2, self.squares)

        pass

    def show_board(self, board: chess.Board):
        # Display the board onto the field
        # Also mark if it's the player turn



        pass

    def highlight(self, field: str, color: tuple = (255, 165, 0)):
        # Highlight a field with an orange border
        pass

    def arrow(self, start: str, end: str, color: tuple = (255, 165, 0)):
        # Draw a line from one field to another
        pass
