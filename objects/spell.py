import enum


from enum import Enum


class SpellType(Enum):
    Rage = 1
    Heal = 2


class Spell():
    
    def __init__(self, type=1 , radius = 1):
        # define the spell type
        self.type = SpellType[type]
        # define the radius of the spell
        self.radii = radius
