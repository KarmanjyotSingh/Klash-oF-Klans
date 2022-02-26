# define the troop class here

from numpy import True_


class Troop():

    def __init__(self, x, y, dimensions=(1, 1), health=50, damage=10):

        # specify the position of the troop
        # the position at which the troop is spawn

        self.position = (x, y)
        # set the dimensions of the troop
        self.width = dimensions[0]
        self.height = dimensions[1]
        # boolean expression for alive
        self.alive = True
        # health for the troop
        self.health = health
        # set the damage for the player
        self.damage = damage
        # set the movement speed for the troop
        self.movement_speed = 10

    def set_position(self, x, y):
        self.position = (x, y)

    def resize(self, dimensions=(30, 30)):
        self.width = dimensions[0]
        self.height = dimensions[1]

    def get_position(self):
        return self.position

    def is_alive(self):
        return self.health > 0
