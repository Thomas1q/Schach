import chess
import pygame
import chess4b.ui.gui_buttons as gui_buttons


class GameDisplay:

    def __init__(self, screen: pygame.Surface, color: chess.Color):

        self.color: chess.Color = color
        self.font = pygame.font.Font('AGENCYR.ttf', 32)
        self.text_col = 'white'
        self.turquoise = (52, 78, 91)

        self.screen: pygame.Surface = screen
        self.squares: dict={}

        self.display_field()
        self.setup_squares()

    def setup_squares(self):






        # Create rects to be able to check if the mouse pointer collides with a field
        color_rect = (248, 239, 221)
        color_rect_2 = (95, 59, 47)
        var = "ABCDEFGH"
        for num in range(1, 9):
            for char in var:
                a = pygame.Rect(200 + (var.index(char)) * 75, 100 + num * 75, 75, 75)
                if (num + (var.index(char))) % 2:

                    self.squares[f"{num}{char}"] = [a, color_rect]

                else:
                    self.squares[f"{num}{char}"] = [a, color_rect_2]


        pass
        print(self.squares)

    def display_field(self):

        # colors
        turquoise = (52, 78, 91)

        X = 1200
        Y = 800
        self.screen = pygame.display.set_mode([X, Y])
        pygame.display.set_caption('Game Window')
        self.screen.fill(turquoise)


        pygame.draw.rect(self.screen, 'black', pygame.Rect(196, 171, 608, 608),4)

        img = self.font.render("PRESS ESC TO PAUSE", True, self.text_col)
        self.screen.blit(img, (500, 750))

        # Display the playing field including the text
        for i in range(1, 9):
            if self.color:
                text = 'ABCDEFGH'

                img = self.font.render(text, True, self.text_col)
                self.screen.blit(img, (i * 50 + 150, 50))
            else:
                text_r = 'HGFEDCBA'

                img = self.font.render(text_r, True, self.text_col)
                x = (i * (-50)) + 900
                self.screen.blit(img, (x, 50))

        # checks if field is even or odd | even = white | odd = black

        for square in self.squares:

            pygame.draw.rect(self.screen, self.squares.get(square)[1], self.squares.get(square)[0])

        pass

    def show_board(self, board: chess.Board):
        # Display the board onto the field
        # Also mark if it's the player turn
        self.display_field()
        black_pawn = pygame.image.load("chess4b/ui/images/black_pawn.png").convert_alpha()
        black_queen = pygame.image.load("chess4b/ui/images/black_queen.png").convert_alpha()
        black_king = pygame.image.load("chess4b/ui/images/black_king.png").convert_alpha()
        black_bishop = pygame.image.load("chess4b/ui/images/black_bishop.png").convert_alpha()
        black_knight = pygame.image.load("chess4b/ui/images/black_knight.png").convert_alpha()
        black_rook = pygame.image.load("chess4b/ui/images/black_rook.png").convert_alpha()

        white_pawn = pygame.image.load("chess4b/ui/images/white_pawn.png").convert_alpha()
        white_queen = pygame.image.load("chess4b/ui/images/white_queen.png").convert_alpha()
        white_king = pygame.image.load("chess4b/ui/images/white_king.png").convert_alpha()
        white_bishop = pygame.image.load("chess4b/ui/images/white_bishop.png").convert_alpha()
        white_knight = pygame.image.load("chess4b/ui/images/white_knight.png").convert_alpha()
        white_rook = pygame.image.load("chess4b/ui/images/white_rook.png").convert_alpha()

        black_pawn_button = gui_buttons.Button(500, 200, black_pawn, 1)
        black_queen_button = gui_buttons.Button(125, 200, black_queen, 1)
        black_king_button = gui_buttons.Button(157, 400, black_king, 1)
        black_bishop_button = gui_buttons.Button(175, 500, black_bishop, 1)
        black_knight_button = gui_buttons.Button(157, 400, black_knight, 1)
        black_rook_button = gui_buttons.Button(157, 400, black_rook, 1)

        white_pawn_button = gui_buttons.Button(500, 200, white_pawn, 1)
        white_queen_button = gui_buttons.Button(125, 200, white_queen, 1)
        white_king_button = gui_buttons.Button(157, 400, white_king, 1)
        white_bishop_button = gui_buttons.Button(175, 500, white_bishop, 1)
        white_knight_button = gui_buttons.Button(157, 400, white_knight, 1)
        white_rook_button = gui_buttons.Button(157, 400, white_rook, 1)



        pass

    def highlight(self, field: str, color: tuple = (255, 165, 0)):
        # Highlight a field with an orange border
        pass

    def arrow(self, start: str, end: str, color: tuple = (255, 165, 0)):
        # Draw a line from one field to another
        pass
