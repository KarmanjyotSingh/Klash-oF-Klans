import enum


from enum import Enum
import globals as macros


class SpellType(Enum):
    Rage = 1
    Heal = 2


class Spell():

    def __init__(self):
        # define the spell type
        self.type = "spell"
        # define the radius of the spell
        # effect
        self.factorSpeed = 0
        self.factorHealth = 0


class HealingSpell(Spell):

    def __init__(self, type=1):
        super().__init__()
        self.type = "heal"
        self.factorHealth = 1.5

    def doHeal(self, village):
        # heal the king first
        if village.king.health > 0:
            health = village.king.health
            health *= self.factorHealth

            if health > macros.KING_HEALTH_POINTS:
                village.king.health = macros.KING_HEALTH_POINTS
            else:
                village.king.health = health

        # heal the troops

        for barbs in village.barbarians:
            if barbs.alive == True:
                health = barbs.health
                health *= 1.5
                if health > macros.BARBARIAN_HEALTH_POINTS:
                    barbs.health = macros.BARBARIAN_HEALTH_POINTS
                else:
                    barbs.health = health


class RageSpell(Spell):

    def __init__(self, type=1):
        super().__init__()
        self.type = "rage"
        self.factorSpeed = 2

    def doRage(self, village):
        # rage king first
        if village.king.health > 0:
            speed = village.king.movement_speed
            speed *= self.factorSpeed
            village.king.movement_speed = speed
            village.king.damage *= self.factorSpeed

        # rage the troops
        for barb in village.barbarians:
            if barb.alive == True:
                speed = barb.movement_speed
                speed *= self.factorSpeed
                barb.movement_speed = speed
                barb.damage *= self.factorSpeed
