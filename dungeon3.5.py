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
    
    #def kill(self):
     #   del Monster.zoo[self.number]    
        
        
class Waechter(Monster):
    
    def init2(self):
        self.hp = 30
        self.char = "W"
        self.attack = 5
        self.defense = 3
        
class Boss(Monster):
    
    def init2(self):
        self.hp = 90
        self.char = "B"
        self.attack = 7
        self.defense = 5
        
class Player(Monster):
    
    def init2(self):
        self.hp = 100
        self.char = "@"
        self.attack = 8
        self.defense = 5
        
        
class Kobolt(Monster):
    
    def init2(self):
        self.hp = 30
        self.char = "K" 
        self.attack = 3
        self.defense = 3 

class Hunter(Monster):
    
    def init2(self):
        self.hp = 40
        self.char = "H"
        self.attack = 6
        self.defense = 3              
        
def fight(attacker, defender):
    print("----- kampfrunde beginnt ------")
    action(attacker, defender)
    # wenn defender noch lebt
    if defender.hp > 0:
        print("---- Gegenschlag----")
        action(defender, attacker)
    print("----- kampfrunde endet ------")
    
def action(attacker, defender):
    print("{} attackiert {}".format(attacker.char, defender.char))
    wa = random.randint(1,6)
    wd = random.randint(1,6)
    print("würfelglück: (angreifer, verteidiger):", wa, wd)
    print("werte: (angreifer attack, vert. def):", attacker.attack, defender.defense)
    print("{} HP: {} {} HP: {}".format(attacker.char,attacker.hp, defender.char, defender.hp))
    if wa + attacker.attack > wd + defender.defense:
        print("attacke war erfolgreich")
        schaden = random.randint(1,6)
        print("schaden:", schaden)
        defender.hp -= schaden
        if defender.hp <= 0:
            print("Kill!!!")
    else:
        print("attacke wurde abgewehrt")
    print("angriff vorbei!")    
    print("{} HP: {} {} HP: {}".format(attacker.char,attacker.hp, defender.char, defender.hp))
        

def randomTeleport(radius = 4):
    while True:
        dx = random.randint(-radius,radius)
        dy = random.randint(-radius, radius)
        if dungeon[hy+dy][hx+dx] == ".":
            return hx+dx,hy+dy
          

            

# hx += random.randint(-5,5)


