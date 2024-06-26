import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        


    

class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)








def getCollisionBounds(obj1):
    leftX = obj1.x
    rightX =obj1.x + obj1.width
    
    highY = obj1.y
    lowY =  obj1.y + obj1.height
    
    return leftX, rightX,  highY, lowY
