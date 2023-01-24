import pygame
import chess4b.ui.gui_buttons as gui_buttons


def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def wait_for_client(screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    # creates screen + settings

    X = 1200
    Y = 800
    screen = pygame.display.set_mode([X, Y])
    pygame.display.set_caption('Loading Window')
    screen.fill((52, 78, 91))

    # loads the image of the button

    play_image = pygame.image.load("chess4b/ui/images/button_play.png").convert_alpha()

    # scaling the button (easier to use than the build in scale (gui_buttons)

    size = (200, 200)
    play_image = pygame.transform.scale(play_image, size)

    # displays the button

    play_button = gui_buttons.Button(500, 200, play_image, 1)
    play_button.draw(screen)

    # text settings

    font = pygame.font.Font('AGENCYR.ttf', 32)
    TEXT_COL = pygame.Color(255, 255, 255)

    # displays the text via draw_text function

    draw_text("PRESS BUTTON TO START", font, TEXT_COL, 475, 100, screen)
    draw_text("WAITING FOR SECOND PLAYER", font, TEXT_COL, 455, 500, screen)

    pass
