import pygame
from engine import *
from engine.game_engine import GameObject

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
x=255
tren=GameObject("Tren",23,34)
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
            if event.key == pygame.K_RIGHT:
                x += 1
    # Screen print 
    screen.fill((255, 255, 255))
    tren.getCoords()
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (x, 250), 75)
    x += 1
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()