import pygame as pg
from engine.game_engine import gameEngine

pg.init()
clock = pg.time.Clock()
# Set up the drawing window with name and res
screen = pg.display.set_mode([1000, 500], pg.RESIZABLE)
pg.display.set_caption("TrainSim")
# Engine setup
g_engine=gameEngine(True)
while g_engine.isRunning():
    g_engine.keyEventsCheck()
    # Screen print 
    screen.fill((220, 236, 251))
    g_engine.renderObjects(screen,clock.get_fps())
    g_engine.update()
    # Flip the display
    pg.display.flip()
    clock.tick(60)
pg.quit()