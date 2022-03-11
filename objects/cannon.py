from objects.building import Building
import objects.globals as macros


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
        if self.health <= 0:
            return
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
        if shoot == True:
            self.texture = macros.CANNON_SHOT
        else:
            health = float(self.health/macros.CANNON_HEALTH_POINTS)
            if health > 0.5:
                self.texture = macros.CANNON
            elif health > 0.2:
                self.texture = macros.midCannon
            else:
                self.texture = macros.CannonDead

        if self.health <= 0:
            self.texture = macros.BACKGROUND_PIXEL
            self.tile = macros.EMPTY
        if shoot == True:
            self.shoot(village, idx)
        return shoot

    def shoot(self, village, idx):

        if self.health <= 0:
            return
        if idx == -1:
            # shoot the king
            print("SHOOTING THE KING", village.king.health)
            if village.king.health > 0:
                village.king.health -= self.damage
                if village.king.health <= 0:
                    village.king.texture = macros.GRAVE_TILE
                    village.tiles[village.king.position[0]
                                  ][village.king.position[1]] = macros.EMPTY
                    village.king.alive = False

        else:
            # shoot barb
            if idx >= 0:
                # check
                if village.barbarians[idx].health > 0:
                    village.barbarians[idx].health -= self.damage
                    if village.barbarians[idx].health <= 0:
                        village.barbarians[idx].texture = macros.GRAVE_TILE
                        village.barbarians[idx].alive = False
                        village.tiles[village.barbarians[idx].position[0]
                                      ][village.barbarians[idx].position[1]] = macros.EMPTY
