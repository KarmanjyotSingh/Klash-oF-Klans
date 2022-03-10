from building import Building
import globals as macros


class Cannon(Building):

    def __init__(self, x, y, size=10, health=10):
        # create an instance of the cannon object
        super().__init__(x, y, size, macros.CANNON_HEALTH_POINTS)
        # define damage attribute for the cannon
        self.damage = macros.CANNON_DAMAGE
        # define the last shot time
        self.last_shot = 0
        self.texture = macros.CANNON
        self.tile = macros.CANNON_TILE

    def distance(self, coord):
        # using manhatten distance for finding up the nearest building !
        return abs(self.position[0] - coord[0]) + abs(self.position[1] - coord[1])

    def find_target(self, village):
        # define a radius of tiles around the cannon ]
        # look for barbarian or the king object , choose the one which is nearest
        shoot = False
        dist = 100000
        idx = -2
        itr = 0
        for barb in village.barbarians:
            if barb.health > 0:
                if abs(self.position[0]-barb.position[0]) <= macros.CANNON_RADIUS and abs(self.position[1]-barb.position[1]) <= macros.CANNON_RADIUS:
                    shoot = True
                    mindist = self.distance(barb.position)
                    if mindist < dist:
                        dist = mindist
                        idx = itr
                itr += 1
        # look for king
        if village.king.health > 0:
            # check if in shooting range
            if abs(self.position[0]-village.king.position[0]) <= macros.CANNON_RADIUS and abs(self.position[1]-village.king.position[1]) <= macros.CANNON_RADIUS:
                shoot = True
                mindist = self.distance(village.king.position)
                if mindist < dist:
                    dist = mindist
                    idx = -1
        self.texture = macros.CANNON_SHOT if shoot else macros.CANNON
        if shoot == True:
            self.shoot(village, idx)
        return shoot

    def shoot(self, village, idx):
        if idx == -1:
            # shoot the king
            village.king.health -= self.damage
            if village.king.health <= 0:
                village.king.texture = macros.GRAVE_TILE
                village.tiles[village.king.position[0]
                             ][village.king.position[1]] = macros.EMPTY

        else:
            # shoot barb
            if idx >= 0:
                # check 
                village.barbarians[idx].health -= self.damage
                if village.barbarians[idx].health <= 0:
                    village.barbarians[idx].texture = macros.GRAVE_TILE
                    village.tiles[village.barbarians[idx].position[0]
                                 ][village.barbarians[idx].position[1]] = macros.EMPTY

