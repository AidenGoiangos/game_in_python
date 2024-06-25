import pygame
import sys
from CharachterEntities import *
from UsefulMethods import *
from MainMap import MainScreen
from Cave import CaveScreen


class gameScreen:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.running = True
        self.screens = []
        self.screen_pointer = 0
        
        self.player = Player(220, 220, 50, 50, (200, 128, 255))
        
        # Initialize Pygame
        pygame.init()
        

        # Set up the displays
        mainScreen = MainScreen(self.width, self.height, self.title, self.player)
        caveScreen = CaveScreen(self.width, self.height, self.title, self.player)
        #add them to the screens list
        self.screens.append(mainScreen)
        self.screens.append(caveScreen)
        

        
    def run(self):
        while self.running:
            x = self.screen_pointer

            self.screens[self.screen_pointer].handle_events()
            self.running = self.screens[self.screen_pointer].running
            self.screen_pointer = self.screens[self.screen_pointer].detect_collisions()

            if self.screen_pointer != x:
                self.screens[self.screen_pointer].player.x = 100
                self.screens[self.screen_pointer].player.y = 100
            self.screens[self.screen_pointer].update()
            
            
            # Cap the frame rate
            self.screens[self.screen_pointer].clock.tick(60)
        self.screens[self.screen_pointer].quit()
    

