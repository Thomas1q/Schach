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

        self.game_display = GameDisplay(screen)

        if host:
            self.color: chess.Color = chess.WHITE
            self.board = chess.Board()
        else:
            self.color: chess.Color = chess.BLACK
            self.board = None

        self.before_color: chess.Color = chess.WHITE

        self.selected: str | None = None
        self.move_to: str | None = None

        super().__init__(screen, clock)

    def start_game_loop(self):
        while True:
            events = pygame.event.get()

            if self.board:
                self.display_board()

                self.get_move(events)

            pygame.display.update()
            self.clock.tick(60)

    def display_board(self):
        if self.before_color != self.board.turn:
            self.before_color = self.board.turn
            if self.board.turn == self.color:
                self.network.write(pickle.dumps(self.board.mirror))
            else:
                self.board = pickle.loads(self.network.recv())
        self.game_display.show_board(self.board)

    def get_move(self, events: list[pygame.event.Event]):
        click = False
        if self.board.turn == self.color:
            if self.selected:
                self.game_display.highlight(self.selected)
            if self.move_to:
                self.game_display.highlight(self.move_to)

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
                if square.rect.collidepoint(pointer):
                    if click:
                        if self.selected:
                            if self.move_to:
                                move = chess.Move.from_uci(f"{self.selected}{self.move_to}")
                                if self.board.is_legal(move):
                                    self.board.push(move)
                            else:
                                self.move_to = square.name
                        else:
                            self.selected = square.name

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
