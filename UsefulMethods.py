import pygame
def getCollisionBounds(obj1):
    leftX = obj1.x
    rightX =obj1.x + obj1.width
    
    highY = obj1.y
    lowY =  obj1.y + obj1.height
    
    return leftX, rightX,  highY, lowY


def is_between(low, high, val):
    if low <= val and val <= high:
        return True
    return False

def draw_hitbox(screen, obj):
    pygame.draw.line(screen, (255, 0, 0), (obj.x, obj.y), (obj.x, obj.y + obj.height))
    pygame.draw.line(screen, (255, 0, 0), (obj.x, obj.y), (obj.x + obj.width, obj.y))
    pygame.draw.line(screen, (255, 0, 0), (obj.x, obj.y + obj.height), (obj.x + obj.width, obj.y + obj.height))
    pygame.draw.line(screen, (255, 0, 0), (obj.x + obj.width, obj.y), (obj.x + obj.width, obj.y + obj.height))






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
