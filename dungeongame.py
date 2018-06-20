import random


class Monster():
    
    number = 0
    zoo = {}
    
    
    def __init__(self, x, y, z, hp=100):
        self.number = Monster.number
        Monster.number += 1
        Monster.zoo[self.number] = self
        self.x = x
        self.y = y
        self.z = z
        self.hp = hp
        self.init2()
        
    def init2(self):
        pass
    
       
        
        
class Guardian(Monster):
    
    def init2(self):
        self.hp = 25
        self.char = "W"
        self.attack = 5
        self.defense = 3
        
class Boss(Monster):
    
    def init2(self):
        self.hp = 35
        self.char = "B"
        self.attack = 7
        self.defense = 5
        
class Player(Monster):
    
    def init2(self):
        self.hp = 100
        self.char = "@"
        self.attack = 13
        self.defense = 5
        
        
class Kobolt(Monster):
    
    def init2(self):
        self.hp = 10
        self.char = "K" 
        self.attack = 3
        self.defense = 3 

class Hunter(Monster):
    
    def init2(self):
        self.hp = 20
        self.char = "H"
        self.attack = 6
        self.defense = 3              
        
def fight(attacker, defender):
    print("----- fight starts ------")
    action(attacker, defender)
    # wenn defender noch lebt
    if defender.hp > 0:
        print("----counterstrike ----")
        action(defender, attacker)
    print("----- fight ends ------")
    
def action(attacker, defender):
    print("{} attacks {}".format(attacker.char, defender.char))
    wa = random.randint(1,6)
    wd = random.randint(1,6)
    print("luck: (attacker, defender):", wa, wd)
    print("values: (attacker attack, vert. def):", attacker.attack, defender.defense)
    print("{} HP: {} {} HP: {}".format(attacker.char,attacker.hp, defender.char, defender.hp))
    if wa + attacker.attack > wd + defender.defense:
        print("attack was sucesfull")
        schaden = random.randint(1,6)
        print("damage:", schaden)
        defender.hp -= schaden
        if defender.hp <= 0:
            print("Kill!!!")
    else:
        print("attack was defended")
    print("attack is over!")    
    print("{} HP: {} {} HP: {}".format(attacker.char,attacker.hp, defender.char, defender.hp))
        

def randomTeleport(radius = 4):
    while True:
        dx = random.randint(-radius,radius)
        dy = random.randint(-radius, radius)
        if dungeon[hy+dy][hx+dx] == ".":
            return hx+dx,hy+dy
          

helptext = """
legend:
@ .... this is you, the player
# .... this is a dungeon wall
. .... this is an empty space in the dungeon
W .... this is a guardian
B .... this is an boss enemy
H .... this is an hunter enemy
K .... this is an cobolt enemy
T .... is a trap
> .... this is a ladder to go down
< .... this is a ladder to go up
b .... this is a burger
p .... this is a pizza
d .... this is a door
k .... this is a key
$ .... this is gold
X and Y .... are teleporters
V and v .... are random teleporters

commands:
w, a, s, d .............move
down, > .......... climb down
up, < .............. climb up
help, ? ... display this text
quit, exit .... exit the game 
pause ... stop the game
            
"""

pausetext = """
...................................
...................................
...................................
..............PAUSE................
...................................
...................................
...................................
"""





level0 = """
############################################
#.>@.b....$....p....A.....#..........W.....#
#......b.......b.............p.............#
####.....T....W..................b..####...#
#$$#...b..T....................b....d.$#...#
#TT###..$......b...........$........####...#
#W.X.#......p..................T...........#
#WWT##p..K.............V...........b..######
#.WT...#####....H...............K.....T.$..#
#...b.B...$.##....#......$.........T..######
#.....#######...W....#.T...b$#...b.......B.#
#........p....b.....v..T######...###########
####...#bb#.....b...#####.......p#bb$bb$$.Y#
#.$..b..##.......$..#...b...W....###########
############################################
"""

