import asyncio
import pygame

from chess4b.ui.utils import draw_text


class LoginPage:
    def __init__(self, loop: asyncio.AbstractEventLoop, clock: pygame.time.Clock, event_queue: asyncio.Queue, screen: pygame.Surface | None = None):
        pygame.init()

        if screen:
            self.screen = screen
        else:
            self.screen = pygame.display.set_mode((1000, 850))

        if clock:
            self.clock = clock
        else:
            self.clock = pygame.time.Clock()

        self.event_queue = event_queue
        self.loop = loop

    async def get_login(self):
        print("get_login")
        return await asyncio.gather(self.login_loop())

    async def login_loop(self, length: int = 14):
        click = False
        username = ""
        print("aSdas")
        while not username:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 200, 600, 300), 0, 5)

            draw_text("Welcome to Chess", (12, 255, 255), self.screen, 220, 220, 50)
            draw_text("Created by Thomas, Daniel and Leon", (12, 255, 255), self.screen, 220, 260, 20)
            draw_text("Insert your Username and press Start", (12, 255, 255), self.screen, 220, 310, 35)

            name_box = pygame.Rect(220, 350, 460, 60)
            pygame.draw.rect(self.screen, (0, 0, 0), name_box, 0, 5)
            input = pygame.font.Font(None, 50).render(username, True, (255, 255, 255))
            self.screen.blit(input, input.get_rect(center=name_box.center))

            start_button = pygame.Rect(220, 420, 130, 60)

            mx, my = pygame.mouse.get_pos()
            if start_button.collidepoint((mx, my)):
                if click:
                    if username:
                        return username

            pygame.draw.rect(self.screen, (0, 161, 255), start_button, 0, 4)
            draw_text("START", (12, 255, 255), self.screen, 230, 435, 50)

            for event in await self.event_queue.get():
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
            self.clock.tick(60)
