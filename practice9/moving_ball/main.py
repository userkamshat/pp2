import pygame
from ball import Ball
pygame.init()
WIDTH = 600
HEIGHT = 600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Moving Ball")
ball=Ball()
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            ball.move(event.key, WIDTH, HEIGHT)

    # White background
    screen.fill((255, 255, 255))

    # Draw the ball
    ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()