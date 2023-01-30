import chess
import pygame
import chess4b.ui.gui_buttons as gui_buttons


class GameDisplay:

    def __init__(self, screen: pygame.Surface, color: chess.Color):
        self.white_king = None
        self.white_bishop = None
        self.white_knight = None
        self.white_rook = None
        self.white_queen = None
        self.white_pawn = None
        self.black_rook = None
        self.black_knight = None
        self.black_bishop = None
        self.black_king = None
        self.black_queen = None
        self.black_pawn = None

        self.color: chess.Color = color
        self.font = pygame.font.Font('AGENCYR.ttf', 32)
        self.text_col = 'white'
        self.text_col_2 = (248, 239, 221)
        self.turquoise = (52, 78, 91)

        self.screen: pygame.Surface = screen
        self.squares: dict = {}

        self.setup_pieces()
        self.display_field()
        self.setup_squares()

    def setup_pieces(self):
        size = (60, 60)

        self.black_pawn = pygame.transform.scale(pygame.image.load("chess4b/ui/images/black_pawn.png").convert_alpha(), size)
        self.black_queen = pygame.transform.scale(pygame.image.load("chess4b/ui/images/black_queen.png").convert_alpha(), size)
        self.black_king = pygame.transform.scale(pygame.image.load("chess4b/ui/images/black_king.png").convert_alpha(), size)
        self.black_bishop = pygame.transform.scale(pygame.image.load("chess4b/ui/images/black_bishop.png").convert_alpha(), size)
        self.black_knight = pygame.transform.scale(pygame.image.load("chess4b/ui/images/black_knight.png").convert_alpha(), size)
        self.black_rook = pygame.transform.scale(pygame.image.load("chess4b/ui/images/black_rook.png").convert_alpha(), size)

        self.white_pawn = pygame.transform.scale(pygame.image.load("chess4b/ui/images/white_pawn.png").convert_alpha(), size)
        self.white_queen = pygame.transform.scale(pygame.image.load("chess4b/ui/images/white_queen.png").convert_alpha(), size)
        self.white_king = pygame.transform.scale(pygame.image.load("chess4b/ui/images/white_king.png").convert_alpha(), size)
        self.white_bishop = pygame.transform.scale(pygame.image.load("chess4b/ui/images/white_bishop.png").convert_alpha(), size)
        self.white_knight = pygame.transform.scale(pygame.image.load("chess4b/ui/images/white_knight.png").convert_alpha(), size)
        self.white_rook = pygame.transform.scale(pygame.image.load("chess4b/ui/images/white_rook.png").convert_alpha(), size)

    def setup_squares(self):

        # Create rects to be able to check if the mouse pointer collides with a field

        color_rect = (248, 239, 221)
        color_rect_2 = (95, 59, 47)

        if self.color:
            var = "abcdefgh"
            rng = range(8, 0, -1)

        else:
            var = "hgfedcba"
            rng = range(1, 9)

        for ind, num in enumerate(rng, start=1):
            for char in var:
                a = pygame.Rect(300 + (var.index(char)) * 75, 50 + ind * 75, 75, 75)
                if (ind + (var.index(char))) % 2:
                    self.squares[f"{char}{num}"] = [a, color_rect]
                else:
                    self.squares[f"{char}{num}"] = [a, color_rect_2]

    def display_field(self):
        # colors
        turquoise = (52, 78, 91)

        X = 1200
        Y = 800
        self.screen = pygame.display.set_mode([X, Y])
        pygame.display.set_caption('Game Window')
        self.screen.fill(turquoise)

        pygame.draw.rect(self.screen, 'black', pygame.Rect(296, 121, 608, 608),4)

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

        # Display all squares
        for square in self.squares:
            pygame.draw.rect(self.screen, self.squares.get(square)[1], self.squares.get(square)[0])

    def show_board(self, board: chess.Board):
        # Display the board onto the field
        # Also mark if it's the player turn
        self.display_field()

        if board.turn:
            img = self.font.render("WHITES TURN", True, self.text_col_2)
            self.screen.blit(img, (530, 750))

        else:
            img = self.font.render("BLACKS TURN", True, self.text_col_2)
            self.screen.blit(img, (530, 750))

        for square, names in zip(chess.SQUARES, chess.SQUARE_NAMES):
            command = board.piece_at(square)
            if command:
                if command.color:
                    match chess.piece_symbol(command.piece_type):
                        case 'p':
                            self.screen.blit(self.white_pawn, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'q':
                            self.screen.blit(self.white_queen, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'k':
                            self.screen.blit(self.white_king, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'b':
                            self.screen.blit(self.white_bishop, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'n':
                            self.screen.blit(self.white_knight, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'r':
                            self.screen.blit(self.white_rook, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

                else:
                    match chess.piece_symbol(command.piece_type):
                        case 'p':
                            self.screen.blit(self.black_pawn, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'q':
                            self.screen.blit(self.black_queen, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'k':
                            self.screen.blit(self.black_king, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'b':
                            self.screen.blit(self.black_bishop, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'n':
                            self.screen.blit(self.black_knight, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))
                        case 'r':
                            self.screen.blit(self.black_rook, tuple(map(lambda x: x+7.5, list(self.squares.get(names)[0].topleft))))

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
        red = (255, 64, 64)

        rect_c = self.squares.get(field)[0]
        pygame.draw.rect(self.screen, red, rect_c, 4)

        for check in checker:
            self.highlight(check, red)
            self.arrow(field, check, red)

        pass
