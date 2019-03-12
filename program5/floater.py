# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage -> Not using this
from prey import Prey
import random
import math

class Floater(Prey): 
    
    def __init__(self,x,y,width,height,angle,speed):
        self.radius = 5
        Prey.__init__(self,x,y,width,height,angle,speed)
        self.randomize_angle()


    def update(self, model):
        if random.randint(0,100) <= 30:
            new_speed = self.get_speed() + random.uniform(-0.5, 0.5)
            if new_speed >= 3.0 and new_speed <= 7.0:
                self.set_speed(new_speed)
            
            new_angle = self.get_angle() + random.uniform(-0.5, 0.5)
            self.set_angle(new_angle)
            
        self.move()

    
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius, self._y-self.radius,
                          self._x+self.radius, self._y+self.radius,
                          fill='red')
