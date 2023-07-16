"""

"""

from .Toy import Toy

class BrokenToy (Toy):

    def play(self):
        print('Ooch!  I am broken!')
        Toy.play(self)
