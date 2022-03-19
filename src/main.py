from src.village import Village
from src.input import *
import src.globals as macros


def Run():
    village = Village()
    village.render()
    inputArr = []
    f = open('src/numreplay.txt', 'r+')
    data = f.readlines()
    n = int(data[0])
    f.close()
    while(True):

        ch = input_to(Get().__call__)
        inputArr.append(ch)
        ret = village.king.moveKing(ch, village)
        if ch == 'q':
            f = open('src/numreplay.txt', 'w')
            f.write(str(n+1))
            f.close()
            file_name = "replay/" + str(n+1)+".txt"
            file = open(file_name, 'w')
            for i in inputArr:
                file.write(str(i)+'\n')
            file.close()
            village.gameLost()
            break
        else:
            village.render()
            village.moveBarbs()
            village.shootCannon()
            ret = village.isActive()
            if ret == False:
                file_name = "replay/" + str(n+1)+".txt"
                file = open(file_name, 'w')
                for i in inputArr:
                    file.write(str(i)+'\n')
                file.close()
                f = open('src/numreplay.txt', 'w')
                f.write(str(n+1))
                f.close()
                village.gameWon()
                break
            else:
                # game lost 
                if village.campsize == macros.CAMP_SIZE:
                    flag = False
                    for barbs in village.barbarians:
                        flag = barbs.alive
                    if flag == False and village.king.alive == False:
                        village.gameLost()
                        break

                