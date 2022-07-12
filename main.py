from tokenize import group
import pygame as pg
from engine import *
from engine.game_engine import GameObject

pg.init()

# Set up the drawing window
screen = pg.display.set_mode([500, 500])
x=255
tren=GameObject("Tren",["objects","train.png"],500,450)
gameObjs= pg.sprite.RenderPlain()
gameObjs.add(tren)
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x -= 1
            if event.key == pg.K_RIGHT:
                x += 1
    # Screen print 
    screen.fill((255, 255, 255))
    #tren.getCoords()
    gameObjs.draw(screen)
    gameObjs.update()
    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (x, 250), 75)
    #x += 1
    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()