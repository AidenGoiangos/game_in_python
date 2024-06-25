import pygame
from CharachterEntities import *
from UsefulMethods import *

class CaveScreen():
    def __init__(self, width, height, title, player):
        self.width = width
        self.height = height
        self.title = title
        self.running = True
        self.objects = []
        self.counter = 0

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        
        # Set up the clock for a decent framerate
        self.clock = pygame.time.Clock()
        
        # Create a player instance
        self.player = player

        #entities
        self.entity1 = Entity(300, 300, 50, 50, (200, 128, 255))
        self.entity2 = Entity(600, 600, 50, 50, (200, 128, 255))

        #add all entities to screen object list
        self.objects.append(self.entity1)
        self.objects.append(self.entity2)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def quit(self):
        pygame.quit()
        sys.exit()

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
        self.screen.fill((100, 100, 100))
        
        # Draw the player on the screen
        self.player.draw(self.screen)

        #draw entities
        self.entity1.draw(self.screen)
        
        # Update the display
        pygame.display.flip()

    def detect_collisions(self):
        player_leftX, player_rightX,  player_highY, player_lowY = getCollisionBounds(self.player)
        for entit in self.objects:
            entity_leftX, entity_rightX,  entity_highY, entity_lowY = getCollisionBounds(entit)
            if (is_between(entity_leftX, entity_rightX, player_leftX) or is_between(entity_leftX, entity_rightX, player_rightX)) and \
                (is_between(entity_highY, entity_lowY, player_highY) or is_between(entity_highY, entity_lowY, player_lowY)):
                # Collision detected, handle it
                self.handle_collision(entit)
                return 0
        return 1
                

          
    def handle_collision(self, entity):
        # Determine overlap between player and entity
        player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        entity_rect = pygame.Rect(entity.x, entity.y, entity.width, entity.height)
        
        if player_rect.colliderect(entity_rect):
            # Calculate overlap in both X and Y directions
            overlap_x = player_rect.clip(entity_rect).width
            overlap_y = player_rect.clip(entity_rect).height
            
            # Adjust player's position to prevent moving into the entity
            if overlap_x > overlap_y:
                # Adjust vertically
                if self.player.y < entity.y:
                    self.player.y -= overlap_y
                else:
                    self.player.y += overlap_y
            else:
                # Adjust horizontally
                if self.player.x < entity.x:
                    self.player.x -= overlap_x
                else:
                    self.player.x += overlap_x

        

    



        