from village import Village
from input import *
village = Village()
village.render()
while(True):
    ch = village.king.moveKing(village)
    if ch == 'q':
        break
    elif ch == None:
        continue
    village.render()
