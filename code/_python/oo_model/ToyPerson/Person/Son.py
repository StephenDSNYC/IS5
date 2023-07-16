"""

"""

from .Person import Person
from ..Toy.Toy import Toy
from ..Toy.GoodToy import GoodToy
from ..Toy.BrokenToy import BrokenToy


class Son (Person):

    def __init__(self, name, toy_name, durability):
        Person.__init__(self, name)
        if durability > 0:
            self.toy = GoodToy(toy_name, durability)
        else:
            self.toy = BrokenToy(toy_name, durability)
        
    def inspect(self):
        Person.inspect(self)
        print("I am a son.")
    
    def play(self):
        self.inspect()
        print(f'Okay, I will play with my toy {self.toy.name}')
        print(f'I have played with it, and it says:')
        self.toy.play()
        if self.toy.durability == 0:
            self.toy = BrokenToy(self.toy.name, 0)
        print("")
        return self
