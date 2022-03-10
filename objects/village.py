from colorama import Fore, Style, Back
from os import system as sys
import math
from time import *
import globals as macros
from king import King
from townhall import TownHall
from hut import Hut
from cannon import Cannon
from wall import Wall
from barbarians import Barabarian


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
        self.coordCannon = [(macros.COORD_TOWN_HALL[0]-4, macros.COORD_TOWN_HALL[1]+3 + len(self.townhall.drawing[0])), (macros.COORD_TOWN_HALL[0] -
                            4, macros.COORD_TOWN_HALL[1]-4), (macros.COORD_TOWN_HALL[0]+len(self.townhall.drawing) + 3, macros.COORD_TOWN_HALL[1]+3 + len(self.townhall.drawing[0])), (macros.COORD_TOWN_HALL[0]+len(self.townhall.drawing) + 3, macros.COORD_TOWN_HALL[1]-4)]
        self.cannons = [Cannon(x, y) for (x, y) in self.coordCannon]
        self.spawningPoints = [
            (int(macros.VILLAGE_HEIGHT)-2, int(macros.VILLAGE_WIDTH/2)), (int(macros.VILLAGE_HEIGHT/2), int(macros.VILLAGE_WIDTH)-2), (int(macros.VILLAGE_HEIGHT/2), 1)]
        self.coordWall = []
        left = int((macros.VILLAGE_WIDTH/2) - 10) - 3
        right = int(macros.VILLAGE_WIDTH/2 - 10 +
                    len(self.townhall.drawing[0])-1)+3
        top = int(macros.VILLAGE_HEIGHT/2)-3
        bottom = int(macros.VILLAGE_HEIGHT/2 + len(self.townhall.drawing)-1)+3
        self.walls = []
        for i in range(top, bottom+1):
            self.coordWall.append((i, left, 2))
            self.coordWall.append((i, right, 1))

        for j in range(left, right):
            self.coordWall.append((top, j, 3))
            self.coordWall.append((bottom, j, 2))
        left -= 4
        right += 4
        top -= 5
        bottom += 5
        for i in range(top, bottom+1):
            self.coordWall.append((i, left, 1))
            self.coordWall.append((i, right, 2))

        for j in range(left, right):
            self.coordWall.append((top, j, 2))
            self.coordWall.append((bottom, j, 3))

        for (x, y, level) in self.coordWall:
            self.walls.append(Wall(x=x, y=y, level=level))

        self.activeBuildings = []

        # add all the cannons to the list

        for coord in self.coordCannon:
            self.activeBuildings.append(coord)

        # add all the huts to the list

        for coord in self.coordHut:
            self.activeBuildings.append(coord)

        # add all the townhall tiles to the list

        # render the barbarians
        for i in range(macros.COORD_TOWN_HALL[0], macros.COORD_TOWN_HALL[0] + len(self.townhall.drawing)):
            for j in range(macros.COORD_TOWN_HALL[1], macros.COORD_TOWN_HALL[1] + len(self.townhall.drawing[0])):
                self.activeBuildings.append((i, j))

        self.barbarians = []

    def renderScoreBoard(self):

        king_health = self.king.health
        max_health = macros.KING_HEALTH_POINTS
        display_health = int((king_health/max_health) *
                             macros.DISPLAY_WIDTH-macros.VILLAGE_WIDTH)

        for i in range(display_health):
            self.village[3
                         ][macros.VILLAGE_WIDTH+i] = Back.RED+' ' + Style.RESET_ALL

    def drawWalls(self):
        for i in self.walls:
            self.village[i.position[0]][i.position[1]] = i.texture
            self.tiles[i.position[0]][i.position[1]] = i.tile

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

        # render the main town hall
        for row in range(0, len(self.townhall.drawing)):
            for col in range(0, len(self.townhall.drawing[row])):
                if self.townhall.health > 0:
                    self.tiles[macros.COORD_TOWN_HALL[0] +
                               row][macros.COORD_TOWN_HALL[1] + col] = macros.TOWN_HALL
                    self.village[macros.COORD_TOWN_HALL[0]+row][macros.COORD_TOWN_HALL[1] +
                                                                col] = Back.GREEN + Fore.RED + self.townhall.drawing[row][col] + Style.RESET_ALL
                else:
                    self.tiles[macros.COORD_TOWN_HALL[0] +
                               row][macros.COORD_TOWN_HALL[1] + col] = macros.EMPTY
                    self.village[macros.COORD_TOWN_HALL[0]+row][macros.COORD_TOWN_HALL[1] +
                                                                col] = macros.BACKGROUND_PIXEL
                    # render walls around the townhall
        self.drawWalls()

        # render the village
        self.renderScoreBoard()

        # render the huts
        itr = 0
        for (x, y) in self.coordHut:
            self.village[x][y] = self.huts[itr].texture
            self.tiles[x][y] = self.huts[itr].tile
            itr += 1
        itr = 0
        # render the cannons
        for (x, y) in self.coordCannon:
            self.village[x][y] = self.cannons[itr].texture
            self.tiles[x][y] = self.cannons[itr].tile
            itr += 1
        # render the spawning points
        for (x, y) in self.spawningPoints:
            self.village[x][y] = macros.RED_PIXEL

        # render the king
        self.village[self.king.position[0]
                     ][self.king.position[1]] = macros.KING_TILE

        # render barbarians
        for barbarians in self.barbarians:
            self.village[barbarians.position[0]
                         ][barbarians.position[1]] = barbarians.texture
       
        # finally draw the village

        for row in range(macros.DISPLAY_HEIGHT):
            for col in range(macros.DISPLAY_WIDTH):
                print(self.village[row][col],
                      end='\n' if col == macros.DISPLAY_WIDTH-1 else '')

    def moveBarbs(self):
        print("Hi")
        for barbs in self.barbarians:
            barbs.move_barbarian(self)
