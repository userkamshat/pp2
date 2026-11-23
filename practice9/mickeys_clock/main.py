import pygame
from clock import MickeyClock
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mickey's Clock")

clock = pygame.time.Clock()
mickey_clock = MickeyClock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Draw clock
    mickey_clock.draw(screen)

    pygame.display.flip()

    clock.tick(1)

pygame.quit()