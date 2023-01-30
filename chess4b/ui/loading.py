import pygame
import chess4b.ui.gui_buttons as gui_buttons
import sys

from chess4b.logic.game import GameLogic


def __init__(self, screen: pygame.Surface):
    self.screen: pygame.Surface = screen


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


def wait_for_decision(
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        game: GameLogic,
        events: list[pygame.event.Event],
        other_decision: bool | None) -> bool | None:
    # Wait for the player to decide if he wants to play again or wait for another player.
    # True -> play again
    # False -> wait for another player
    # None -> not made any decision yet
    # Other decision is the decision of the other player

    X = 450
    Y = 700
    screen = pygame.display.set_mode([X, Y])
    pygame.display.set_caption('End Window')
    screen.fill((52, 78, 91))

    turquoise = (52, 78, 91)
    white = (248, 239, 221)
    color = (248, 239, 221)

    TEXT = "END MENU"
    FONT = pygame.font.Font('AGENCYR.ttf', 32)
    TEXT_COL = pygame.Color(248, 239, 221)

    draw_text(TEXT, FONT, TEXT_COL, 175, 50, screen)

    rect_pa = pygame.Rect(155, 200, 140, 32)
    rect_w = pygame.Rect(155, 400, 140, 32)

    pygame.draw.rect(screen, color, rect_pa, 2, 2)
    pygame.draw.rect(screen, color, rect_w, 2, 2)

    base_font = pygame.font.Font('AGENCYR.ttf', 32)
    text = base_font.render('PLAY AGAIN', True, TEXT_COL, turquoise)
    textRect = text.get_rect()
    textRect.center = rect_pa.center

    base_font = pygame.font.Font('AGENCYR.ttf', 32)
    text2 = base_font.render('NEW PLAYER', True, TEXT_COL, turquoise)
    text2Rect = text.get_rect()
    text2Rect.center = (rect_w.center[0]-4, rect_w.center[1])

    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)

    if other_decision:
        text_od = 'OPPONENT WANTS TO PLAY AGAIN'
        draw_text(text_od, FONT, TEXT_COL, 15, 600, screen)

    else:
        text_od = 'OPPONENT DOES NOT WANT TO PLAY AGAIN'
        draw_text(text_od, FONT, TEXT_COL, 15, 600, screen)

    active = False
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            click = False

    mouse_pos = pygame.mouse.get_pos()
    if rect_pa.collidepoint(mouse_pos):
        if click:
            if other_decision:
                active = True
                color = pygame.Color("lightskyblue3")
                return True

    elif rect_w.collidepoint(mouse_pos):
        if click:
            active = True
            color = pygame.Color("lightskyblue3")
            return False

    else:
        if click:
            if active:
                color = white