level1 = """
################################
#<..>..#..WTB.#...b..$....W....#
#......#...#bb#...b.....b..p...#
#d######...####....p..$.$......#  
#....$....b.....T..K..W.....#### 
#####..b..b...b.....$..#d##B$bb#
#.$p#....HT..######....#$$######
#.$.TT.......B....#..A.#bk#....#
################################
"""

level2 = """
################
#<...K..p.kp...#
#############TT#
#>bbbkk$d$.b.WW#
################
################


"""

level3 = """
########################################
#..<#..B.....T....b.........#.T........#
#..>#........###.......$....#......#####
#.###b...W...b...v..K.....k....b...Tb$$#
#B......#......#......#B#...T...A..#####
#...$...#.W....#...$..#B#.......p.$TTB.#
#.............$.####..#k#....B.....#.k.#
########################################
"""

level4 = """
#################################
#...<.#............A.T..p.......#
#.....#..bbbbbb.................#
#WWWWW#....$.$$..$$$.$$.$.$...K.#
#....TB.....W........W..........#
#################################
"""

levels = [level0, level1, level2, level3, level4]
dungeon = []
for z, rawstring in enumerate(levels):
    d = []
    for y, line in enumerate(rawstring.splitlines()):
        l = []
        for x, char in enumerate(line):
            if char == "@":
                l.append(".")
                Player(x,y,z)
            elif char =="W":
                l.append(".")
                Guardian(x,y,z)
            elif char == "B":
                l.append(".")
                Boss(x,y,z)
            elif char == "K":
                l.append(".")
                Kobolt(x,y,z)
            elif char == "H":
                l.append(".")
                Hunter(x,y,z)    
            else:
                l.append(char)
            
        d.append(l)
    dungeon.append(d)
