# if __name__ == "__main__":
from player.py import Player
import random
file = open("record.txt")

#### Initialize Player ####
#load from file or initialize player
#if user chooses to load, open file. Or initialize player

#king gives you 100 gold.

#Initialize phase. Increment every time player win.
phase = 0

# #1 Adventure
##initialize enemy
##Fight, lvl up

if(win):
    phase+=1
    #update lvl, status
elif(lose):
    record = {phase: int, playername, status:{"hp":int, "mp":int, "str": int, "vit":int}, item:{str}, money:int}
    file.write(record)

##### ENTER LOOP ####
#choices: adventure, shop, lake 
while(True):
    #Shop appears with 1/4 chance
    shop = True if 1 == random.randint(4) else False
    #Lake appears with 1/5 chance
    lake = True if 1 == random.randint(5) else False
    if(shop):
        pass
    elif(lake):
        pass
    #Adventure
    else:
        pass

close(file)