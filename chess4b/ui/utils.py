import sys
import pygame


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def username_input(screen: pygame.Surface, clock: pygame.time.Clock, length: int = 10) -> tuple[str, bool]:
    """
    Function to resolve the Name of the Player and if the player wants to be Host or client

    :param screen: The Surface of the game
    :param clock: The pygame clock to sync the game to
    :param length: The length of the name
    :return:
        str: The name of the Player
        bool: True -> Host, False -> Client
    """
    max_len_name = 10

    # colors
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    grey = (136, 136, 136)
    turquoise = (52, 78, 91)

    color = grey
    # Coordinates
    X = 450
    Y = 700
    # Set up the drawing window
    pygame.display.set_mode([X, Y])
    pygame.display.set_caption('Login Window')

    header_font = pygame.font.Font('AGENCYR.ttf', 64)
    base_font = pygame.font.Font('AGENCYR.ttf', 32)
    user_text = ''
    text = header_font.render('LOGIN MENU', True, white, turquoise)
    text2 = base_font.render('NAME:', True, white, turquoise)
    text3 = base_font.render('host', True, white)
    text4 = base_font.render('client', True, white)
    text5 = base_font.render('host has to be selected first', True, white, turquoise)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 20)
    text2Rect = text.get_rect()
    text2Rect.center = (X // 1.45, Y // 4)
    text3Rect = text.get_rect()
    text3Rect.center = (X // 1.82, Y // 2)
    text4Rect = text.get_rect()
    text4Rect.center = (X // 1.225, Y // 2)
    text5Rect = text.get_rect()
    text5Rect.center = (X // 2.2, Y // 1.3)
    input_rect = pygame.Rect(170, 200, 140, 32)
    host_rect = pygame.Rect(122, 308, 50, 45)

    client_rect = pygame.Rect(242, 308, 63, 45)

    active = False
    click = False
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                click = False

            elif event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    if active:
                        user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    if active:
                        if len(user_text) < max_len_name:
                            user_text += event.unicode

        mouse_pos = pygame.mouse.get_pos()
        if input_rect.collidepoint(mouse_pos):
            if click:
                active = True
                color = pygame.Color("lightskyblue3")
        elif host_rect.collidepoint(mouse_pos):
            if click:
                if user_text:
                    return user_text, True
        elif client_rect.collidepoint(mouse_pos):
            if click:
                if user_text:
                    return user_text, False
        else:
            if click:
                if active:
                    color = grey

        # Fill the background with white
        screen.fill(turquoise)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        screen.blit(text3, text3Rect)
        screen.blit(text4, text4Rect)
        screen.blit(text5, text5Rect)

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)

        pygame.draw.rect(screen, grey, host_rect, 2, 2)
        pygame.draw.rect(screen, grey, client_rect, 2, 2)

        text_surface = base_font.render(user_text, True, white)

        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 0))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        # display.update() will update the display
        pygame.display.update()

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)
