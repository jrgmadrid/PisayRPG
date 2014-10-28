import random
import time

class Node():
    def __init__(self, name, desc, stpos):
        self.Name = name
        self.Desc = desc
        self.N = []
        self.start = stpos
        self.wt = None
    def addN(self,n,wt):
        self.N.append([n,wt])
        self.wt = wt
    def addN2(self,n,wt):
        self.addN(n,wt)
        n.addN(self,wt)

flag = Node("Flagpole", "Where three flagpoles sit. The entrance to the Philippine Science High School Main Campus.", True)
fLob = Node("Front Lobby", "A popular hangout for students during lunch break. Crammers can typically be found here.", False)
SHB1F = Node("Science and Humanities Building (1F)", "The part of the main building devoted to science lessons.", False)
SHB2F = Node("Science and Humanities Building (2F)", "The part of the main building devoted to administrative offices and the like.", False)
SHB3F = Node("Science and Humanities Building (3F)", "The part of the main building filled with classrooms, mostly for the humanities subjects.", False)
SHB4F = Node("Science and Humanities Building (4F)", "The part of the main building devoted to the field of mathematics.", False)
ASTB1F = Node("Advanced Science and Technology Building (1F)", "The part of the annex building filled with computer laboratories and whatnot.", False)
ASTB2F = Node("Advanced Science and Technology Building (2F)", "The part of the annex building filled with biology and chemistry labs.", False)
ASTB3F = Node("Advanced Science and Technology Building (3F)", "The part of the annex building filled with physics labs.", False)
Roof = Node("Science and Humanities Building (Roof)", "The highest point of the school. You can observe everything from here.", False)
bLob = Node("Back Lobby", "A popular hangout for students during lunch break, in part due to its proximity to the cafeteria.", False)
Caf = Node("Cafeteria", "Where you get food.", False)
Gym = Node("Gym", "This unfinished building is where scholars train their bodies.", False)
Oval = Node("The Oval", "Essentially an elliptical track, running speed can be increased here.", False)
Lib = Node("Library", "This hall of learning enables you to train your mind.", False)

wmap = [flag,fLob,SHB1F,SHB2F,SHB3F,SHB4F,ASTB1F,ASTB2F,ASTB3F,Roof,bLob,Caf,Gym,Oval,Lib]

flag.addN2(fLob,10)
flag.addN2(bLob,50)
flag.addN2(Oval,15)
fLob.addN2(SHB1F,10)
fLob.addN2(ASTB1F,20)
fLob.addN2(bLob,30)
fLob.addN2(Oval,10)
SHB1F.addN2(SHB2F,15)
SHB1F.addN2(bLob,10)
SHB2F.addN2(Lib,5)
SHB2F.addN2(SHB3F,15)
SHB3F.addN2(SHB4F,15)
SHB4F.addN2(Roof,5)
ASTB1F.addN2(bLob,20)
ASTB1F.addN2(ASTB2F,15)
ASTB2F.addN2(ASTB3F,15)
bLob.addN2(Oval,10)
bLob.addN2(Caf,15)
Oval.addN2(Gym,30)


def RNG():
    x = random.randint(1,100)
    return x

def ID():
    x = RNG()
    if x <= 10:
        return "A"
    elif x <= 20:
        return "B"
    elif x <= 30:
        return "C"
    elif x <= 40:
        return "D"
    elif x <= 50:
        return "E"
    elif x <= 60:
        return "F"
    elif x <= 70:
        return "G"
    elif x <= 80:
        return "H"
    elif x <= 90:
        return "I"
    else:
        return "J"

