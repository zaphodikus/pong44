#
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from colours import *
from sprite_sheet import FontSheet


def draw(window, ss1, ss2):
    for x in range(0, 25):
        window.blit(ss1.glyph_by_char(chr(ord('A') + x)),
                    (x * ss1.glyph_width,
                     ss1.glyph_height,
                     (x+1) * ss1.glyph_width,
                     2 * ss1.glyph_height))

    for x in range(0, 10):
        window.blit(ss1.glyph_by_char(chr(ord('0') + x)),
                    (x * ss1.glyph_width,
                     3 * ss1.glyph_height,
                     (x+1) * ss1.glyph_width,
                     4 * ss1.glyph_height))
    x=0
    for ch in "A (Small.TXT) file! or? <big>-+_":
        window.blit(ss1.glyph_by_char(ch),
                    (x * ss1.glyph_width,
                     5 * ss1.glyph_height,
                     (x+1) * ss1.glyph_width,
                     6 * ss1.glyph_height))
        x+=1

    for x in range(0, 25):
        window.blit(ss2.glyph_by_char(chr(ord('A') + x)),
                    (x * ss2.glyph_width,
                     ss2.glyph_height,
                     (x+1) * ss2.glyph_width,
                     2 * ss2.glyph_height))

    x=0
    for ch in "A (Small.TXT) file! or? <big>-+_Copyright©":
        window.blit(ss2.glyph_by_char(ch),
                    (x * ss2.glyph_width,
                     12 * ss2.glyph_height,
                     (x+1) * ss2.glyph_width,
                     13 * ss2.glyph_height))
        x += 1


# main
width = 1000
height = 800
BORDER_THICK = 5
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite sheet test")
clock = pygame.time.Clock()
font1 = FontSheet('../images/digital_font_page0.png')
font2 = FontSheet('../images/digifont_16x16.png')

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    if run:
        win.fill(BLUE)
        draw(win, font1, font2)
        pygame.draw.rect(win, RED, (1, 0, width, BORDER_THICK))
        x = width/2
        length = int(height/20/2)
        stroke = int(length/2)
        for segment in range(0, int(height/length)):
            pygame.draw.line(win, WHITE, (x, segment*length), (x, segment*length+stroke))
        pygame.display.update()
