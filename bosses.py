import os
import sys
import math
#from main import selDiff, selGM

selGM = "IvN"

if selGM == "IvN":
    bossOne = "Darius"
    bossOneqd = int(100)
    bossOnewd = int(100)
    bossOneed = int(100)
    bossOnerd = int(100)
    bossTwo = "Kled"
    bossTwoqd = int(100)
    bossTwowd = int(100)
    bossTwoed = int(100)
    bossTword = int(100)
    bossThree = "Swain"
    bossThreeqd = int(100)
    bossThreewd = int(100)
    bossThreeed = int(100)
    bossThrerd = int(100)
    finalBoss = "Mordekeiser"
    finalBossqd = int(100)
    finalBosswd = int(100)
    finalBossed = int(100)
    finalBossrd = int(100)
    # objOneC
    # objTwoC
    # objThreeC
    nothing = "Darius Auto Attacks / Moves"


    print(nothing)
    event = input()
    print(nothing)
    event = input()
    print(nothing)
    event = input()
    print(nothing)
    event = input()
    print("Darius Pulls and empowered hits,\n if caught, you lose one turn of speed DMG: "+str(int(bossOneed)+int(bossOnewd)))
    event = input()
    print("Darius swings his axe in a circle around him DMG:"+str(bossOneqd))
    event = input()

else:
    print("Error")
