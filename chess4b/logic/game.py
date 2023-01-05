import pygame

from chess4b.logic import BaseLogic

class GameLogic(BaseLogic):
    def __init__(self, screen: pygame.Surface = None, clock: pygame.time.Clock = None):
        super().__init__(screen, clock)

    def start_game_loop(self):
        while True:
            events = pygame.event.get()
