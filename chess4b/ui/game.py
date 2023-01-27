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

        if self.color:

            var = "abcdefgh"
            rng = range(1, 9)

        else:

            var = "hgfedcba"
            rng = range(8, 0, -1)

        for num in rng:
            for char in var:
                a = pygame.Rect(300 + (var.index(char)) * 75, 50 + num * 75, 75, 75)
                if (num + (var.index(char))) % 2:

                    self.squares[f"{char}{num}"] = [a, color_rect]
                else:
                    self.squares[f"{char}{num}"] = [a, color_rect_2]

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
        temp_2 = '12345678'
        temp = '87654321'

        counter = 0
        counter_2 = 0

        if self.color:
            for char in text:
                img = self.font.render(char, True, self.text_col_2)
                self.screen.blit(img, (counter * 75 + 330, 75))
                counter = counter + 1

            for number in temp:
                img_2 = self.font.render(number, True, self.text_col_2)
                self.screen.blit(img_2, (260, counter_2 * 75 + 140))
                counter_2 = counter_2 + 1
        else:
            for char in text_r:
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

        size = (60, 60)

        black_pawn = pygame.transform.scale(black_pawn, size)
        black_queen = pygame.transform.scale(black_queen, size)
        black_king = pygame.transform.scale(black_king, size)
        black_bishop = pygame.transform.scale(black_bishop, size)
        black_knight = pygame.transform.scale(black_knight, size)
        black_rook = pygame.transform.scale(black_rook, size)

        white_pawn = pygame.transform.scale(white_pawn, size)
        white_queen = pygame.transform.scale(white_queen, size)
        white_king = pygame.transform.scale(white_king, size)
        white_bishop = pygame.transform.scale(white_bishop, size)
        white_knight = pygame.transform.scale(white_knight, size)
        white_rook = pygame.transform.scale(white_rook, size)

        """""""""
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
        """""""""

        for square, names in zip(chess.SQUARES, chess.SQUARE_NAMES):
            #print(names, board.piece_at(square))

            command = board.piece_at(square)
            if command:
                if command.color:
                    match chess.piece_symbol(command.piece_type):

                        case 'p':

                            self.screen.blit(white_pawn, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'q':

                            self.screen.blit(white_queen, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'k':

                            self.screen.blit(white_king, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'b':

                            self.screen.blit(white_bishop, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'n':

                            self.screen.blit(white_knight, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'r':

                            self.screen.blit(white_rook, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                else:

                    match chess.piece_symbol(command.piece_type):

                        case 'p':

                            self.screen.blit(black_pawn, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'q':

                            self.screen.blit(black_queen, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'k':

                            self.screen.blit(black_king, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'b':

                            self.screen.blit(black_bishop, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'n':

                            self.screen.blit(black_knight, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                        case 'r':

                            self.screen.blit(black_rook, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

        pass

    def highlight(self, field: str, color: tuple = (217, 134, 58)):
        # Highlight a field with an orange border
        rect_h = self.squares.get(field)[0]
        pygame.draw.rect(self.screen, color, rect_h, 4)

        pass

    def arrow(self, start: str, end: str, color: tuple = (217, 134, 58)):
        # Draw a line from one field to another
        rect_as = self.squares.get(start)[0].center
        rect_ae = self.squares.get(end)[0].center
        pygame.draw.line(self.screen, color, rect_as, rect_ae, 4)
        pass

    def show_check(self, field: str, checker: list[str]):
        # Display if you are in check and the position of your king
        # Show the fields of the checkers
        pass
