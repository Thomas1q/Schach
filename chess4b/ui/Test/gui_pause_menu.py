import pygame
import gui_buttons

pygame.init()

X = 450
Y = 700
# Set up the drawing window

screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Pause Window')

#game variables

game_paused = False

#define fonts

font = pygame.font.Font('AGENCYR.ttf', 32)
font2 = pygame.font.Font('AGENCYR.ttf', 64)

#define colors

TEXT_COL = (255, 255, 255)

#load buttons

resume_image = pygame.image.load("chess4b/ui/images/button_resume.png").convert_alpha()
quit_image = pygame.image.load("chess4b/ui/images/button_quit.png").convert_alpha()

#create buttons instances
resume_button = gui_buttons.Button(125, 200, resume_image, 1)
quit_button = gui_buttons.Button(157, 400, quit_image, 1)

#simple function to draw text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))


#game loop
run = True
while run:

    #background color
    screen.fill((52, 78, 91))

    #check if game is paused
    if game_paused == True:
        draw_text("PAUSE MENU", font2, TEXT_COL, 100,50)
        if resume_button.draw(screen):
            game_paused = False
        if quit_button.draw(screen):
            run = False
    #display menu
    else:
        draw_text("PRESS ESC TO PAUSE", font, TEXT_COL, 125, 50)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()