class foe():
    def __init__(self,boss):
        if boss == "mook":
            x = ID()
            if x == "A":
                self.name = "The Grade-Conscious"
                self.desc = "Look at him, with his calculator in hand, always trying to figure out how much he needs to score to get that elusive uno."
                self.useMAG = None
                self.normATK = "The Grade-Conscious whips out his calculator and graphs the different ways he can kick your ass. Ouch."
                self.critATK = "The Grade-Conscious calculates your spin, charge and mass and synthesizes an anti-You particle! WHAM."
            elif x == "B":
                self.name = "The Popular"
                self.desc = "She's the girl surrounded by friends, the girl every guy wants. She smiled at you! Quick, look away! No! She spotted you!"
                self.useMAG = None
                self.normATK = "The Popular Girl smiles at you. Your chest begins to ache because she's out of your league, man."
                self.critATK = "The Popular Girl's boyfriend arrives! Heartbreak ensues!"
            elif x == "C":
                self.name = "The Activist"
                self.desc = "This guy's all up in the world's business, always with an opinion."
                self.useMAG = None
                self.normATK = "The Activist begins to advocate social change! You begin to feel the pain of all the oppressed people throughout history..."
                self.critATK = "The Activist begins to lament the horrors of the Holocaust! OH NOES!"
            elif x == "D":
                self.name = "The Artistic"
                self.desc = "This moody girl gives you a glance from behind her long hair and continues sketching."
                self.useMAG = None
                self.normATK = "The Artistic pulls out three fountain pens and throws 'em at you, kinda like throwing knives."
                self.critATK = "The Artistic does a quick portrait of you, and burns it, a la Dorian Grey. Okay, maybe not, but still."
            elif x == "E":
                self.name = "The STR Geek"
                self.desc = "They're always in foreign countries, talking about how plants can be applied instead of medicine."
                self.useMAG = None
                self.normATK = "The STR Geek waves his tarp, summoning a soxhlet extractor! You can feel all 21 grams of your soul being sucked away!"
                self.critATK = "The STR Geek waves his tarp, and proceeds to perform several Variance Analysis tests... ON YOUR FACE."
            elif x == "F":
                self.name = "The Mathemagician"
                self.desc = "This guy has a way with numbers, and that's putting it lightly."
                self.useMAG = None
                self.normATK = "The Mathemagician predicts your next position and trips you up."
                self.critATK = "The Mathemagician begins to push your body to its asymptotic limit with his fists!"
            elif x == "G":
                self.name = "Average Student"
                self.desc = "Your everyday scholar. Works hard, plays hard."
                self.useMAG = None
                self.normATK = "The Average Student begins to lament his low stipend."
                self.critATK = "The Average Student begins to cram pain into your solar plexus!"
            elif x == "H":
                self.name = "The Otaku"
                self.desc = "Kekekeke! She is so kawaii, desu ne~~~~ ^_^"
                self.useMAG = None
                self.normATK = "POCKY ATTA~KU!"
                self.critATK = "GANDAMMU BURASTAAAAAA~~"
            elif x == "I":
                self.name = "The Crammer"
                self.desc = "He just can't seem to catch a break! Don't you feel sorry for the guy?"
                self.useMAG = None
                self.normATK = "The Crammer realizes he has a Math test to take and tackles you in an effort to get to the classroom."
                self.critATK = "The Crammer whips out Serway and incessantly asks you Physics questions! THE HORROR!"
            elif x == "J":
                self.name = "The PDA Couple"
                self.desc = "GET A ROOM, YOU TWO."
                self.useMAG = None
                self.normATK = "They begin to make out. Poorly. It's disgusting."
                self.critATK = "They begin to make out, and you find yourself being drawn into the throes of lust..."
            self.HP = random.randint(1,60)
            self.MP = 0
            self.DMG = random.randint(1,30)
            self.CRIT = self.DMG*2
            self.AGI = random.randint(1,20)
            self.G = random.randint(1,5)
        else:
            x = ID()
            setOne = ["A","B","C","D","E"]
            setTwo = ["F","G","H","I","J"]
            for var in setOne:
                if x == var:
                    self.name = "The Freakin' Moon"
                    self.desc = "It's the MOON."
                    self.normATK = "It slowly but surely inches toward you."
                    self.critATK = "OH SNAP, THE MOON DROPPED ON ALL Y'ALL"
                    self.useMAG = None
                    self.HP = 500
                    self.MP = 0
                    self.DMG = 0
                    self.CRIT = 9001
                    self.AGI = -10
                    self.G = 10
            for var in setTwo:
                if x == var:
                    self.name = "DAGRON"
                    self.desc = "It's a poorly drawn (and misspelled) dragon. Go figure."
                    self.normATK = "The dagron unleashes its mighty braeth attack."
                    self.critATK = "The dagron unleashes an ifnreno of flaem!"
                    self.useMAG = None
                    self.HP = 50
                    self.MP = 0
                    self.DMG = 10
                    self.CRIT = 20
                    self.AGI = 5
                    self.G = 10
        self.HP_MAX = self.HP
        self.MP_MAX = self.MP
        self.stats = ["HP: "+str(self.HP)+"/"+str(self.HP_MAX), "MP: "+str(self.MP)+"/"+str(self.MP_MAX), "DMG: "+str(self.DMG), "AGI: "+str(self.AGI)]

def statAlloc(stat, pts):
    print "How many points do you wish to allocate?"
    print "Current value: "+str(stat)
    points = raw_input()
    fPoints = pts - int(points)
    if fPoints < 0:
        print "Too many points."
    else:
        x = stat + int(points)
        return [x, fPoints]

def hpADD(x,increase):
    x.HP_MAX += increase
    x.HP = x.HP_MAX

def mpADD(x,increase):
    x.MP_MAX += increase
    x.MP = x.MP_MAX

