import pygame
pygame.init()

#framerate
clock = pygame.time.Clock()

#state
login_name = True
login_fin = False

#draw function
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
grey = (136, 136, 136)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('grey')
color = color_passive

#Coordinates
X = 450
Y = 700
# Set up the drawing window
screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Login Window')

header_font = pygame.font.Font('AGENCYR.ttf', 64)
base_font = pygame.font.Font('AGENCYR.ttf', 32)
user_text = ''
text = header_font.render('menu', True, black, white)
text2 = base_font.render('name:', True, black, white)
text3 = base_font.render('checkhost:', True, black, white)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 50)
text2Rect = text.get_rect()
text2Rect.center = (X // 2, Y // 9)
input_rect = pygame.Rect(170, 90, 140, 32)


active = False
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if login_name = True && check_host = True && done_button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Hello")
                login_name = False
                draw_text("Check Host:",base_font, white, 170, 150)
                input_rect = pygame.Rect(170, 150, 140, 32)

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

    # Fill the background with white
    screen.fill((white))
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
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
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()

    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)