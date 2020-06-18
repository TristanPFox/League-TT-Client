import sys
import os
from __main__ import selLegend

if selLegend == "Jhin":
    global p
    p = "Every 4th shot does 50% more damage\nTakes one turn to reload after the fourth shot\nAuto reload after 2 turns of not attacking"
    qt = int(3) #q cd
    qd = int(25) #q damage
    qm = int(20) #q mana cost
    wt = int(3) #w cd
    wd = int(25) #w damage
    wm = int(30) #w mana cost
    et = int(3) #e cd
    ed = int(25) #e damage
    em = int(20) #e mana cost
    rt = int(6) #r cd
    rd = int(25) #r damage
    rm = int(80) #r mana cost
    lad = int(100) #base AD
    lap = int(20) #base AP
    lspd = int(220) #base speed
    lhp = int(1000) #health
    lhpr = int(20) #health regen
    lm = int(100) #mana
    lmr = int(10) #mana regen
    lar = int(0) #armor
