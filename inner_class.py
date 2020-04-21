#!/usr/bin/env python
class Head:
    def talk(self):
        return 'talking...'


class Brain:
    def think(self):
        return 'thinking...'
class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
        self.brain = self.Brain()





if __name__ == '__main__':
    guido = Human()
    print(guido.name)
    print(guido.head.talk())
    print(guido.brain.think())