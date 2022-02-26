# A king is a type of troop
from troop import Troop
import globals as macros
from input import *
# define king as Troop , but control the king's position by the user
# control king using wasd keys
# space bar for using power up
# f for attack


class King(Troop):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.troop_type = macros.KING
        self.health = macros.KING_HEALTH_POINTS
        self.damage = macros.KING_DAMAGE
        self.movement_speed = macros.KING_MOVEMENT_SPEED

    def moveKing(self, village):
        char = input_to(Get().__call__)
        
        if char == 'w':
            if self.position[1] > 0:
                self.position = (self.position[0], self.position[1] - 1)
        elif char == 'a':
            if self.position[0] > 0:
                self.position = (self.position[0] - 1, self.position[1])
        elif char == 's':
            if self.position[1] < village.height - 1:
                self.position = (self.position[0], self.position[1] + 1)
        elif char == 'd':
            if self.position[0] < village.width - 1:
                self.position = (self.position[0] + 1, self.position[1]) 
        return char
