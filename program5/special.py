# A Special is Prey; it updates by moving in the opposite direction 
#    of the closest Predator (Black_Hole and its children),
#    but only if the Predator is within it's short vision.
#    It displays as a yellow square with a radius of 5 (width/height 10).
#    It also has a speed of 10 rather than 5.

from ball import Ball
from blackhole import Black_Hole
from math import atan2


class Special(Ball):  
       
    def __init__(self,x,y,width,height,angle,speed):
        Ball.__init__(self,x,y,width,height,angle,speed)
        self.vision = 50
        self.randomize_angle()
        

    def update(self, model):
        Ball.update(self, model)
        
        predator_set = model.find(lambda x: isinstance(x, Black_Hole))
        can_see = set()
        for pred in predator_set:
            distance = ( (self._x - pred._x)**2 + (self._y - pred._y)**2 )**0.5
            if distance < self.vision:
                can_see.add(pred)
        
        distances = set()
        for pred in can_see:
            distance = ( (self._x - pred._x)**2 + (self._y - pred._y)**2 )**0.5
            distances.add( (pred, distance) )
        if len(distances) > 0:
            closest = sorted(distances, key=lambda x: x[1])[0]
            self.set_angle( atan2( (self._y - closest[0]._y), (self._x - closest[0]._x) ) )

    
    def display(self,canvas):
       canvas.create_rectangle(self._x-self.radius, self._y-self.radius,
                               self._x+self.radius, self._y+self.radius,
                               fill='yellow')
