import sys
import pygame
import pickle
import threading

from chess4b.ui.loading import wait_for_client
from chess4b.logic import BaseLogic
from chess4b.logic.game import GameLogic
from chess4b.models import User
from chess4b.network import Server
from chess4b.database import SqlInterface


class HostLogic(BaseLogic):
    def __init__(self, username: str, screen: pygame.Surface = None, clock: pygame.time.Clock = None):
        self._db_intf = SqlInterface()
        self._db_intf.setup()

        self.server: Server = Server()

        self.user_data: User = self._db_intf.get_user_data(username)
        self.enemy_data: User | None = None

        self.client_waiter = threading.Thread(target=self.wait_for_client)
        self._db_intf.close()
        super().__init__(screen, clock, False)

    def start_game_loop(self):
        while True:
            events = pygame.event.get()

            wait_for_client(self.screen, self.clock)

            try:
                self.client_waiter.start()
            except RuntimeError:
                pass

            if self.enemy_data:
                pygame.time.wait(100)
                log = GameLogic.from_host(self)
                log.start_game_loop()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

    def wait_for_client(self):
        self._db_intf = SqlInterface()
        self._db_intf.setup(False)
        self.server.start_server()
        self.server.write(pickle.dumps(self.user_data))

        self.enemy_data = self._db_intf.get_user_data(self.server.recv().decode())
        self.server.write(pickle.dumps(self.enemy_data))

    @classmethod
    def from_selector(cls, obj, username):
        return cls(
            username,
            obj.screen,
            obj.clock
        )

