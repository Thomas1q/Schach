import pygame
import gui_buttons

pygame.init()

#size of window
X=1200
Y=800

#game variables
login_completed = False
game_started = False
game_paused = False

#create screens
screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Game Window')

#fps
clock = pygame.time.Clock()

#text function
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#text settings

font = pygame.font.Font('AGENCYR.ttf', 32)
font2 = pygame.font.Font('AGENCYR.ttf', 64)
TEXT_COL = (255, 255, 255)

#load buttons

play_image = pygame.image.load("chess4b/ui/images/button_play.png").convert_alpha()
resume_image = pygame.image.load("chess4b/ui/images/button_resume.png").convert_alpha()
quit_image = pygame.image.load("chess4b/ui/images/button_quit.png").convert_alpha()
done_image = pygame.image.load("chess4b/ui/images/button_done.png").convert_alpha()

#scale button

size = (200, 200)

play_image = pygame.transform.scale(play_image, size)

#show button

play_button = gui_buttons.Button(500, 200, play_image, 1)
resume_button = gui_buttons.Button(125, 200, resume_image, 1)
quit_button = gui_buttons.Button(157, 400, quit_image, 1)
done_button = gui_buttons.Button(175, 500, done_image, 0.5)

run = True
while run:


    screen.fill((52, 78, 91))


    #checks if login is done
    if login_completed == False:
        screen = pygame.display.set_mode([450, 700])
        pygame.display.set_caption('Login Window')
        screen.fill((52, 78, 91))
        if done_button.draw(screen):
            login_completed = True

        #opens starting window
        if login_completed == True:
            screen = pygame.display.set_mode([X, Y])
            pygame.display.set_caption('Starting Window')
            screen.fill((52, 78, 91))

    #checks if game has started
    if game_started == False:
        draw_text("PRESS BUTTON TO START", font, TEXT_COL, 475, 100)
        draw_text("WAITING FOR SECOND PLAYER", font, TEXT_COL, 455, 500)
        if play_button.draw(screen):
            game_started = True


    if game_started == True:

        #checks if game is paused
        #opens pause window
        if game_paused == True:
            screen = pygame.display.set_mode([450, 700])
            pygame.display.set_caption('Pause Window')
            screen.fill((52, 78, 91))
            draw_text("PAUSE MENU", font2, TEXT_COL, 100, 50)
            if resume_button.draw(screen):
                game_paused = False
            if quit_button.draw(screen):
                run = False
        else:
            screen = pygame.display.set_mode([1200, 800])
            pygame.display.set_caption('Game Window')
            screen.fill((52, 78, 91))
            draw_text("PRESS ESC TO PAUSE", font, TEXT_COL, 500, 750)


            draw_text("A", font, TEXT_COL, 200, 50)
            draw_text("B", font, TEXT_COL, 300, 50)
            draw_text("C", font, TEXT_COL, 400, 50)
            draw_text("D", font, TEXT_COL, 500, 50)
            draw_text("E", font, TEXT_COL, 600, 50)
            draw_text("F", font, TEXT_COL, 700, 50)
            draw_text("G", font, TEXT_COL, 800, 50)
            draw_text("H", font, TEXT_COL, 900, 50)

            draw_text("1", font, TEXT_COL, 125, 100)
            draw_text("2", font, TEXT_COL, 125, 175)
            draw_text("3", font, TEXT_COL, 125, 250)
            draw_text("4", font, TEXT_COL, 125, 325)
            draw_text("5", font, TEXT_COL, 125, 400)
            draw_text("6", font, TEXT_COL, 125, 475)
            draw_text("7", font, TEXT_COL, 125, 550)
            draw_text("8", font, TEXT_COL, 125, 625)




    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()




pygame.quit()