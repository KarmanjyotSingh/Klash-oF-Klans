from src.village import Village
from src.globals import *

import time
f = open('src/numreplay.txt', 'r')
num = int(f.read())
if num == 0:
    print("No replays !!!")
    exit()
# print(num)
# sys.path.insert(0, './src')

timeout = 0.9
for replay in range(1, num+1):
    print("Replaying " + str(replay))
    village = Village()
    village.render()
    file_name = "replay/" + str(replay) + ".txt"
    file = open(file_name, 'r')
    data = file.readlines()
    for input in data:
        if input == "None":
            time.sleep(timeout)
        else:
            ret = input[0]
            if ret == 'q':
                break
            village.king.moveKing(ret, village)
            village.render()
            village.moveBarbs()
            village.shootCannon()
            r = village.isActive()
            if r == False:
                break
            time.sleep(timeout)
    time.sleep(timeout+1)
