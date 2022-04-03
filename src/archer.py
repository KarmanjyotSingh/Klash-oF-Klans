from src.troop import Troop
import src.globals as macros


class Archer(Troop):

    def __init__(self, x, y, health=macros.BARBARIAN_HEALTH_POINTS/2, damage=macros.BARBARIAN_DAMAGE/2, speed=macros.BARBARIAN_MOVEMENT_SPEED*2):

        super().__init__(x, y, (1, 1), health, damage, speed)
        self.troop_type = 'A'
        self.texture = macros.ARCHER_TILE
        self.tile = macros.ARCH
        self.attack_range = macros.ARCHER_ATTACK_RANGE

    def set_position(self, x, y):
        self.position = (x, y)

    def get_position(self):
        return self.position

    def distance(self, coord):
        x = coord[0]
        y = coord[1]
        # using manhatten distance for finding up the nearest building !
        return abs(self.position[0] - x) + abs(self.position[1] - y)

    def move_archer(self, village):

        if self.health <= 0:
            self.alive = False
            return

        top = 1
        left = 1
        right = village.width - 1
        bottom = village.height - 1

        # look for the nearest building first

        minDist = 100000
        building = (-1, -1)

        # iterate over the coordinates of the active buildings

        for coordinate in village.activeBuildings:
            dist = self.distance(coordinate)
            if dist < minDist:
                if village.tiles[coordinate[0]][coordinate[1]] == macros.EMPTY:
                    continue
                minDist = dist
                building = coordinate
        # just add the barbarian to the screen , meaning game won
        if building == (-1, -1):
            return True
        # got the building make the barbarian move towards it

        direction = (building[0],
                     building[1])

        topBuild = building[0]-self.attack_range
        leftBuild = building[1]-self.attack_range
        rightBuild = building[1]+self.attack_range
        bottomBuild = building[0]+self.attack_range
        if topBuild < top:
            topBuild = top
        if leftBuild < left:
            leftBuild = left
        if rightBuild > right:
            rightBuild = right
        if bottomBuild > bottom:
            bottomBuild = bottom

        for i in range(topBuild, bottomBuild+1):
            for j in range(leftBuild, rightBuild+1):
                dist = self.distance((i, j))
                if dist < minDist:
                    minDist = dist
                    direction = (i, j)

        # got the point to approach in the direction

        direction = (direction[0] - self.position[0],
                     direction[1] - self.position[1])
        
        
