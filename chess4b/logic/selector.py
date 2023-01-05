import pygame

from chess4b.logic import BaseLogic
from chess4b.logic.host import HostLogic
from chess4b.logic.client import ClientLogic

from chess4b.ui.utils import username_input


class HostClientSelector(BaseLogic):
    def __init__(self, auto_setup: bool = True):
        self.clock = None

        super().__init__(auto_setup=auto_setup)

        if auto_setup:
            self.setup()

    def setup(self) -> None:
        """
        Initialize pygame, set a caption, get the clock and enable key repeat

        Returns
        -------
        None
        """
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Schach")
        # Pygame now allows natively to enable key repeat:
        pygame.key.set_repeat(200, 25)

    def start_game_loop(self) -> None:
        username, host = username_input(self.screen, self.clock)
        if host:
            log = HostLogic.from_selector(self, username)

        else:
            log = ClientLogic.from_selector(self, username)

        log.start_game_loop()
