# Black_Hole is derived from the Simulton: each updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import math


class Black_Hole(Simulton):
     
    def __init__(self,x,y,width,height):
        self.radius = 10
        Simulton.__init__(self,x,y,width,height)


    def update(self, model):
        prey_set = model.find(lambda x: isinstance(x, Prey))
        eaten = set()
        
        for prey in prey_set:
            if self.__contains__(prey) == True:
                eaten.add(prey)

        for prey in eaten:
            model.remove(prey)
            
        return eaten

    
    def display(self,canvas):
       canvas.create_oval(self._x-(self._width/2), self._y-(self._height/2),
                          self._x+(self._width/2), self._y+(self._height/2),
                          fill='black')
       
       
    def __contains__(self, prey):
        distance = ( (self._x - prey._x)**2 + (self._y - prey._y)**2 )**0.5
        if distance < (self._width/2) or distance < (self._height/2):
            return True
        return False
    
