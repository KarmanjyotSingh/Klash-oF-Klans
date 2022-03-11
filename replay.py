from objects.village import Village
from objects.globals import * 

import time
f = open('numreplay.txt', 'r')
num = int(f.read())
print(num)
# sys.path.insert(0, './objects')

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
