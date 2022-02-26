from colorama import Fore, Style, Back
# village macros
VILLAGE_WIDTH = 210
VILLAGE_HEIGHT = 50
BORDER_PIXEL = Back.WHITE + ' ' + Style.RESET_ALL
BACKGROUND_PIXEL = Back.BLACK + ' ' + Style.RESET_ALL
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
