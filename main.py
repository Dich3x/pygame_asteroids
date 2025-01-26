import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *



def main():

    pygame.init()
    print("Starting asteroids!")
    life = 2
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    points = 0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            for shot in shots:
                if thing.position.x < -100 or thing.position.x > 2020 or thing.position.y < -100 or thing.position.y > 1180:
                    thing.kill()
                if shot.position.x < -100 or shot.position.x > 2020 or shot.position.y < -100 or shot.position.y > 1180:
                    shot.kill()
                if thing.collisionDetection(shot):
                    shot.kill()
                    thing.split()
                    points += 1

            if player.collisionDetection(thing):
                if life == 0:
                    print(f"Yore points: {points}")
                    sys.exit("Game over!")
                else:
                    life -= 1
                    thing.kill()
                    screen.fill(RED)
                    for thing in drawable:
                        thing.draw(screen)
                    pygame.display.flip()
                    dt = clock.tick(60) / 10000

        screen.fill(BLACK)
        for thing in drawable:
            thing.draw(screen)
        if len(updatable) < points / 5 + 3:
            AsteroidField()

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()