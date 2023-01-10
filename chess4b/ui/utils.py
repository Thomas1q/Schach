import pygame


def username_input(screen: pygame.Surface, clock: pygame.time.Clock, length: int = 10) -> tuple[str, bool]:
    """
    Function to resolve the Name of the Player and if the player wants to be Host or client

    :param screen: The Surface of the game
    :param clock: The pygame clock to sync the game to
    :param length: The length of the name
    :return:
        str: The name of the Player
        bool: True -> Host, False -> Client
        str: user_text
        bool: Host_Client
    """

    # game varibales
    login_name = True
    login_fin = False
    host_client = None

    # colors
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    grey = (136, 136, 136)
    turquoise = (52, 78, 91)

    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('grey')
    color = color_passive
    color2 = pygame.Color(black)
    # Coordinates
    X = 450
    Y = 700
    # Set up the drawing window
    pygame.display.set_mode([X, Y])
    pygame.display.set_caption('Login Window')

    header_font = pygame.font.Font('AGENCYR.ttf', 64)
    base_font = pygame.font.Font('AGENCYR.ttf', 32)
    user_text = ''
    text = header_font.render('menu', True, black, turquoise)
    text2 = base_font.render('name:', True, black, turquoise)
    text3 = base_font.render('host', True, black, 'grey')
    text4 = base_font.render('client', True, black, 'grey')
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 20)
    text2Rect = text.get_rect()
    text2Rect.center = (X // 2, Y // 4)
    text3Rect = text.get_rect()
    text3Rect.center = (X // 2.5, Y // 2)
    text4Rect = text.get_rect()
    text4Rect.center = (X // 1.5, Y // 2)
    input_rect = pygame.Rect(170, 200, 140, 32)
    host_rect = pygame.Rect(122, 308, 50, 45)
    client_rect = pygame.Rect(242, 308, 63, 45)

    # draw function
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    active = False
    running = True
    while running:
        print(host_client)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True

                else:
                    active = False
                if host_rect.collidepoint(event.pos):

                    host_client = True
                    return user_text, True


                else:
                    host_client = False
                    return user_text, False


            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

        # Fill the background with white
        screen.fill((turquoise))
        pygame.draw.rect(screen, color2, host_rect)
        pygame.draw.rect(screen, color2, client_rect)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        screen.blit(text3, text3Rect)
        screen.blit(text4, text4Rect)

        pygame.display.update()

        if active:
            color = color_active
        else:
            color = color_passive

            # draw rectangle and argument passed which should
            # be on screen
        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 0))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)