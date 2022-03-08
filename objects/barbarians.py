from troop import Troop
import globals as macros
# define the barbarian class
# inherit from the troop class
# set the troop type to barbarian


class Barabarian(Troop):
    def __init__(self, x, y, health=macros.BARBARIAN_HEALTH_POINTS, damage=macros.BARBARIAN_DAMAGE, speed=macros.BARBARIAN_MOVEMENT_SPEED):
        super().__init__(x, y, (1, 1), health, damage, speed)

        self.troop_type = macros.BARBARIAN

    def move_barbarian(self, village):
        pass
