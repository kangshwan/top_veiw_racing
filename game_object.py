import point_n_rect as pnr

class Gameobject(Rectangle):
    def __init__(self, width, height):
        # args should add in (x,y) tuple
        self.position = pnr.Point()
        self.hitbox = pnr.Rectangle(self.position, width, height)
    
    def intersects(self, other):
        #is this object is collide by other game object?