import pygame
from constants import *



class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, color=WHITE, points=self.triangle(), width=2)

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collisionDetection(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
