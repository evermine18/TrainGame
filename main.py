from tokenize import group
import pygame as pg
from engine import *
from engine.game_engine import GameObject

pg.init()
clock = pg.time.Clock()
clock.tick(60)
# Set up the drawing window with name and res
screen = pg.display.set_mode([500, 500])
pg.display.set_caption("Train Driver")
#Test GameObject
tren=GameObject("Tren",["objects","train.png"],500,450)
gameObjs= pg.sprite.RenderPlain()
gameObjs.add(tren)
#DEBUG VARS
font = pg.font.SysFont(None, 24)
GREEN = (0, 255, 0)
# Run until the user asks to quit
running = True
while running:
    #Keyboard events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                tren.increaseSpeed()
            if event.key == pg.K_a:
                tren.decreaseSpeed()
    # Screen print 
    screen.fill((255, 255, 255))
    #tren.getCoords()
    gameObjs.draw(screen)
    gameObjs.update()
    #Draw DEBUG Info
    fps_count = font.render('FPS: '+str(clock.get_fps()), True, GREEN)
    screen.blit(fps_count, (20, 20))
    train_speed = font.render(' Train Speed: '+str(tren.getSpeed()), True, GREEN)
    screen.blit(train_speed, (15, 50))
    # Flip the display
    pg.display.flip()
    clock.tick(60)
# Done! Time to quit.
pg.quit()