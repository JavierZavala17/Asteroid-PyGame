from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
import pygame

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Initiate Game
    pygame.init()
    # Create clock for FPS and update things
    clock = pygame.time.Clock()
    
    # Set containers before creating instances
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )

    # Create Instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    # Set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        # Set to 60 FPS
        dt = clock.tick(60) / 1000
        # Initialize logging 
        log_state()

        # Check if user click the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Show screen
        screen.fill("black")
        # Draw Player and Asteroids (?)
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        # player.draw(screen)
        # player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
