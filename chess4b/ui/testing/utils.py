import pygame


def draw_text(text: str, color: tuple[int, int, int], surface: pygame.Surface, x: int, y: int, text_size: int = 30) -> pygame.rect.Rect:
    font = pygame.font.SysFont(None, text_size)
    obj = font.render(text, True, color)
    rect = obj.get_rect()
    rect.topleft = (x, y)
    surface.blit(obj, rect)
    return rect


def username_input(screen: pygame.Surface, clock: pygame.time.Clock, length: int = 10):
    click = False
    run = True
    username = ""
    while run:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(200, 200, 600, 300), 0, 5)

        draw_text("Welcome to Chess", (12, 255, 255), screen, 220, 220, 50)
        draw_text("Created by Thomas, Daniel, Leon", (12, 255, 255), screen, 220, 260, 20)
        draw_text("Insert your Username and select Host/Client", (12, 255, 255), screen, 220, 310, 35)

        name_box = pygame.Rect(220, 350, 460, 60)
        pygame.draw.rect(screen, (0, 0, 0), name_box, 0, 5)
        input = pygame.font.Font(None, 50).render(username, True, (255, 255, 255))
        screen.blit(input, input.get_rect(center=name_box.center))

        host_button = pygame.Rect(220, 420, 150, 60)
        client_button = pygame.Rect(450, 420, 150, 60)

        mx, my = pygame.mouse.get_pos()
        if host_button.collidepoint((mx, my)):
            if click:
                if username:
                    return username, True
        elif client_button.collidepoint((mx, my)):
            if click:
                if username:
                    return username, False

        pygame.draw.rect(screen, (0, 161, 255), host_button, 0, 4)
        draw_text("HOST", (12, 255, 255), screen, 230, 435, 50)

        pygame.draw.rect(screen, (0, 161, 255), client_button, 0, 4)
        draw_text("CLIENT", (12, 255, 255), screen, 460, 435, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key == pygame.K_RETURN:
                    if username:
                        return username
                else:
                    if len(username) < length:
                        username += event.unicode

        pygame.display.update()
        clock.tick(60)
