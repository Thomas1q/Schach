import pygame

from chess4b.logic import BaseLogic
from chess4b.database import SqlInterface


class ClientLogic(BaseLogic):
    def __init__(self, username: str, screen: pygame.Surface = None, clock: pygame.time.Clock = None):
        self.username = username

        self.user_data: User | None = None
        self.enemy_data: User | None = None

        super().__init__(screen, clock, False)

    def start_game_loop(self):
        pass

    @classmethod
    def from_selector(cls, obj, username: str):
        return cls(
            username,
            obj.screen,
            obj.clock
        )
