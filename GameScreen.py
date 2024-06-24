import pygame
import sys
from CharachterEntities import *

class gameScreen:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.running = True
        
        # Initialize Pygame
        pygame.init()
        
        # Set up the display
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        
        # Set up the clock for a decent framerate
        self.clock = pygame.time.Clock()
        
        # Create a player instance
        self.player = Player(100, 100, 50, 50, (0, 128, 255))

        #entities
        self.entity1 = Entity(300, 300, 50, 50, (0, 128, 255))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        # Get the set of keys pressed and check for user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(1, 0)
        if keys[pygame.K_UP]:
            self.player.move(0, -1)
        if keys[pygame.K_DOWN]:
            self.player.move(0, 1)
        
        # Fill the screen with white
        self.screen.fill((1, 100, 100))
        
        # Draw the player on the screen
        self.player.draw(self.screen)

        #draw entities
        self.entity1.draw(self.screen)
        
        # Update the display
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            # Cap the frame rate
            self.clock.tick(60)
        self.quit()
    
    def quit(self):
        pygame.quit()
        sys.exit()
