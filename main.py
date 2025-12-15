from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
import pygame

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
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
        # Draw Player
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
