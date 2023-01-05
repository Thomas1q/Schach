import pygame


class BaseLogic:
    def __init__(self, screen: pygame.Surface = None, clock: pygame.time.Clock = None, auto_setup: bool = True):
        self.screen = screen
        self.clock = clock

        if auto_setup:
            self.setup()

    def setup(self):
        if not self.screen:
            pygame.init()

            pygame.display.set_caption("Chess")
            self.screen = pygame.display.set_mode((1000, 700))
            # Pygame now allows natively to enable key repeat:
            pygame.key.set_repeat(200, 25)

        if not self.clock:
            self.clock = pygame.time.Clock()

    def start_game_loop(self):
        while True:
            events = pygame.event.get()

            pygame.display.update()
            self.clock.tick(60)

    def from_selector(self, obj, username: str):
        ...