def dmgADD(x,increase):
    x.DMG += increase
    x.CRIT = x.DMG*2

def agiADD(x,increase):
    x.AGI += increase

class Hero():
    def __init__(self):
        print "Name?"
        self.name = raw_input()
        print "Job Class?"
        self.job = raw_input()
        print "What weapon do you wish to use?"
        self.weapon = raw_input()
        print "What element of magic do you wish to use?"
        self.magic = raw_input()
        self.HP_MAX = 10
        self.MP_MAX = 5
        self.DMG = 5
        self.AGI = 5
        self.DEF = 1
        self.G = 10
        self.currentPos = flag
        x = 110
        while x > 0:
            print "Divide "+str(x)+" among your parameters."
            print "Which parameter would you like to increase?"
            print "Valid commands: HP, MP, DMG, AGI"
            param = raw_input()
            param = param.lower()
            if param == "hp":
                results = statAlloc(self.HP_MAX, x)
                self.HP_MAX = results[0]
                x = results[1]
            elif param == "mp":
                results = statAlloc(self.MP_MAX, x)
                self.MP_MAX = results[0]
                x = results[1]
            elif param == "dmg":
                results = statAlloc(self.DMG, x)
                self.DMG = results[0]
                x = results[1]
            elif param == "agi":
                results = statAlloc(self.AGI, x)
                self.AGI = results[0]
                x = results[1]
            else:
                "Sorry, invalid."
        self.CRIT = self.DMG*2
        self.HP = self.HP_MAX
        self.MP = self.MP_MAX
        self.stats = ["HP: "+str(self.HP)+"/"+str(self.HP_MAX), "MP: "+str(self.MP)+"/"+str(self.MP_MAX), "DMG: "+str(self.DMG), "AGI: "+str(self.AGI)]
        lol = str(self.DMG)
        self.normATK = self.name+" hits the enemy with the "+self.weapon+"."
        self.critATK = "BOOM! "+self.name+" hit the enemy on the head with your " +self.weapon+ "."
        self.useMAG = "Crack-thoom! "+self.name+" threw a ball of "+self.magic+" at the enemy!"
    def Heal(self):
        print self.name+" prays!"
        if self.MP == 0:
            print "The prayer failed!"
        else:
            if self.HP == self.HP_MAX:
                print "But it turned out to be useless!"
                self.MP-=1
            else:
                if self.HP_MAX <= (self.HP + self.DMG):
                    print self.name+"'s wounds were fully healed!"
                    self.HP = self.HP_MAX
                else:
                    self.HP+=self.DMG
                    print self.name+" feels better! Sort of."
                self.MP-=1
        update(self)

def attack(user,target):
    accuracy = random.randint(1,20)
    if accuracy == 1:
        print "EPIC FAIL ENSUED!"
        accu2 = random.randint(1,20)
        if accu2 == 20:
            user.HP -= user.CRIT
            print user.name+" took "+str(user.CRIT)+" damage."
        else:
            user.HP -= user.DMG
            print user.name+" took "+str(user.DMG)+" damage."
    elif accuracy < target.AGI:
        print target.name+" dodged the attack!"
    elif accuracy == 20:
        print user.critATK
        target.HP -= user.CRIT
        print target.name+" took "+str(user.CRIT)+" damage."
    else:
        print user.normATK
        target.HP -= user.DMG
        print target.name+" took "+str(user.DMG)+" damage."
    update(user)
    update(target)

def useMagic(user,target):
    print user.name+" tried to cast a spell!"
    if user.useMAG != None and user.MP > 0:
        print user.useMAG
        print target.name+" took "+str(user.DMG)+" damage."
        user.MP-=1
        target.HP-=user.DMG
    else:
        print "The spell fizzled!"

def judge(a,b):
    if a.HP > 0 and b.HP > 0:
        print "The turn ends."
        return 0
    elif b.HP <= 0:
        print "You win!"
        a.G += b.G
        print "Gained "+str(b.G)+" Stipend Points!"
        return 1
    elif a.HP >= 0:
        print "You lose..."
        return 2
    else:
        print "The battle ended in a tie."
        return 3

def action(user,target,action):
    if action == "attack" or action == "a":
        attack(user,target)
        return "turn end"
    elif action == "magic" or action == "m":
        useMagic(user,target)
        return "turn end"
    elif action == "heal" or action == "h":
        user.Heal()
    elif action == "hanky-panky":
        user.HP = user.HP_MAX
        user.MP = user.MP_MAX
        user.DMG = user.CRIT
        user.AGI = 0
        print "...uh-huh."
        return "turn end"
    elif action == "scan" or action == "s":
        print "Using ANOVA, you statistically analyze the "+target.name+"'s stats."
        print target.stats
    elif action == "do nothing":
        print "If you say so."
        return "turn end"
    else:
        print "Oh, come on."

