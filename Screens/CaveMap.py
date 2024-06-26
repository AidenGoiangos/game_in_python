import pygame
from CharachterEntities import *
from UsefulMethods import *
import sys
class CaveScreen():
    def __init__(self, width, height, title, player, score_val):
        self.width = width
        self.height = height
        self.title = title
        self.running = True
        self.objects = []
        self.counter = 0
        self.score_value = score_val


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
        self.font = pygame.font.Font('freesansbold.ttf', 32)


    def show_score(self, score_value):
        self.score_value = score_value
        self.score = self.font.render("Score : " + str(self.score_value), True, (255, 255, 255))
        self.screen.blit(self.score, (10, 10))




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
        self.entity2.draw(self.screen)

        self.show_score(self.score_value)


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
       #real method under useful, unneeded
        pass

        

    



        