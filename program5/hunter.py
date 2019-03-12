# Hunter is derived both from the Mobile_Simulton/Pulsator classes; each updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    
    def __init__(self,x,y,width,height,angle,speed):
        Pulsator.__init__(self,x,y,width,height)
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)
        self.vision = 200
        self.randomize_angle()
        
        
    def update(self, model):
        Pulsator.update(self, model)
        Mobile_Simulton.move(self)
        
        prey_set = model.find(lambda x: isinstance(x, Prey))
        can_see = set()
        for prey in prey_set:
            distance = ( (self._x - prey._x)**2 + (self._y - prey._y)**2 )**0.5
            if distance < self.vision:
                can_see.add(prey)
        
        nearby = []
        for prey in can_see:
            distance = ( (self._x - prey._x)**2 + (self._y - prey._y)**2 )**0.5
            nearby.append( (prey, distance) )
        if len(nearby) > 0:
            closest = sorted(nearby, key=lambda x: x[1])[0]
            self.set_angle( atan2( (closest[0]._y - self._y), (closest[0]._x - self._x) ) )
    
    
    