hx = Monster.zoo[0].x
hy = Monster.zoo[0].y
hz = Monster.zoo[0].z
gold = 0
hunger = 50
hp = 100
keys = 0
randomX = random.randint(2,30)
randomY = random.randint(2,10)
randomZ = random.randint(0,1)
while Monster.zoo[0].hp > 0:
    z = Monster.zoo[0].z
    for y, line in enumerate(dungeon[z]):
        for x, char in enumerate(line):
            sign = char
            #clear zoo from dead monsters
            zoo2 = {}
            for mo in Monster.zoo:
                if Monster.zoo[mo].hp > 0:
                    zoo2[mo] = Monster.zoo[mo] 
            Monster.zoo = zoo2
            for mo in Monster.zoo:
                if Monster.zoo[mo].z == z and Monster.zoo[mo].y == y and Monster.zoo[mo].x == x and Monster.zoo[mo].hp > 0:
                    sign = Monster.zoo[mo].char
            
            print(sign, end="")
        print()
    hx = Monster.zoo[0].x
    hy = Monster.zoo[0].y
    hz = Monster.zoo[0].z
    command = input("x: {} y:{} z:{} help or ? to get help  \ngold: {} hunger: {} health: {} keys: {} \n  What do you want to do?>>>".format(hx, hy, hz, gold, hunger, Monster.zoo[0].hp, keys))
    dx = 0
    dy = 0
    if command == "a":
        dx =-1
    if command == "d":
        dx = 1
    if command == "w":
        dy = -1
    if command == "s":
        dy = 1
    if command == "help" or command == "?":
        print(helptext)
        input("press enter to continue....")
    if command == "quit" or command == "exit":
        break 
    if command == "pause":
        print(pausetext)
        input("press enter to continue...")          
        
         
    # ---- illegal move -----
    target_location = dungeon[hz][hy+dy][hx + dx]
    # -------- up / down ----------
    if command == "down" or command == ">":
        if target_location == ">":
            print("You go deeper in the dungeon")
            hz += 1
            Monster.zoo[0].z += 1
        else:
            print("you have to find a ladder (>)")
    if command == "up" or command == "<":
        if target_location == "<": 
            print("You go up in the dungeon")
            hz -= 1
            Monster.zoo[0].z -= 1
        else:
            print("You have to find a ladder (<)")    
        
    
    if target_location == "#":
        print("you can’t walk there because of the wall")
        dx = 0
        dy = 0
    if target_location == "d":
        if keys < 1:
            print("Before you can open the door you must find a key")
            dx = 0
            dy = 0
        else:
            print("You open the door with the key")
            keys -= 1
            dungeon[hz][hy + dy][hx + dx] = "."
                                             
    # ----- kampf ? --------------
    # alle monster durchiterieren (stück für stück abarbeiten)
    # und schauen ob spieler in ein anderes monster reinläuft
    
    for mo in Monster.zoo:
        if mo == 0:
            continue # das ist der Spieler , nächstes Monster bitte
        if Monster.zoo[mo].z != hz:
            continue # monster im falschen level, nächstes monster bitte
        if Monster.zoo[mo].x != hx + dx or Monster.zoo[mo].y != hy + dy:
            continue # monster ist nicht dort wo spieler hinläuft, nächstes Monster bitte
        # --- Kampf ----
        fight(Monster.zoo[0], Monster.zoo[mo])
        dx = 0
        dy = 0
        
            
            
        
        # lebt spieler noch?
    if Monster.zoo[0].hp <= 0:
            break
            
            
            
    # -----move------
    hx+=dx
    hy+=dy
    Monster.zoo[0].x = hx
    Monster.zoo[0].y = hy
    # -----foodclock----
    hunger+=1
    if hunger > 100 and random.random() < 0.2:
        print("You get damage because of hunger")
        hp -= 1
        #------health+---
    if hunger < 10 and hp < 100 and random.random() > 0.1:
        print("you heal one HP")
        hp += 1
    # --- pick up tile ----
    if dungeon[hz][hy][hx]=="$":  # == --> Vergleich
        print("You have find gold")
        gold += random.randint(1,6)
        dungeon[hz][hy][hx]="."   # =  --> Zuweisung 
    if dungeon[hz][hy][hx]=="b":
        print("You eat a burger")
        hunger -= random.randint(1,20) 
        dungeon[hz][hy][hx]="."
    if dungeon[hz][hy][hx]=="p":
        print("You eat a pizza")
        hunger -= random.randint(1, 13)
        dungeon[hz][hy][hx]="."
    if dungeon[hz][hy][hx]=="T":
        print("You walked into a trap")
        Monster.zoo[0].hp -= random.randint(1,50)
        dungeon[hz][hy][hx]="." 
    if dungeon[hz][hy][hx]=="k":
       print("You have found a key")
       keys += 1
       dungeon[hz][hy][hx]="."
    if dungeon[hz][hy][hx] == "X":
        print("You walked into a teleporter")
        hx = 41
        hy = 13
    if dungeon[hz][hy][hx] == "Y": 
        print("You walked into a teleporter")
        hx = 2
        hy = 7 
    if dungeon[hz][hy][hx] == "V":
        print("You walked into a random teleporter")  
        
        hx,hy = randomTeleport(7)
        
    if dungeon[hz][hy][hx] == "v":
        print("You walked into a mini-random teleporter")
        hx,hy = randomTeleport()  
    if dungeon[hz][hy][hx] == "A" and hx != "#" and hy != "#":
		
	    print("You have a new quest! Go to x: {} y: {} und z: {}".format(randomX, randomY, randomZ))
    if hx == randomX and hy == randomY and hz == randomZ:
            print("You finished the quest! You get gold food and health")
            gold += 10
            hp += 30
            hunger -= 50
            randomX = random.randint(2,30)
            randomY = random.randint(2,8)
            randomZ = random.randint(0,1)    
             
 
        
           
            
            
            
    
             
    
            
        

