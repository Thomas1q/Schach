import pygame
import chess4b.ui.gui_buttons as gui_buttons
import sys

from chess4b.logic.game import GameLogic


def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def wait_for_client() -> None:
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
    draw_text("WAITING FOR SECOND PLAYER", font, TEXT_COL, 455, 500, screen)

    pass


def wait_for_decision(
        game: GameLogic,
        events: list[pygame.event.Event],
        other_decision: bool | None) -> bool | None:
    # Wait for the player to decide if he wants to play again or wait for another player.
    # True -> play again
    # False -> wait for another player
    # None -> not made any decision yet
    # Other decision is the decision of the other player

    # Define Constants that are used in this function
    X = 450
    Y = 700
    FONT = pygame.font.Font('AGENCYR.ttf', 32)
    COL = pygame.Color(248, 239, 221)
    TURQUOISE = pygame.Color(52, 78, 91)

    screen = pygame.display.set_mode([X, Y])
    pygame.display.set_caption('End Window')
    screen.fill(TURQUOISE)

    end_text = FONT.render("END MENU", True, COL)
    end_text_rect = end_text.get_rect(center=(X / 2, 50))
    screen.blit(end_text, end_text_rect)

    # Display it the player won or lost
    if game.board.turn != game.color:
        TEXT = "YOU WON"
    else:
        TEXT = "YOU LOST"
    outcome_text = FONT.render(TEXT, True, COL)
    outcome_text_rect = outcome_text.get_rect(center=(X / 2, 150))
    screen.blit(outcome_text, outcome_text_rect)

    # Button to play again
    pa_text = FONT.render('PLAY AGAIN', True, COL, TURQUOISE)
    pa_rect = pa_text.get_rect(center=(X / 2, 200))
    pygame.draw.rect(screen, COL, pa_rect.inflate(20, 0), 2, 2)
    screen.blit(pa_text, pa_rect)

    # Button to wait for another player
    np_text = FONT.render('NEW PLAYER', True, COL, TURQUOISE)
    np_rect = np_text.get_rect(center=(X / 2, 400))
    pygame.draw.rect(screen, COL, np_rect.inflate(20, 0), 2, 2)
    screen.blit(np_text, np_rect)

    # Show button outline
    # pygame.draw.rect(screen, COL, pa_rect.inflate(2, 0), 2, 2)
    # pygame.draw.rect(screen, COL, np_rect.inflate(2, 0), 2, 2)

    # Show the decision of the other player
    if other_decision is True:
        text_od = 'OPPONENT WANTS TO PLAY AGAIN'
    elif other_decision is False:
        text_od = 'OPPONENT DOES NOT WANT TO PLAY AGAIN'
    else:
        text_od = 'WAITING FOR OPPONENTS DECISION'

    text_od = FONT.render(text_od, True, COL)
    text_od_rect = text_od.get_rect(center=(X / 2, 600))
    screen.blit(text_od, text_od_rect)
    
    click = False

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            click = False

    # Check if a button was pressed and return the decision
    mouse_pos = pygame.mouse.get_pos()
    if pa_rect.collidepoint(mouse_pos):
        if click:
            return True
    elif np_rect.collidepoint(mouse_pos):
        if click:
            return False

    return None
