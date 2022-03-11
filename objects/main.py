import globals as macros
from village import Village
from input import *
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
        file_name = "../replay/" + str(n+1)+".txt"
        file = open(file_name, 'w')
        for i in inputArr:
            print(i)
            file.write(str(i)+'\n')
        file.close()
        f = open('numreplay.txt', 'w')
        f.write(str(n+1))
        f.close()
        break
    else:
        village.render()
        village.moveBarbs()
        village.shootCannon()
        ret = village.isActive()
        if ret == False:
            file_name = "../replay" + str(n+1)+".txt"
            file = open(file_name, 'w')
            for i in inputArr:
                file.write(str(i))
            file.close()
            break
