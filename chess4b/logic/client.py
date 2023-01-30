import sys
import pygame
import pickle
import threading

from chess4b.logic import BaseLogic
from chess4b.logic.game import GameLogic
from chess4b.network import Client
from chess4b.database import SqlInterface
from chess4b.ui.loading import wait_for_decision


class ClientLogic(BaseLogic):
    def __init__(self, username: str, screen: pygame.Surface = None, clock: pygame.time.Clock = None):
        self.username = username

        self.client: Client = Client()
        self.log: GameLogic | None = None

        self.user_data: User | None = None
        self.enemy_data: User | None = None

        self.decision_waiter: threading.Thread | None = None

        self.decision: bool | None = None
        self.other_decision: bool | None = None
        self.told_decision: bool = False

        self.already: bool = False

        super().__init__(screen, clock, False)

    def start_game_loop(self):
        while True:
            events = pygame.event.get()
            if self.already:
                # The other player has not made a decision yet -> start the waiter again
                if not self.decision_waiter:
                    self.decision_waiter = threading.Thread(target=self.wait_for_decision)
                    try:
                        self.decision_waiter.start()
                        print("Started decision waiter")
                    except RuntimeError:
                        pass
                # Check if the player has already made a decision
                if not self.decision:
                    self.decision = wait_for_decision(self.screen, self.clock, self.log, events, self.other_decision)
                # The player has made a decision
                if self.decision is not None:
                    if not self.told_decision:
                        print("Sending decision", self.decision)
                        self.client.write(pickle.dumps(self.decision))
                        self.told_decision = True
                    # He wants to play with someone else
                    if self.decision is False:
                        self.enemy_data = None
                        self.already = False
                        self.log = None
            # The player is starting to search for a new opponent
            else:
                self.join_server()
                if not self.user_data:
                    return

            if self.decision is True and ((self.user_data and not self.already) or (self.already and self.other_decision is True)):
                pygame.time.wait(100)
                self.log = GameLogic.from_client(self)
                self.log.start_game_loop()
                self.already = True
                self.decision = None
                self.other_decision = None

                self.decision_waiter = None

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

    def join_server(self):
        conn = self.client.client_connect()
        if conn:
            self.enemy_data = pickle.loads(self.client.recv())
            self.client.write(self.username.encode())
            self.user_data = pickle.loads(self.client.recv())
            self.decision = True
        return

    def wait_for_decision(self) -> None:
        self.other_decision = pickle.loads(self.client.recv())

    @classmethod
    def from_selector(cls, obj, username: str):
        pygame.display.set_mode((1200, 800))
        return cls(
            username,
            obj.screen,
            obj.clock
        )
