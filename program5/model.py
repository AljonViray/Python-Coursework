import controller, sys
import model   # Pass a reference to this module to each update call in update_all

# Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special 


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
simultons = set()
selection = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())


#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons, selection
    running = False
    cycle_count = 0
    simultons = set()
    selection = None


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, running
    running = True
    update_all()
    running = False

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selection
    selection = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global selection, simultons
    if selection == 'Remove': #Need to finish
        for sim in simultons.copy():
            if sim.contains( (x,y) ):
                remove(sim)
    elif selection == 'Ball':
        add( Ball(x,y,5,5,0,5) )
    elif selection == 'Floater':
        add( Floater(x,y,5,5,0,5) )
    elif selection == 'Black_Hole':
        add( Black_Hole(x,y,20,20) )
    elif selection == 'Pulsator':
        add( Pulsator(x,y,20,20) )
    elif selection == 'Hunter':
        add( Hunter(x,y,20,20,0,5) )
    elif selection == 'Special':
        add( Special(x,y,5,5,0,10) )
    

#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global simultons
    result = set()
    for sim in simultons:
        if p(sim) == True:
            result.add(sim)
    return result


#call update for each simulton in the simulation (pass the model as an argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count, simultons
    if running:
        cycle_count += 1
        for sim in simultons.copy():
            sim.update(model)
            


#delete from the canvas every simulton being simulated; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    global simultons
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for sim in simultons:
        sim.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" simultons/"+str(cycle_count)+" cycles")
