from models.py import *
import random


class Main():
    def __init__(self):
        # Open file if exsisted, otherwise make a file
        self.file = open("record.txt, w")
        # Load other necessary files e.g. sound, image

        self.init_game()

    def init_game(self):
        # show title
        self.game_state = TITLE
        #Initialize phase. Increment every time player win.
        self.phase = 0

        #### Initialize Player ####
        #load from file or initialize player
        #if user chooses to load, open file. Or initialize player
        i = input("Type player number to load, or type 0 to initialize.")
        if(i == 0):
            self.player = Player()
        else:
            # check if the player exists in record, then initialize player with the value
            self.player = Player(file[i].status))
        
        #### King gives you 100 gold ####

        self.game_state = ADVENTURE

        #### Initialize enemy, Battle
        enemy = Enemy()
        b = Battle(player, enemy)
        b.fight()
        if(result == WIN):
            b.win()
        elif(result == LOSE):
            b.lose()
            

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
            #Battle
            else:
                b = Battle(player, enemy)


        close(file)

class Battle():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    def fight(self):
        result = None
        if(self.player.status.hp > self.enemy.status.hp):
            result = WIN
        else:
            result = LOST
        return result

    def win(self):
        player.lvlup()
        phase +=1

    def lose(self):
        record = {
            phase: self.phase, playername: player.name, 
            status:{"hp":player.status.hp, "mp":player.status.mp, "str": player.status.str, "vit":player.status.vit}, 
            item:{player.items}, money:player.money
            }
        file.write(record)
        
    

if __name__ == "__main__":
    Main()