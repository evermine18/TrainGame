import pygame as pg
from engine import *
from engine.game_engine import GameEngine

def main():
    pg.init()
    clock = pg.time.Clock()
    # Set up the drawing window with name and res
    screen = pg.display.set_mode([500, 500], pg.RESIZABLE)
    pg.display.set_caption("Train Driver")

    # Engine setup
    engine = GameEngine(True)
    while engine.isRunning():
        engine.keyEventsCheck()
        # Screen print
        screen.fill((220, 236, 251))
        engine.renderObjects(screen, clock.get_fps())
        # Flip the display
        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == "__main__":
    main()
