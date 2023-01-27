import sys
import pickle
import chess
import pygame

from chess4b.logic import BaseLogic
from chess4b.models import User
from chess4b.network import Server, Client
from chess4b.ui.game import *


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

        super().__init__(screen, clock)

    def start_game_loop(self):
        if self.board:
            self.network.write(pickle.dumps(self.board))
        else:
            self.board = pickle.loads(self.network.recv())
        while True:
            events = pygame.event.get()
            self.screen.fill((255, 255, 255))

            self.display_board()

            self.get_move(events)

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

    def display_board(self):
        if self.board.turn == self.color:
            if self.just_moved:
                self.just_moved = False
            else:
                self.network.write(pickle.dumps(self.board))
        else:
            try:
                self.board = pickle.loads(self.network.recv())
            # Raises when an invalid data is received
            except pickle.UnpicklingError:
                pass
            except UnicodeDecodeError:
                pass
        self.game_display.show_board(self.board)

    def get_move(self, events: list[pygame.event.Event]):
        click = False
        if self.board.turn == self.color:
            if self.selected:
                self.game_display.highlight(self.selected)
            if self.move_to:
                self.game_display.highlight(self.move_to)
            if self.selected and self.move_to:
                self.game_display.arrow(self.selected, self.move_to)

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    click = False

            pointer = pygame.mouse.get_pos()
            for square in self.game_display.squares:
                if self.game_display.squares.get(square)[0].collidepoint(pointer):
                    if click:
                        print(square)
                        if self.my_piece(square):
                            self.selected = square
                            self.move_to = None
                        if self.empty_field(square):
                            if self.selected:
                                if self.move_to:
                                    move = chess.Move.from_uci(f"{self.selected}{self.move_to}")
                                    if self.board.is_legal(move):
                                        self.board.push(move)
                                        self.selected = None
                                        self.move_to = None
                                        self.network.write(pickle.dumps(self.board))
                                        self.just_moved = True
                                else:
                                    move = chess.Move.from_uci(f"{self.selected}{square}")
                                    if self.board.is_legal(move):
                                        self.move_to = square

    def my_piece(self, field: str) -> bool:
        square = self.board.piece_at(chess.parse_square(field))
        if square:
            if square.color == self.color:
                print(square)
                return True
        return False

    def empty_field(self, field: str) -> bool:
        square = self.board.piece_at(chess.parse_square(field))
        return False if square else True

    @classmethod
    def from_client(cls, obj):
        return cls(
            False,
            obj.user_data, obj.enemy_data,
            obj.client,
            obj.screen, obj.clock
        )

    @classmethod
    def from_host(cls, obj):
        return cls(
            True,
            obj.user_data, obj.enemy_data,
            obj.server,
            obj.screen, obj.clock
        )
