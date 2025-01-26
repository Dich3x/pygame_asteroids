import pygame
from constants import *
from circleshape import *
from shot import *



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_shot = 0
        self.cooldown_up_speed = 0
        self.timer_up_speed = 10

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown_shot -= dt
        self.timer_up_speed -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_LSHIFT]:
            if self.timer_up_speed < -1:
                self.timer_up_speed = 0
            if self.cooldown_up_speed <= 10 and self.timer_up_speed <= 0:
                self.move(dt * 1.5)
                self.cooldown_shot = PLAYER_SHOOT_COOLDOWN
                self.cooldown_up_speed += PLAYER_UP_SPEED_COOLDOWN * 2
            elif self.timer_up_speed <= 0:
                self.timer_up_speed = 5
                self.cooldown_up_speed = 0

        if keys[pygame.K_SPACE]:
            if self.cooldown_shot <= 0:
                self.shoot()
                self.cooldown_shot = PLAYER_SHOOT_COOLDOWN


    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED