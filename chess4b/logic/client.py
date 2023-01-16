import sys
import pygame
import pickle

from chess4b.logic import BaseLogic
from chess4b.logic.game import GameLogic
from chess4b.network import Client
from chess4b.database import SqlInterface


class ClientLogic(BaseLogic):
    def __init__(self, username: str, screen: pygame.Surface = None, clock: pygame.time.Clock = None):
        self.username = username

        self.client: Client = Client()

        self.user_data: User | None = None
        self.enemy_data: User | None = None

        super().__init__(screen, clock, False)

    def start_game_loop(self):
        while True:
            event = pygame.event.get()
            self.join_server()
            if not self.user_data:
                return

            pygame.display.update()
            self.clock.tick(60)

    def join_server(self):
        conn = self.client.client_connect()
        if conn:
            self.enemy_data = pickle.loads(self.client.recv())
            self.client.write(self.username.encode())
            self.user_data = pickle.loads(self.client.recv())
            log = GameLogic.from_client(self)
            log.start_game_loop()
        return

    @classmethod
    def from_selector(cls, obj, username: str):
        pygame.display.set_mode((1200, 800))
        return cls(
            username,
            obj.screen,
            obj.clock
        )
