"""

"""

class Toy:
    def __init__(self, name, durability) -> None:
        self.name = name
        self.durability = durability
    
    def play(self):
        if self.durability > 0:
            print('Okay, got it!  Have fun!')
            self.durability -= 1
            if self.durability > 0:
                print(f'I can play {self.durability} more times.')
            else:
                print('I am done')
        else:
            print('Sorry, I cannot play anymore!')