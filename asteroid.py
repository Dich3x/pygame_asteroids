import pygame
import random
from constants import *
from circleshape import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color=WHITE, center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_agle = int(random.uniform(20, 50))
        
        velosity1 = self.velocity.rotate(random_agle)
        velosity2 = self.velocity.rotate(-random_agle)
        old_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, old_radius)
        asteroid.velocity = velosity1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, old_radius)
        asteroid.velocity = velosity2 * 1.2