level0 = """
############################################
#.>@.b....$....p....A.....#..........W.....#
#......b.......b.............p.............#
####.....T....W..................b..####...#
#$$#...b..T....................b....d.$#...#
#TT###..$......b....................####...#
#W.X.#......p..................T...........#
#WWT##p..K.............V...........b..######
#.WT...#####....H...............K.....T.$..#
#...b.B...$.##....#................T..######
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
                Waechter(x,y,z)
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
schluessel = 0
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
            #if y == hy and x == hx:
            #    print(hero, end="")
            #else:
            print(sign, end="")
        print()
    hx = Monster.zoo[0].x
    hy = Monster.zoo[0].y
    hz = Monster.zoo[0].z
    command = input("x: {} y:{} z:{}  Treppe runter = down/> Treppe hoch = up/< \ngold: {} hunger: {} leben: {} schlüssel: {} \n  Was nun?>>>".format(hx, hy, hz, gold, hunger, Monster.zoo[0].hp, schluessel))
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
        
         
    # ---- illegal move -----
    target_location = dungeon[hz][hy+dy][hx + dx]
    # -------- up / down ----------
    if command == "down" or command == ">":
        if target_location == ">":
            print("du steigst tiefer in den dungeon hinab")
            hz += 1
            Monster.zoo[0].z += 1
        else:
            print("du musst erst eine Leiter finden (>)")
    if command == "up" or command == "<":
        if target_location == "<": 
            print("du steigst höher in den dungeon hinauf")
            hz -= 1
            Monster.zoo[0].z -= 1
        else:
            print("du musst erst eine Leiter finden (<)")    
        
    
    if target_location == "#":
        print("Du kannst nicht weiter gehen wegen einer Wand!")
        dx = 0
        dy = 0
    if target_location == "d":
        if schluessel < 1:
            print("Du kommst nicht durch die Tür du musst den Schlüssel finden!")
            dx = 0
            dy = 0
        else:
            print("Du öffnest die Tür mit deinem Schlüssel")
            schluessel -= 1
            dungeon[hz][hy + dy][hx + dx] = "."
    #if target_location == "W":
    #    print("Du kämpfst gegen einen Wächter!") 
    #    hp -= 10
    #    # loss/ win?
    #    if random.random() < 0.5:
    #        print("Du hast den Kampf gewonnen")
    #        dungeon[hz][hy+dy][hx+dx] = "."
    #    else:
    #        print("Du hast den Kampf verloren")  
    #    dx = 0
    #    dy = 0
        
    #if target_location == "B":
    #    print("Du kämpst gegen einen Boss-Wächter!")   
    #    hp -= 20
    #    # loss/ win?
    #    if random.random() < 0.4:
    #        print("Du hast den Kampf gewonnen")
    #        dungeon[hz][hy+dy][hx+dx] = "."
    #    else:
    #        print("Du hast den Kampf verloren")  
    #    dx = 0
    #    dy = 0
                                                    
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
        print("Hunger schwächt dich")
        hp -= 1
        #------health+---
    if hunger < 10 and hp < 100 and random.random() > 0.1:
        print("Du heilst ein HP")
        hp += 1
    # --- pick up tile ----
    if dungeon[hz][hy][hx]=="$":  # == --> Vergleich
        print("Du hast Gold gefunden")
        gold += random.randint(1,6)
        dungeon[hz][hy][hx]="."   # =  --> Zuweisung 
    if dungeon[hz][hy][hx]=="b":
        print("Du hast einen Burger gegessen!")
        hunger -= random.randint(1,20) 
        dungeon[hz][hy][hx]="."
    if dungeon[hz][hy][hx]=="p":
        print("Du hast eine Pizza gegessen!")
        hunger -= random.randint(1, 13)
        dungeon[hz][hy][hx]="."
    if dungeon[hz][hy][hx]=="T":
        print("Du bist in eine Falle gelaufen!")
        Monster.zoo[0].hp -= random.randint(1,50)
        dungeon[hz][hy][hx]="." 
    if dungeon[hz][hy][hx]=="k":
       print("Du hast einen Schlüssel gefunden")
       schluessel += 1
       dungeon[hz][hy][hx]="."
    if dungeon[hz][hy][hx] == "X":
        print("Du bist auf einen Teleporter gelaufen!")
        hx = 41
        hy = 13
    if dungeon[hz][hy][hx] == "Y": 
        print("Du bist auf einen Teleporter gelaufen!")
        hx = 2
        hy = 7 
    if dungeon[hz][hy][hx] == "V":
        print("Du bist auf einen Zufalls-Teleporter gelaufen")  
        #hx += random.randint(-5,5) 
        #hy += random.randint(-4,4)  
        hx,hy = randomTeleport(7)
        
    if dungeon[hz][hy][hx] == "v":
        print("Du bist auf einen Mini-Zufalls-Teleporter gelaufen")
        hx,hy = randomTeleport()  
    if dungeon[hz][hy][hx] == "A" and hx != "#" and hy != "#":
		
	    print("Du hast eine Aufgabe gefunden! Gehe zu x: {} y: {} und z: {}".format(randomX, randomY, randomZ))
    if hx == randomX and hy == randomY and hz == randomZ:
            print("Du hast die Aufgabe geschafft! Du bekommst eine Belohnung!")
            gold += 10
            hp += 30
            hunger -= 50
            randomX = random.randint(2,30)
            randomY = random.randint(2,8)
            randomZ = random.randint(0,1)    
             
 
        
    #if dungeon[hy][hx] == "W" and random.random() < 0.4:
    #    print("Du hast den Kampf gewonnen!") 
    #    dungeon[hy][hx] = "."
    #elif dungeon[hy][hx] == "W"and random.random() > 0.4:
    #    print("Du hast den Kampf verloren!")         
            
            
            
    
             
    
            
        

