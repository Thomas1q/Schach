import pygame

from chess4b.logic import BaseLogic
from chess4b.database import SqlInterface


class HostLogic(BaseLogic):
    def __init__(self, username: str, screen: pygame.Surface = None, clock: pygame.time.Clock = None):
        self._db_intf = SqlInterface()
        self._db_intf.setup()

        self.user_data: User = self._db_intf.get_user_data(username)
        self.enemy_data: User | None = None

        super().__init__(screen, clock, False)

    def start_game_loop(self):
        while True:
            events = pygame.event.get()

            self.wait_for_client()

            pygame.display.update()
            self.clock.tick(60)

    def wait_for_client(self):
        pass

    @classmethod
    def from_selector(cls, obj, username):
        return cls(
            username,
            obj.screen,
            obj.clock
        )

