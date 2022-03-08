from colorama import Fore, Style, Back
from os import system as sys
import math
from time import *
import globals as macros
from king import King
from townhall import TownHall
from hut import Hut
from cannon import Cannon


class Village():

    def __init__(self):
        # specify the village ka dimension
        self.width = macros.VILLAGE_WIDTH
        self.height = macros.VILLAGE_HEIGHT
        self.village = [[macros.BACKGROUND_PIXEL for i in range(macros.DISPLAY_WIDTH)]
                        for j in range(macros.DISPLAY_HEIGHT)]
        # initialize the village tiles
        self.tiles = [[0 for i in range(macros.DISPLAY_WIDTH)]
                      for j in range(macros.DISPLAY_HEIGHT)]
        self.king = King(10, 1)
        self.townhall = TownHall(3, 24)
        self.coordHut = [(1, 1), (1, macros.VILLAGE_WIDTH-2), (macros.VILLAGE_HEIGHT -
                                                               2, macros.VILLAGE_WIDTH-2), (macros.VILLAGE_HEIGHT-2, 1), (1, int(macros.VILLAGE_WIDTH/2))]
        self.huts = [Hut(x, y) for (x, y) in self.coordHut]
        self.coordCannon = [(macros.COORD_TOWN_HALL[0]-4, macros.COORD_TOWN_HALL[1]+5 + len(self.townhall.drawing[0])), (macros.COORD_TOWN_HALL[0] -
                            4, macros.COORD_TOWN_HALL[1]-4), (macros.COORD_TOWN_HALL[0]+len(self.townhall.drawing) + 3, macros.COORD_TOWN_HALL[1]+5 + len(self.townhall.drawing[0])), (macros.COORD_TOWN_HALL[0]+len(self.townhall.drawing) + 3, macros.COORD_TOWN_HALL[1]-4)]
        self.cannons = [Cannon(x, y) for (x, y) in self.coordCannon]
        self.spawningPoints = [
            (int(macros.VILLAGE_HEIGHT)-2, int(macros.VILLAGE_WIDTH/2)), (int(macros.VILLAGE_HEIGHT/2), int(macros.VILLAGE_WIDTH)-2), (int(macros.VILLAGE_HEIGHT/2), 1)]

    def renderScoreBoard(self):

        king_health = self.king.health
        max_health = macros.KING_HEALTH_POINTS
        display_health = int((king_health/max_health) *
                             macros.DISPLAY_WIDTH-macros.VILLAGE_WIDTH)

        for i in range(display_health):
            self.village[3
                         ][macros.VILLAGE_WIDTH+i] = Back.RED+' ' + Style.RESET_ALL

    def drawWalls(self, top, bottom, left, right, level=1):

        wall_level = macros.WALL_LEVEL_1
        tile_level = macros.TILE_WALL_LEVEL_1
        if level == 2:
            wall_level = macros.WALL_LEVEL_2
            tile_level = macros.TILE_WALL_LEVEL_2
        elif level == 3:
            wall_level = macros.WALL_LEVEL_3
            tile_level = macros.TILE_WALL_LEVEL_3

        for i in range(top, bottom+1):
            self.village[i][left] = wall_level
            self.village[i][right] = wall_level
            self.tiles[i][left] = tile_level
            self.tiles[i][right] = tile_level

        for j in range(left, right):
            self.village[top][j] = wall_level
            self.village[bottom][j] = wall_level
            self.tiles[top][j] = tile_level
            self.tiles[bottom][j] = tile_level

    def render(self):
        # initialize the village
        sys('clear')

        for i in range(macros.DISPLAY_HEIGHT):
            for j in range(macros.DISPLAY_WIDTH):
                # render the game border
                if j < self.width and (j == 0 or j == self.width-1 or i == 0 or i == self.height-1):
                    self.village[i][j] = macros.BORDER_PIXEL
                    self.tiles[i][j] = -1
                else:
                    # the main score card area
                    if j >= self.width:
                        self.village[i][j] = macros.SCORECARD_PIXEL
                    else:
                        # background pixel
                        self.village[i][j] = macros.BACKGROUND_PIXEL

        # render the king
        self.village[self.king.position[0]
                     ][self.king.position[1]] = macros.KING_TILE

        # render the main town hall
        for row in range(0, len(self.townhall.drawing)):
            for col in range(0, len(self.townhall.drawing[row])):
                self.tiles[macros.COORD_TOWN_HALL[0] +
                           row][macros.COORD_TOWN_HALL[1] + col] = macros.TOWN_HALL
                self.village[macros.COORD_TOWN_HALL[0]+row][macros.COORD_TOWN_HALL[1] +
                                                            col] = Back.GREEN + Fore.RED + self.townhall.drawing[row][col] + Style.RESET_ALL

        # render walls around the townhall
        left = int((macros.VILLAGE_WIDTH/2) - 10) - 3
        right = int(macros.VILLAGE_WIDTH/2 - 10 +
                    len(self.townhall.drawing[row])-1)+3
        top = int(macros.VILLAGE_HEIGHT/2)-3
        bottom = int(macros.VILLAGE_HEIGHT/2 + len(self.townhall.drawing)-1)+3

        self.drawWalls(top, bottom, left, right)

        # render the cannons

        # render the village
        self.renderScoreBoard()

        left -= 4
        right += 4
        top -= 5
        bottom += 5
        self.drawWalls(top, bottom, left, right, 2)

        # render the huts
        for (x, y) in self.coordHut:
            self.village[x][y] = macros.HUT
            self.tiles[x][y] = macros.HUT_TILE

        for (x, y) in self.coordCannon:
            self.village[x][y] = macros.CANNON
            self.tiles[x][y] = macros.CANNON_TILE
        for (x, y) in self.spawningPoints:
            self.village[x][y] = macros.RED_PIXEL
        # finally draw the village
        for row in range(macros.DISPLAY_HEIGHT):
            for col in range(macros.DISPLAY_WIDTH):
                print(self.village[row][col],
                      end='\n' if col == macros.DISPLAY_WIDTH-1 else '')
