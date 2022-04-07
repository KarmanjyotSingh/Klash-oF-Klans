from src.village import Village
from src.input import *
import src.globals as macros
import src.levels as levels


def Run(choice):
    # choice refers to king or queen chosen by the player
    # choice = 1 for king
    # choice = 2 for queen
    village = Village(1, choice)
    village.render()
    inputArr = []
    f = open('src/numreplay.txt', 'r+')
    data = f.readlines()
    n = int(data[0])
    f.close()
    while(True):

        ch = input_to(Get().__call__)
        inputArr.append(ch)
        if choice == 1:
            village.king.moveKing(ch, village)

        else:
            village.queen.moveQueen(ch, village)
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
            village.shootWizard()
            ret = village.isActive()
            if ret == False:
                if village.level == 1:
                    village = Village(2, choice)
                elif village.level == 2:
                    village = Village(3, choice)
                else:
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
                    # set the new variables ig
                # village.campsize = 20
            else:
                # game lost
                flag = False

                for barbs in village.barbarians:
                    flag = barbs.alive
                troopFlag = False
                if choice == 1 : 
                    troopFlag = village.king.alive
                else:
                    troopFlag = village.queen.alive
                if flag == False and village.campsize == 20 and troopFlag == False:
                    village.gameLost()
                    break
