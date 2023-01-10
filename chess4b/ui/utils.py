import pygame


def username_input(screen: pygame.Surface, clock: pygame.time.Clock, length: int = 10) -> tuple[str, bool]:
    """
    FUnction to resolve the Name of the Player and if the player wants to be Host or client

    :param screen: The Surface of the game
    :param clock: The pygame clock to sync the game to
    :param length: The length of the name
    :return:
        str: The name of the Player
        bool: True -> Host, False -> Client
    """
    pass