# A king is a type of troop
from troop import Troop
import globals as macros
from input import *
# define king as Troop , but control the king's position by the user
# control king using wasd keys
# space bar for using power up
# f for attack
attackRadius = 5


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
        elif char == ' ':
            self.attackKing(village)

    def attackKing(self, village):
        # axe vala attack , in radius of 5 tiles
        x = int(self.position[0])
        print(x)
        y = int(self.position[1])
        print(y)
        attackTh = False
        for i in range(x-attackRadius, x+attackRadius+1):
            for j in range(y-attackRadius, y+attackRadius+1):
                # check if it lies inside the box frame
                if i >= 0 and i < village.height and j >= 0 and j < village.width:
                    # it can be a cannon object , or hut , or townhall , or walls , loop over them
                    if (i, j) in village.coordHut:
                        idx = village.coordHut.index((i, j))
                        village.huts[idx].health -= self.damage
                        if village.huts[idx].health <= 0:
                            village.village[village.huts[idx].position[0]
                                            ][village.huts[idx].position[1]] = macros.EMPTY
                            village.huts[idx].texture = macros.BACKGROUND_PIXEL
                            village.huts[idx].tile = macros.EMPTY
                            if (village.huts[idx].position[0], village.huts[idx].position[1]) in village.activeBuildings:
                                village.activeBuildings.remove(
                                    (village.huts[idx].position[0], village.huts[idx].position[1]))

                    # check for townhall
                    if attackTh == False and i >= macros.COORD_TOWN_HALL[0] and i < macros.COORD_TOWN_HALL[0] + len(village.townhall.drawing) and j >= macros.COORD_TOWN_HALL[1] and j < macros.COORD_TOWN_HALL[1] + len(village.townhall.drawing[0]):
                        village.townhall.health -= self.damage
                        # attack the townhall
                        if village.townhall.health <= 0:
                            if (i, j) in village.activeBuildings:
                                village.activeBuildings.remove((i, j))
                        attackTh = True

                    # check for cannons

                    if(i, j) in village.coordCannon:
                        idx = village.coordCannon.index((i, j))
                        village.cannons[idx].health -= self.damage
                        if village.cannons[idx].health <= 0:
                            village.cannons[idx].texture = macros.BACKGROUND_PIXEL
                            village.cannons[idx].tile = macros.EMPTY
                            if (village.cannons[idx].position[0], village.cannons[idx].position[1]) in village.activeBuildings:
                                village.activeBuildings.remove(
                                    (village.cannons[idx].position[0], village.cannons[idx].position[1]))

                    # check for walls
                    for itr in range(0, len(village.coordWall)):
                        if i == village.coordWall[itr][0] and j == village.coordWall[itr][1]:
                            # print(itr)
                            # print(len(village.walls))
                            village.walls[itr].health -= self.damage
                            # remove the wall
                            if village.walls[itr].health <= 0:
                                village.walls[itr].texture = macros.BACKGROUND_PIXEL
                                village.walls[itr].tile = macros.EMPTY
