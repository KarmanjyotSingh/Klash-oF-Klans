from troop import Troop
import globals as macros
import math
# define the barbarian class
# inherit from the troop class
# set the troop type to barbarian


class Barabarian(Troop):
    def __init__(self, x, y, health=macros.BARBARIAN_HEALTH_POINTS, damage=macros.BARBARIAN_DAMAGE, speed=macros.BARBARIAN_MOVEMENT_SPEED):

        super().__init__(x, y, (1, 1), health, damage, speed=1)
        self.troop_type = macros.BARBARIAN
        self.texture = macros.BARBARIAN_TILE
        self.tile = macros.BARB

    def distance(self, coord):
        x = coord[0]
        y = coord[1]
        # using manhatten distance for finding up the nearest building !
        return abs(self.position[0] - x) + abs(self.position[1] - y)

    def move_barbarian(self, village):
        # set the game boundary variables
        top = 1
        left = 1
        right = village.width - 1
        bottom = village.height - 1

        # look for the building to move to move
        # to the building

        minDist = 100000
        building = (-1, -1)
        for coordinate in village.activeBuildings:
            dist = self.distance(coordinate)
            if dist < minDist:
                minDist = dist
                building = coordinate
        # just add the barbarian to the screen , meaning game won
        if building == (-1, -1):
            return
        # got the building make the barbarian move towards it

        direction = (building[0],
                     building[1])

        for i in range(0, 3):
            for j in range(0, 3):
                dist = self.distance((building[0]-1 + i, building[1]-1 + j))
                if dist < minDist:
                    minDist = dist
                    direction = (building[0]-1 + i, building[1]-1 + j)

        direction = (direction[0] - self.position[0],
                     direction[1] - self.position[1])

        if direction[1] == 0:
            # it is in same horizontal level
            if direction[0] > 0:
                # move down
                steps = 0
                for i in range(1, self.movement_speed + 1):
                    if self.position[0] + i < bottom and village.tiles[self.position[0] + i][self.position[1]] == macros.EMPTY:
                        steps += 1
                    else:
                        break
                if self.position[0] + i < bottom and self.position[0] + steps > bottom:
                    self.set_position(bottom, self.position[1])
                    return

                self.set_position(
                    self.position[0] + steps, self.position[1])

            elif direction[0] < 0:
                # move up
                steps = 0
                for i in range(1, self.movement_speed + 1):

                    if self.position[0]-i > 1 and village.tiles[self.position[0] - i][self.position[1]] == macros.EMPTY:
                        steps += 1
                    else:
                        break
                if self.position[0] - steps < top:
                    self.set_position(top, self.position[1])
                    return
                self.set_position(
                    self.position[0] - steps, self.position[1])

        elif direction[1] > 0:
            # move right

            steps = 0
            for i in range(1, self.movement_speed + 1):
                if self.position[1] + i < right and village.tiles[self.position[0]][self.position[1] + i] == macros.EMPTY:
                    steps += 1
                else:
                    break
            if self.position[1] + steps > right:

                self.set_position(
                    self.position[0], right)
                steps = 0
                return
            self.set_position(
                self.position[0], self.position[1]+steps)
        else:
          # move left
            steps = 0
            for i in range(1, self.movement_speed + 1):
                if self.position[1] - i < left and village.tiles[self.position[0]][self.position[1] - i] == macros.EMPTY:
                    steps += 1
                else:
                    break
            if self.position[1] - steps < left:
                self.set_position(self.position[0], left)
                return

            self.set_position(
                self.position[0], self.position[1]-steps)

    def attackBarbarian():
        pass

    def set_position(self, x, y):
        self.position = (x, y)

    def get_position(self):
        return self.position
