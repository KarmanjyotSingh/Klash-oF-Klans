from colorama import Fore, Style, Back

DISPLAY_WIDTH = 210
DISPLAY_HEIGHT = 50
# village macros
VILLAGE_WIDTH = 170
VILLAGE_HEIGHT = 50
BORDER_PIXEL = Back.WHITE + ' ' + Style.RESET_ALL
BACKGROUND_PIXEL = Back.GREEN + ' ' + Style.RESET_ALL
SCORECARD_PIXEL = Back.BLUE + ' ' + Style.RESET_ALL
RED_PIXEL = Back.RED + ' ' + Style.RESET_ALL
HUT = Back.LIGHTBLACK_EX + 'H' + Style.RESET_ALL
CANNON = Fore.RED + Back.LIGHTWHITE_EX + 'C' + Style.RESET_ALL
# building coordinates
COORD_HUTS = []
# store the top left corner baki can be done using manipulations
COORD_TOWN_HALL = (int(VILLAGE_HEIGHT/2), int(VILLAGE_WIDTH/2)-10)

# building health points
TOWN_HALL_HEALTH = 1000


# tile map code
EMPTY = 0


# define the characters
KING = 'K'
KING_HEALTH_POINTS = 1000
KING_DAMAGE = 10
KING_MOVEMENT_SPEED = 10
KING_TILE = Fore.RED + "K" + Style.RESET_ALL
BARBARIAN = 'B'
BARBARIAN_HEALTH_POINTS = 100
BARBARIAN_DAMAGE = 1
BARBARIAN_MOVEMENT_SPEED = 1
BARBARIAN_TILE = Fore.YELLOW + "B" + Style.RESET_ALL
CANNON_HEALTH_POINTS = 100
CANNON_DAMAGE = 20

# walls levels
WALL_LEVEL_1 = Back.YELLOW + Fore.BLACK + '*' + Style.RESET_ALL
WALL_LEVEL_2 = Back.MAGENTA + Fore.BLACK + '*' + Style.RESET_ALL
WALL_LEVEL_3 = Back.CYAN+Fore.BLACK + '*' + Style.RESET_ALL
# Health level
HWALL_LEVEL_1 = 10
HWALL_LEVEL_2 = 20
HWALL_LEVEL_3 = 30

# tile type
# empty tile
EMPTY = 0
# wall tile
TILE_WALL_LEVEL_1 = 1
TILE_WALL_LEVEL_2 = 2
TILE_WALL_LEVEL_3 = 3
TOWN_HALL = 4
HUT_TILE = 5
CANNON_TILE = 6
