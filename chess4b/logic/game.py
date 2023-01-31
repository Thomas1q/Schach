import sys
import pickle
import chess
import pygame

from chess4b.logic import BaseLogic
from chess4b.models import User
from chess4b.network import Server, Client
from chess4b.ui.game import *
from chess4b.Sound.Sounds import move_sound, sieg_sound


class GameLogic(BaseLogic):
    def __init__(self, host: bool, user_data: User, enemy_data: User, network: Server | Client,
                 screen: pygame.Surface = None, clock: pygame.time.Clock = None):

        self.network: Server | Client = network

        self.user_data: User = user_data
        self.enemy_data: User = enemy_data

        if host:
            self.color: chess.Color = chess.WHITE
            self.board: chess.Board | None = chess.Board()
            self.game_display = GameDisplay(screen, self.color)
        else:
            self.color: chess.Color = chess.BLACK
            self.board: chess.Board | None = None
            self.game_display = GameDisplay(screen, self.color)

        self.selected: str | None = None
        self.move_to: str | None = None
        self.just_moved: bool = False

        self.finished: bool = False

        super().__init__(screen, clock)

    def start_game_loop(self):
        # Send the board to the other player or receive it if you have no board
        if self.board:
            self.network.write(pickle.dumps(self.board))
        else:
            self.board = pickle.loads(self.network.recv())

        # Run the game loop
        while True:
            events = pygame.event.get()
            self.screen.fill((255, 255, 255))

            # Display the board
            self.display_board()

            # Get back to the HostLogic or ClientLogic if the game is finished
            if self.finished:
                return

            # Resolve the move according to the events
            self.get_move(events)

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

    def display_board(self):
        # When a new game is started the other player might send True to indicate that he wants to play again
        if isinstance(self.board, bool):
            self.network.write(pickle.dumps(True))
            self.board = pickle.loads(self.network.recv())
            return
        # Do not send the because it gets send when a move is done
        if self.board.turn == self.color or self.just_moved is True:
            if self.just_moved is True:
                self.just_moved = False
            if self.color:
                # Send a copy of the board to the other player
                board = chess.Board(self.board.fen())
                self.network.write(pickle.dumps(board))
            else:
                self.network.write(pickle.dumps(self.board))
        else:
            try:
                # Load the board from the other player
                data: chess.Board = pickle.loads(self.network.recv())
                if isinstance(data, bool):
                    return
                # Update self.board only if something changed
                if str(data) != str(self.board):
                    move_sound()
                    if self.color:
                        last_move = data.move_stack.pop()
                        self.board.push(last_move)
                    else:
                        self.board = data
            # Raises when an invalid data is received
            except pickle.UnpicklingError:
                pass
            # Raises when the data cant be decoded
            except UnicodeDecodeError:
                pass
        # Display the board
        self.game_display.show_board(self.board)

    def get_move(self, events: list[pygame.event.Event]):
        # When a new game is started the other player might send True to indicate that he wants to play again
        if isinstance(self.board, bool):
            return
        # When there are no legal moves left the game is finished
        click = False
        if self.board.legal_moves.count() == 0:
            self.finished = True
            sieg_sound()
            return

        # Only get the move if it is your turn
        if self.board.turn == self.color:
            # Display some information on the GUI
            if self.selected:
                self.game_display.highlight(self.selected)
            if self.move_to:
                self.game_display.highlight(self.move_to)
            if self.selected and self.move_to:
                self.game_display.arrow(self.selected, self.move_to)
            if self.board.is_check():
                self.game_display.show_check(
                    chess.SQUARE_NAMES[self.board.king(self.color)],
                    [chess.SQUARE_NAMES[square] for square in self.board.checkers()]
                )

            # Update click variable when the mouse is pressed
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    click = False

            # Check all the squares if they are clicked
            pointer = pygame.mouse.get_pos()
            for square in self.game_display.squares:
                # mouse hovers
                if self.game_display.squares.get(square)[0].collidepoint(pointer):
                    if click:
                        # When you click your piece it gets selected
                        if self.my_piece(square):
                            self.selected = square
                            self.move_to = None
                        # When you click an empty field the square gets highlighted
                        if self.empty_field(square):
                            if self.selected:
                                # When there is already a piece selected and you click a empty field the second time
                                # the piece gets moved to the field if it is legal
                                if self.move_to:
                                    if square == self.move_to:
                                        move = chess.Move.from_uci(f"{self.selected}{self.move_to}")
                                        if self.board.is_legal(move):
                                            self.board.push(move)
                                            self.selected = None
                                            self.move_to = None
                                            # self.network.write(pickle.dumps(self.board))
                                            self.just_moved = True
                                            move_sound()
                                    else:
                                        move = chess.Move.from_uci(f"{self.selected}{square}")
                                        if self.board.is_legal(move):
                                            self.move_to = square
                                else:
                                    move = chess.Move.from_uci(f"{self.selected}{square}")
                                    if self.board.is_legal(move):
                                        self.move_to = square
                        # Check if you want to throw a piece from the enemy
                        elif self.other_piece(square):
                            if self.selected:
                                if self.move_to:
                                    # Check if legal
                                    if square == self.move_to:
                                        move = chess.Move.from_uci(f"{self.selected}{square}")
                                        if self.board.is_legal(move):
                                            self.board.push(move)
                                            self.selected = None
                                            self.move_to = None
                                            self.just_moved = True
                                    else:
                                        move = chess.Move.from_uci(f"{self.selected}{self.move_to}")
                                        if self.board.is_legal(move):
                                            self.move_to = square
                                else:
                                    move = chess.Move.from_uci(f"{self.selected}{square}")
                                    if self.board.is_legal(move):
                                        self.move_to = square

    def my_piece(self, field: str) -> bool:
        # Check if the piece on the field is yours
        square = self.board.piece_at(chess.parse_square(field))
        if square:
            if square.color is self.color:
                return True
        return False

    def empty_field(self, field: str) -> bool:
        # Check if the field is empty
        square = self.board.piece_at(chess.parse_square(field))
        return False if square else True

    def other_piece(self, field: str) -> bool:
        # Check if the piece on the field is from the other player
        square = self.board.piece_at(chess.parse_square(field))
        if square:
            if square.color is not self.color:
                return True
        return False

    @classmethod
    def from_client(cls, obj):
        # Create a new object from the ClientLogic class
        return cls(
            False,
            obj.user_data, obj.enemy_data,
            obj.client,
            obj.screen, obj.clock
        )

    @classmethod
    def from_host(cls, obj):
        # Create a new object from the HostLogic class
        return cls(
            True,
            obj.user_data, obj.enemy_data,
            obj.server,
            obj.screen, obj.clock
        )
