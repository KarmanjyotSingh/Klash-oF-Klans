from colorama import Fore, Style, Back
from os import system as sys
import math
from time import *
import globals as macros
from king import King


class Village():
    def __init__(self):
        # specify the village ka dimension
        # using village as a 100 x 100 grid
        self.width = macros.VILLAGE_WIDTH
        self.height = macros.VILLAGE_HEIGHT  
        self.village = [[macros.BACKGROUND_PIXEL for i in range(self.width)]
                        for j in range(self.height)]
        # initialize the village tiles
        self.tiles = [[0 for i in range(self.width)]
                      for j in range(self.height)]
        self.king = King(self.width-1, 0)

    def render(self):
        # initialize the village
        sys('clear')
        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width-1 or i == 0 or i == self.height-1:
                    self.village[i][j] = macros.BORDER_PIXEL
                else:
                    self.village[i][j] = macros.BACKGROUND_PIXEL
        
        self.village[self.king.position[1]
                     ][self.king.position[0]] = macros.KING_TILE

        # render the village
        for row in range(self.height):
            for col in range(self.width):
                print(self.village[row][col],
                      end='\n' if col == self.width-1 else '')

       