def battle(a,b):
    print " "
    print " "
    print "You encountered "+b.name
    print b.desc
    a_INIT = a.AGI + RNG()
    b_INIT = b.AGI + RNG()
    while a_INIT == b_INIT:
        a_INIT = a.AGI + RNG()
        b_INIT = b.AGI + RNG()
    while a.HP > 0 and b.HP > 0:
        if a_INIT > b_INIT:
            print "Your turn!"
            print "Commands: attack, magic, scan, heal"
            print a.stats
            command = raw_input()
            while action(a,b,command) != "turn end":
                print "Commands: attack, magic, scan, heal"
                print a.stats
                command = raw_input()
            update(a)
            update(b)
            if judge(a,b) != 0:
                return judge(a,b)
            print "Your opponent's turn!"
            action(b,a,"a")
            if judge(a,b) != 0:
                return judge(a,b)
            update(a)
            update(b)
        else:
            print "Your opponent's turn!"
            action(b,a,"a")
            update(a)
            update(b)
            if judge(a,b) != 0:
                return judge(a,b)
            print "Your turn!"
            print "Commands: attack, magic, scan, heal"
            print a.stats
            command = raw_input()
            while action(a,b,command) != "turn end":
                print "Commands: attack, magic, scan, heal"
                print a.stats
                command = raw_input()
            update(a)
            update(b)
            if judge(a,b) != 0:
                return judge(a,b)
    

def statBuy(x,statName,stat,xchange, adj):
    print "You can increase your "+statName+" here."
    print "Price: "+str(xchange)+" Stipend Points per "+statName+" increase."
    print "Will you? (y/n)"
    dec = raw_input()
    if dec == "y" or dec == "Y":
        print "How much?"
        print "You currently have "+str(x.G)+" Stipend Points..."
        print "Please be advised that you can't have a fraction of a skill point."
        pay = raw_input()
        if int(pay) == 0:
            print "You leave without spending anything."
        elif int(pay) > x.G:
            print "Not enough."
        else:
            x.G -= int(pay)
            inc = int(pay)/xchange
            if statName == "Maximum HP":
                hpADD(x,inc)
            elif statName == "Maximum MP":
                mpADD(x,inc)
            elif statName == "Damage":
                dmgADD(x,inc)
            else:
                agiADD(x,inc)
            update(x)
            print "You feel "+adj+"..."
            update(x)
            print x.stats
    else:
        print "You leave."

def move(x, destination):
    y = 0
    battled = False
    while y < destination.wt and battled == False:
        rand = RNG()
        if rand > destination.wt:
            ene = foe("mook")
            battled = True
            result = battle(x,ene)
            if result == 2 or result == 3:
                return False
        else:
            y+=1
    x.currentPos = destination

def checkLoc(x):
    print " "
    print " "
    print x.currentPos.Name
    print x.currentPos.Desc
    name = x.currentPos.Name
    if name == "Library":
        statBuy(x,"Maximum MP",x.MP_MAX,2,"smarter")
    elif name == "Cafeteria":
        statBuy(x,"Maximum HP",x.HP_MAX,3,"tougher")
    elif name == "Gym":
        statBuy(x,"Damage",x.DMG,5,"stronger")
    elif name == "The Oval":
        statBuy(x,"Agility",x.AGI,1,"more agile")
                

def update(a):
    a.stats = ["HP: "+str(a.HP)+"/"+str(a.HP_MAX), "MP: "+str(a.MP)+"/"+str(a.MP_MAX), "DMG: "+str(a.DMG), "AGI: "+str(a.AGI)]

def startGame():
    turns = 0
    bossWins = 0
    print "WELCOME TO PISAY: THE RPG"
    print "AN OVERUSED PROJECT IDEA GIVEN NEW LIFE. OR NOT."
    x = Hero()
    state = True
    while state == True:
        checkLoc(x)
        print "Where will you go?"
        turnsLeft = 5 - turns
        print "You have "+str(turnsLeft)+" turns until a Long Test."
        locales = []
        for place in x.currentPos.N:
            locales.append(place[0].Name)
        print locales
        y = raw_input()
        for item in x.currentPos.N:
            if y.lower() == item[0].Name.lower():
                if move(x,item[0]) == False:
                    state = False
            elif y.lower() == "wait":
                print "You do nothing."
        turns+=1
        if turns == 0:
            boss = foe("boss")
            if battle(x,boss) == False:
                state = False
            else:
                bossWins += 1
                turns = 0
        if bossWins == 5:
            print "You win!"
            state = False
            startGame()

                    

startGame()
