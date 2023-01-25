import chess
import pygame
import chess4b.ui.gui_buttons as gui_buttons


class GameDisplay:

    def __init__(self, screen: pygame.Surface, color: chess.Color):

        self.color: chess.Color = color
        self.font = pygame.font.Font('AGENCYR.ttf', 32)
        self.text_col = 'white'
        self.text_col_2 = (248, 239, 221)
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
                a = pygame.Rect(300 + (var.index(char)) * 75, 50 + num * 75, 75, 75)
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


        pygame.draw.rect(self.screen, 'black', pygame.Rect(296, 121, 608, 608),4)

        img = self.font.render("PRESS ESC TO PAUSE", True, self.text_col)
        self.screen.blit(img, (500, 750))

        # Display the playing field including the text

        text = 'ABCDEFGH'
        text_r = 'HGFEDCBA'
        temp = '12345678'
        temp_2 = '87654321'

        counter = 0
        counter_2 = 0

        if self.color:
            for char in text:
                text_w = "WHITES TURN"
                text_img = self.font.render(text_w, True, self.text_col)
                self.screen.blit(text_img, (545, 25))
                img = self.font.render(char, True, self.text_col_2)
                self.screen.blit(img, (counter * 75 + 330, 75))
                counter = counter + 1

            for number in temp:
                img_2 = self.font.render(number, True, self.text_col_2)
                self.screen.blit(img_2, (260, counter_2 * 75 + 140))
                counter_2 = counter_2 + 1
        else:
            for char in text_r:
                text_w = "BLACKS TURN"
                text_img = self.font.render(text_w, True, self.text_col)
                self.screen.blit(text_img, (545, 25))
                img = self.font.render(char, True, self.text_col_2)
                self.screen.blit(img, (counter * 75 + 330, 75))
                counter = counter + 1
            for number in temp_2:
                img_2 = self.font.render(number, True, self.text_col_2)
                self.screen.blit(img_2, (260, counter_2 * 75 + 140))
                counter_2 = counter_2 + 1

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

        black_pawn_buttons = []

        for i in range(0, 8):

            black_pawn_buttons.append(gui_buttons.Button(314 + i * 75, 207, black_pawn, 0.25))

        white_pawn_buttons = []

        for i in range(0, 8):

            white_pawn_buttons.append(gui_buttons.Button(314 + i * 75, 582, white_pawn, 0.25))

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

        if self.color:

            for btn in black_pawn_buttons:
                btn.draw(self.screen)

            for wtn in white_pawn_buttons:
                wtn.draw(self.screen)



        else:





            pass

    def highlight(self, field: str, color: tuple = (255, 165, 0)):
        # Highlight a field with an orange border
        pass

    def arrow(self, start: str, end: str, color: tuple = (255, 165, 0)):
        # Draw a line from one field to another
        pass
