import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot



def main():
    # Initiate Game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Create containers then instances of shot
    Shot.containers = (shots, updatable, drawable)

    # Create containers then instances of asteroid and asteroidfield
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Create containers then instances of player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        # Initialize logging 
        log_state()

        # Check if user click the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        # Check player - asteroid collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            # Check shoot - asteroid collision
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # Show screen
        screen.fill("black")

        # Draw Player and Asteroids
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        # Set to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
