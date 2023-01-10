#simple function to draw text on screen

import pygame
pygame.init()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))