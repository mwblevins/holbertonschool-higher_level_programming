#!/usr/bin/python3
"""Live code over inheritance in Python"""


class CircleOfLife(object):
    """Base Class""" #Parent#
    
    alive = True
    
    AllAnimals = ()
    def __init__(self, name=None, age=None, size=None):
        """Init"""
        
        self.name = name
        self.age = age
        self.size = size

    def eat(self):
        """eat method"""
        
        print(self.name + " is grubbin")
    
    def sleep(self):
        
        print(self.name + " is snoozing")
        
    @classmethod #keep track#
    def logAnimal(cls, name):
        CircleOfLife.AllAnimals[name] = cls.__name__
        

class Mammals(CircleOfLife):
    """Mammal class""" #Child#
    
    def __init__(self, name=None, age=None, size=None, bipedal=None):
        super().__init__(name, age, size)
        self.bipedal = bipedal
        super().logAnimal(name)
        
class SeaCreatures(CircleOfLife):
    """SeaCreature class""" #Child#
    
    def __init__(self, name=None, age=None, size=None, swimSpeed=None):
        super().__init__(name, age, size)
        self.swimSpeed = swimSpeed
        super().logAnimal(name)
        
        
        
puppy1 = Mammals('Rex', 1, 'smol', False)
puppy1.eat()
print(CircleOfLife.AllAnimals)

seahorse1 = SeaCreatures('Betty', 102, 'Medium', 'Super Fast')
seahorse1.eat()
seahorse1.sleep()
print(CircleOfLife.AllAnimals)