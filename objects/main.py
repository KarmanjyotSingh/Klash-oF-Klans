from objects.village import Village
from objects.input import *


def Run():
    village = Village()
    village.render()
    inputArr = []
    f = open('numreplay.txt', 'r+')
    data = f.readlines()
    n = int(data[0])
    f.close()
    while(True):

        ch = input_to(Get().__call__)
        inputArr.append(ch)
        ret = village.king.moveKing(ch, village)
        if ch == 'q':
            f = open('numreplay.txt', 'w')
            f.write(str(n+1))
            f.close()
            file_name = "replay/" + str(n+1)+".txt"
            file = open(file_name, 'w')
            for i in inputArr:
                file.write(str(i)+'\n')
            file.close()
            
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
                f = open('numreplay.txt', 'w')
                f.write(str(n+1))
                f.close()
                break
