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

    
    def moveKing(self, char, village):
        #  just to check health bar 
        if char == '1':
            self.health -= int(1)
        elif char == 'w':
            # is present at the top edge of the game
            if self.position[0] > 0:
                if village.tiles[self.position[0]-1][self.position[1]] == macros.EMPTY:
                    self.position = (self.position[0] - 1, self.position[1])
        elif char == 's':
            if self.position[0] < village.height - 1:
                if village.tiles[self.position[0]+1][self.position[1]] == macros.EMPTY:
                    self.position = (self.position[0] + 1, self.position[1])
        elif char == 'a':
            if self.position[1] > 0:
                if village.tiles[self.position[0]][self.position[1]-1] == macros.EMPTY:
                    self.position = (self.position[0], self.position[1] - 1)
        elif char == 'd':
            if self.position[1] < village.width - 1:
                if village.tiles[self.position[0]][self.position[1]+1] == macros.EMPTY:
                    self.position = (self.position[0], self.position[1] + 1)
        # elif char == ' ':
