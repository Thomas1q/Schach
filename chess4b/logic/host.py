import sys
import pygame
import pickle
import threading

from chess4b.ui.loading import wait_for_client, wait_for_decision
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
        self.log: GameLogic | None = None

        self.user_data: User = self._db_intf.get_user_data(username)
        self.enemy_data: User | None = None

        self.already: bool = False

        self.client_waiter: threading.Thread | None = None
        self.decision_waiter: threading.Thread | None = None

        self.decision: bool | None = None
        self.other_decision: bool | None = None
        self.told_decision: bool = False

        self._db_intf.close()
        super().__init__(screen, clock, False)

    def start_game_loop(self):
        while True:
            events = pygame.event.get()

            # A game was already played
            if self.already:
                # The other player has not made a decision yet -> start the waiter again
                if not self.decision_waiter:
                    self.decision_waiter = threading.Thread(target=self.wait_for_decision)
                    try:
                        self.decision_waiter.start()
                        print("Started decision waiter")
                    except RuntimeError:
                        pass
                print(self.other_decision)
                # Check if the player has already made a decision
                if not self.decision:
                    self.decision = wait_for_decision(self.screen, self.clock, self.log, events, self.other_decision)
                # The player has made a decision
                if self.decision is not None:
                    if not self.told_decision:
                        print("Sending decision", self.decision)
                        self.server.write(pickle.dumps(self.decision))
                        self.told_decision = True
                    # He wants to play with someone else
                    if self.decision is False:
                        self.enemy_data = None
                        self.already = False
                        self.log = None
            # The player is starting to search for a new opponent
            else:
                # Starting a new
                try:
                    if not self.client_waiter:
                        print("Starting client waiter")
                        self.client_waiter = threading.Thread(target=self.wait_for_client)
                        try:
                            self.client_waiter.start()
                        except RuntimeError:
                            pass
                except RuntimeError:
                    pass
                wait_for_client(self.screen, self.clock)

            if self.decision is True and ((self.user_data and not self.already) or (self.already and self.other_decision is True)):
                pygame.time.wait(100)
                self.log = GameLogic.from_host(self)
                self.log.start_game_loop()
                self.already = True
                self.decision = None
                self.other_decision = None

                # Reset waiters to start new when needed
                self.client_waiter = None
                self.decision_waiter = None

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
        print("Client connected")
        self.decision = True

    def wait_for_decision(self) -> None:
        self.other_decision = pickle.loads(self.server.recv())

    @classmethod
    def from_selector(cls, obj, username):
        return cls(
            username,
            obj.screen,
            obj.clock
        )

