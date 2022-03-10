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
