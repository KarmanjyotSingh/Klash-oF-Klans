from village import Village
from input import *
village = Village()
village.render()
while(True):
    ch = input_to(Get().__call__)
    village.king.moveKing(ch, village)
    if ch == 'q':
        break
    else:
        village.render()
        village.moveBarbs()
