
def getCollisionBounds(obj1):
    leftX = obj1.x
    rightX =obj1.x + obj1.width
    
    highY = obj1.y
    lowY =  obj1.y + obj1.height
    
    return leftX, rightX,  highY, lowY


def is_between(low, high, val):
    if low < val and val < high:
        return True
    return False