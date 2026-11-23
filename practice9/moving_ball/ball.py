import pygame
RADIUS=25
STEP=20
class Ball:
    def __init__(self):
        self.x=300
        self.y=300
    def draw(self,screen):
        pygame.draw.circle(screen,(255,0,0),(self.x,self.y),RADIUS)

    def move(self, key, width, height):
        if key == pygame.K_UP:
            if self.y - RADIUS - STEP >= 0:
                self.y -= STEP

        elif key == pygame.K_DOWN:
            if self.y + RADIUS + STEP <= height:
                self.y += STEP

        elif key == pygame.K_LEFT:
            if self.x - RADIUS - STEP >= 0:
                self.x -= STEP

        elif key == pygame.K_RIGHT:
            if self.x + RADIUS + STEP <= width:
                self.x += STEP