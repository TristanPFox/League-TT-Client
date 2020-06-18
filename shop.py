import sys
import os
import math
import tkinter as tk
from legends import rt, lad, lap, lspd, lhp, lhpr, lm, lmr, lar

try:
    sd
except NameError:
    aegis = int(0)
    aegisAR = int(0)
    bfs = int(0)
    bfsAD = int(0)
    black = int(0)
    blackAD = int(0)
    blackHP = int(0)
    blackUCD = int(0)
    bloodt = int(0)
    bloodtAD = int(0)
    bloodtLS = int(0)
    bospd = int(0)
    bospdSPD = int(0)
    cwh = int(0)
    cwhAD = int(0)
    cwhUCD = int(0)
    deadmans = int(0)
    deadmansSPD = int(0)
    deadmansAR = int(0)
    deadmansHP  = int(0)
    deaths = int(0)
    deathsAR = int(0)
    deathsAD = int(0)
    dusk = int(0)
    duskAD = int(0)
    duskUCD = int(0)
    edge = int(0)
    edgeAD = int(0)
    edgeHP = int(0)
    reaver = int(0)
    reaverAD = int(0)
    reaverUCD = int(0)
    reaverMR = int(0)
    giants = int(0)
    giantsHP = int(0)
    ie = int(0)
    ieAD = int(0)
    ieMana = int(0)
    jf = int(0)
    jfAD = int(0)
    jfHP = int(0)
    kindle = int(0)
    kindleHP = int(0)
    kindleUCD = int(0)
    longs = int(0)
    longsAD = int(0)
    phg = int(0)
    phgHP = int(0)
    phgAD = int(0)
    pick = int(0)
    pickAD = int(0)
    hydra = int(0)
    hydraAD = int(0)
    hydraHPR = int(0)
    hydraLS = int(0)
    rejb = int(0)
    rejbHPR = int(0)
    ruby = int(0)
    rubyHP = int(0)
    saph = int(0)
    saphMana = int(0)
    dirk = int(0)
    dirkAD = int(0)
    gage = int(0)
    gageADX = int(1)
    gageHP = int(0)
    vamp = int(0)
    vampAD = int(0)
    vampLS = int(0)
    warmog = int(0)
    warmogHP = int(0)
    warmogHPR = int(0)
    warmogAR = int(0)
    ghost = int(0)
    ghostAD = int(0)
    ghostUCD = int(0)
    ghostSPD = int(0)

    # pull item log
    f = open("itemlog.txt","r")
    message = f.read()
    f.close()

def savelog():
    global message
    save_text = open("itemlog.txt", 'a')
    save_text.write(message)
    save_text.close()

# basic items
def aegisofthelegion():
    global aegis, aegisAR, message
    aegis = int(aegis) + int(1) # add item
    message = ("\nOwn "+str(aegis)+" Aegis of the Legion") # log item
    aegisAR = int(aegis)*int(30) # item stat
    savelog()
def bfsword():
    global bfs, bfsAD, message
    bfs = int(bfs) + int(1) # add item
    message = ("\nOwn "+str(bfs)+" B.F. Sword") # log item
    bfsAD = int(bfs)*int(40) # item stat
    savelog()
def bootsofspeed():
    global bospd, bospdSPD, message
    bospd = int(bospd) + int(1) # add item
    message = ("\nOwn "+str(bospd)+" Boots of Speed") # log item
    bospdSPD = int(bospd)*int(2) # item stat
    savelog()
def caulfieldswarhammer():
    global cwh, cwhAD, cwhUCD, message
    cwh = int(cwh) + int(1) # add item
    message = ("\nOwn "+str(cwh)+" Caulfields Warhammer") # log item
    cwhAD = int(cwh)*int(20) # item stat
    cwhUCD = int(cwh)*int(1) # item stat
    savelog()
def giantsbelt():
    global giants, giantsHP, message
    giants = int(giants) + int(1) # add item
    message = ("\nOwn "+str(giants)+" Giants Belt") # log item
    giantsHP = int(giants)*int(380) # item stat
    savelog()
def jaurimsfist():
    global jf, jfAD, jfHP, message
    jf = int(jf) + int(1) # add item
    message = ("\nOwn "+str(jf)+" Jaurims Fist") # log item
    jfAD = int(jf)*int(15) # item stat
    jfHP = int(jf)*int(200) # item stat
    savelog()
def kindlegem():
    global kindle, kindleHP, kindleUCD, message
    kindle = int(kindle) + int(1) # add item
    message = ("\nOwn "+str(kindle)+" Kindle Gem") # log item
    kindleHP = int(kindle)*int(100) # item stat
    kindleUCD = int(kindle)*int(1) # item stat
    savelog()
def longsword():
    global longs, longsAD, message
    longs = int(longs) + int(1) # add item
    message = ("\nOwn "+str(longs)+" Longsword") # log item
    longsAD = int(longs)*int(10) # item stat
    savelog()
def phage():
    global phg, phgAD, phgHP, message
    phg = int(phg) + int(1) # add item
    message = ("\nOwn "+str(phg)+" Phage") # log item
    phgAD = int(phg)*int(15) # item stat
    phgHP = int(phg)*int(200) # item stat
    savelog()
def pickaxe():
    global pick, pickAD, message
    pick = int(pick) + int(1) # add item
    message = ("\nOwn "+str(pick)+" Pickaxe") # log item
    pickAD = int(pick)*int(25) # item stat
    savelog()
def rejuvinationbead():
    global rejb, rejbHPR, message
    rejb = int(rejb) + int(1) # add item
    message = ("\nOwn "+str(rejb)+" Rejuvination Bead") # log item
    rejbHPR = int(rejb)*int(25) # item stat
    savelog()
def rubycrystal():
    global ruby, rubyHP, message
    ruby = int(ruby) + int(1) # add item
    message = ("\nOwn "+str(ruby)+" Ruby Crystal") # log item
    rubyHP = int(ruby)*int(150) # item stat
    savelog()
def sapphirecrystal():
    global saph, saphMana, message
    saph = int(saph) + int(1) # add item
    message = ("\nOwn "+str(saph)+" Sapphire Crystal") # log item
    saphMana = int(saph)*int(25) # item stat
    savelog()
def serrateddirk():
    global dirk, dirkAD, message
    dirk = int(dirk) + int(1) # add item
    message = ("\nOwn "+str(dirk)+" Serrated Dirk") # log item
    dirkAD = int(dirk)*int(30) # item stat
    savelog()
def tearofthegoddess():
    global tear, tearMR, message
    tear = int(tear) + int(1) # add item
    message = ("\nOwn "+str(tear)+" Tear of the Goddess") # log item
    tearMR = int(tear)*int(5)
def vampiricsceptre():
    global vamp, vampAD, vampLS, message
    vamp = int(vamp) + int(1) # add item
    message = ("\nOwn "+str(vamp)+" Vampiric Sceptre") # log item
    vampAD = int(vamp)*int(25) # item stat
    vampLS = int(vamp)*int(10)
    savelog()

# combined items
def blackcleaver():
    global black,blackAD,blackHP,blackUCD,phg,phgAD,kindle,kindleHP,kindleUCD,longs,longsAD,message
    if (int(phg)>=1)&(int(kindle)>=1)&(int(longs)>=1):
        black = int(black)+int(1)
        blackAD = int(black)*int(40)
        blackHP = int(black)*int(400)
        blackUCD = int(black)*int(1)
        phg = int(phg)-int(1)
        phgAD = int(phg)*int(15)
        phgHP = int(phg)*int(200)
        kindle = int(kindle)-int(1)
        kindleHP = int(kindle)*int(100)
        kindleUCD = int(kindle)*int(1)
        longs = int(longs)-int(1)
        longsAD = int(longs)*int(10)
        message = ("\nObtained Black Cleaver!\nCurrently have:"+str(black))
    else:
        message = ("\nNeed Phage, Kindle Gem, and Longsword to complete")
    savelog()
def bloodthirster():
    global bloodt,bloodtAD,bloodtLS,bfs,bfsAD,longs,longsAD,vamp,vampAD,vampLS,message
    if (int(bfs)>=1)&(int(longs)>=1)&(int(vamp)>=1):
        bloodt = int(bloodt)+int(1)
        bloodtAD = int(bloodt)*int(80)
        bloodtLS = int(bloodt)*int(30)
        bfs = int(bfs)-int(1)
        bfsAD = int(bfs)*int(40)
        longs = int(longs)-int(1)
        longsAD = int(longs)*int(10)
        vamp = int(vamp)-int(1)
        vampAD = int(vamp)*int(25)
        vampLS = int(vamp)*int(10)
        message = ("\nObtained Blood Thirster!\nCurrently have:"+str(bloodt))
    else:
        message = ("\nNeed B.F. Sword, Longsword, and Vampiric Sceptre to complete")
    savelog()
def deadmansplate():
    global deadmans,deadmansAR,deadmansSPD,deadmansHP,aegis,aegisAR,bospd,bospdSPD,giants,giantsHP,message
    if (int(aegis)>=1)&(int(bospd)>=1)&(int(giants)>=1):
        deadmans = int(deadmans)+int(1)
        deadmansSPD = int(lspd)*int(2)
        deadmansHP = int(deadmans)*int(425)
        deadmansAR = int(deadmans)*int(60)
        aegis = int(aegis)-int(1)
        aegisAR = int(aegis)*int(30)
        bospd = int(bospd)-int(1)
        bospdSPD = int(bospd)*int(2)
        giants = int(giants)-int(1)
        giantsHP = int(giants)*int(380)
        message = ("\nObtained Dead Mans Plate!\nCurrently have:"+str(deadmans))
    else:
        message = ("\nNeed Aegis of the Legion, Boots of Speed, and Giants Belt to complete")
    savelog()
def deathsdance():
    global deaths,deathsAR,deathsAD,deathsUCD,deathsLS,aegis,aegisAR,cwh,longsAD,vamp,vampAD,vampLS,message
    if (int(aegis)>=1)&(int(cwh)>=1)&(int(vamp)>=1):
        deaths = int(deaths)+int(1)
        deathsAR = int(deaths)*int(30)
        deathsAD = int(deaths)*int(35)
        deathsLS = int(deaths)*int(15)
        aegis = int(aegis)-int(1)
        aegisAR = int(aegis)*int(30)
        longs = int(longs)-int(1)
        longsAD = int(longs)*int(10)
        vamp = int(vamp)-int(1)
        vampAD = int(vamp)*int(25)
        vampLS = int(vamp)*int(10)
        message = ("\nObtained Deaths Dance!\nCurrently have:"+str(deaths))
    else:
        message = ("\nNeed Aegis of the Legion, Longsword, and Vampiric Sceptre to complete")
    savelog()
def duskblade():
    global dusk,duskAD,duskUCDdirk,dirkAD,cwh,cwhAD,cwhUCD,longs,longsAD,message
    if (int(dirk)>=1)&(int(cwh)>=1)&(int(longs)>=1):
        dusk = int(dusk)+int(1)
        duskAD = int(dusk)*int(60)
        duskUCD = int(dusk)*int(2)
        dirk = int(dirk)-int(1)
        dirkAD = int(dirk)*int(30)
        cwh = int(cwh)-int(1)
        cwhAD = int(cwh)*int(20)
        cwhUCD = int(cwh)*int(1)
        longs = int(longs)-int(1)
        longsAD = int(longs)*int(10)
        message = ("\nObtained Duskblade!\nCurrently have:"+str(dusk))
    else:
        message = ("\nNeed Caulfields Warhammer, Longsword, and Serrated Dirk to complete")
    savelog()
def edgeofnight():
    global edge,edgeAD,edgeHP,pick,pickAD,dirk,dirkAD,ruby,rubyHP,message
    if (int(pick)>=1)&(int(dirk)>=1)&(int(ruby)>=1):
        edge = int(edge)+int(1)
        edgeAD = int(edge)*int(55)
        edgeHP = int(edge)*int(325)
        pick = int(pick)-int(1)
        pickAD = int(pick)*int(25)
        dirk = int(dirk)-int(1)
        dirkAD = int(dirk)*int(30)
        ruby = int(ruby)-int(1)
        rubyHP = int(ruby)*int(150)
        message = ("\nObtained Edge of Night!\nCurrently have:"+str(edge))
    else:
        message = ("\nNeed Pickaxe, Ruby Crystal, and Serrated Dirk to complete")
    savelog()
def essencereaver():
    global reaver,reaverAD,reaverUCD,reaverMR,tear,tearMR,bfs,bfsAD,cwh,cwhAD,cwhUCD,message
    if (int(tear)>=1)&(int(bfs)>=1)&(int(cwh)>=1):
        reaver = int(reaver)+int(1)
        reaverAD = int(reaver)*int(40)
        reaverUCD = int(reaver)*int(1)
        reaverMR = int(reaver)*int(5)
        tear = int(tear)-int(1)
        tearMR = int(tear)*int(5)
        bfs = int(bfs)-int(1)
        bfsAD = int(bfs)*int(40)
        cwh = int(cwh)-int(1)
        cwhAD = int(cwh)*int(20)
        cwhUCD = int(cwh)*int(1)
        message = ("\nObtained Essence Reaver!\nCurrently have:"+str(reaver))
    else:
        message = ("\nNeed B.F. Sword, Caulfield Warhammer, and Tear of the Goddess to complete")
    savelog()
def infinityedge():
    global ie,ieAD,ieMana,bfs,bfsAD,pick,pickAD,saph,saphMana,message
    if (int(bfs)>=1)&(int(pick)>=1)&(int(saph)>=1):
        ie = int(ie)+int(1)
        ieAD = int(ie)*int(80)
        ieMana= int(ie)*int(50)
        bfs = int(bfs)-int(1)
        bfsAD = int(bfs)*int(40)
        pick = int(pick)-int(1)
        pickAD = int(pick)*int(25)
        saph = int(saph)-int(1)
        saphMana = int(saph)*int(25)
        message = ("\nObtained Infinity Edge!\nCurrently have:"+str(ie))
    else:
        message = ("\nNeed B.F. Sword, Pickaxe, and Sapphire Crystal to complete")
    savelog()
def ravenoushydra():
    global hydra,hydraAD,hydraHPR,hydraLS,pick,pickAD,rejb,rejbHPR,vamp,vampAD,vampLS,message
    if (int(pick)>=1)&(int(rejb)>=1)&(int(vamp)>=1):
        hydra = int(hydra)+int(1)
        hydraAD = int(hydra)*int(80)
        hydraHPR = int(hydra)*int(50)
        hydraLS = int(hydra)*int(20)
        pick = int(pick)-int(1)
        pickAD = int(pick)*int(25)
        rejb = int(rejb)-int(1)
        rejbHPR = int(rejb)*int(25)
        vamp = int(vamp)-int(1)
        vampAD = int(vamp)*int(25)
        vampLS = int(vamp)*int(10)
        message = ("\nObtained Ravenous Hydra!\nCurrently have:"+str(hydra))
    else:
        message = ("\nNeed Pickaxe, Rejuvination Bead, and Vampiric Sceptre to complete")
    savelog()
def steraksgage():
    global gage,gageADX,gageHP,jf,jfAD,jfHP,pick,pickAD,ruby,rubyHP,message
    if (int(pick)>=1)&(int(jf)>=1)&(int(ruby)>=1):
        gage = int(gage)+int(1)
        gageADX = int(gage)*float(1.5)
        gageHP = int(gage)*int(450)
        jf = int(jf)-int(1)
        jfAD = int(jf)*int(15)
        jfHP = int(jf)*int(200)
        pick = int(pick)-int(1)
        pickAD = int(pick)*int(25)
        ruby = int(ruby)-int(1)
        rubyHP = int(ruby)*int(150)
        message = ("\nObtained Steraks Gage!\nCurrently have:"+str(gage))
    else:
        message = ("\nNeed Jaurims Fist, Pickaxe, and Ruby Crystal to complete")
    savelog()
def warmog():
    global warmog,warmogHP,warmogHPR,warmogAR,aegis,aegisAR,giants,giantsHP,rejb,rejbHPR,message
    if (int(aegis)>=1)&(int(giants)>=1)&(int(rejb)>=1):
        warmog = int(warmog)+int(1)
        warmogHP = int(warmog)*int(800)
        warmogHPR = int(warmog)*int(200)
        warmogAR = int(warmog)*int(30)
        aegis = int(aegis)-int(1)
        aegisAR = int(aegis)*int(30)
        giants = int(giants)-int(1)
        giantsHP = int(giants)*int(380)
        rejb = int(rejb)-int(1)
        rejbHPR = int(rejb)*int(25)
        message = ("\nObtained Warmogs Armor!\nCurrently have:"+str(warmog))
    else:
        message = ("\nNeed Aegis of the Legion, Giants Belt, and Rejuvination Bead to complete")
    savelog()
def youmuusghostblade():
    global ghost,ghostAD,ghostUCD,ghostSPD,cwh,cwhAD,cwhUCDdirk,dirkAD,bospd,bospdSPD,message
    if (int(cwh)>=1)&(int(dirk)>=1)&(int(bospd)>=1):
        ghost = int(ghost)+int(1)
        ghostAD = int(ghost)*int(55)
        ghostUCD = int(ghost)*int(1)
        ghostSPD = int(ghost)*int(4)
        cwh = int(cwh)-int(1)
        cwhAD = int(cwh)*int(20)
        cwhUCD = int(cwh)*int(1)
        dirk = int(dirk)-int(1)
        dirkAD = int(dirk)*int(30)
        bospd = int(bospd)-int(1)
        bospdSPD = int(bospd)*int(2)
        message = ("\nObtained Youmuus Ghostblade!\nCurrently have:"+str(ghost))
    else:
        message = ("\nNeed Boots of Speed, Caulfields Warhammer, Serrated Dirk to complete")
    savelog()

def calcadap():
    global ad,ap,spd,adap,hp,hpr,mhp,mana,manam,mr,ar,ucd,message
    try:
        sdd, dbd, hp, mhp, mana, manam, hpr, mr
    except NameError:
        hp = int(lhp)
        mhp = int(lhp)
        hpr = int(lhpr)
        mana = int(lm)
        manam = int(lm)
        mr = int(lmr)
    ad = float(gageADX)*(int(lad)+int(bfsAD)+int(blackAD)+int(bloodtAD)+int(cwhAD)+int(deathsAD)+int(dirkAD)+int(duskAD)+int(edgeAD)+int(ghostAD)+int(hydraAD)+int(ieAD)+int(jfAD)+int(longsAD)+int(phgAD)+int(pickAD)+int(reaverAD)+int(vampAD))
    ap = int(lap)
    spd = int(lspd)+int(bospdSPD)+int(deadmansSPD)+int(ghostSPD)
    adap = str(ad)+" / "+str(ap)+" / "+str(spd) #calc adap
    mhp = int(mhp)+int(blackHP)+int(deadmansHP)+int(edgeHP)+int(gageHP)+int(giantsHP)+int(jfHP)+int(kindleHP)+int(phgHP)+int(rubyHP)+int(warmogHP)
    hpr = int(lhpr)+int(hydraHPR)+int(rejbHPR)+int(warmogHPR)
    manam = int(lm)+int(ieMana)+int(saphMana)
    mr = int(lmr)+int(reaverMR)
    ar = int(lar)+int(aegisAR)+int(deadmansAR)+int(deathsAR)+int(warmogAR)
    ucd = int(blackUCD)+int(cwhUCD)+int(duskUCD)+int(ghostUCD)+int(kindleUCD)+int(reaverUCD)
    if int(ucd)>int(4):
        ucd = int(4)

def openShop():
    shop = tk.Tk()
    shop.configure(bg="Grey2")
    shop.geometry('{}x{}'.format(800, 550))
    shop.title('Shop and Items ')
    left = tk.Frame(shop, bg='orange')
    right = tk.Frame(shop, bg='grey')
    shop.grid_rowconfigure(0, weight=1)
    shop.grid_columnconfigure(0, weight=1)
    shop.grid_columnconfigure(1, weight=5)
    left.grid(row=0, column=0, sticky='nsew')
    right.grid(row=0, column=1, sticky='nsew')

    # Text Window
    t = tk.Text(right, height=50, width=80, bg='white', fg='black', font=("Helvetica", 12, "bold"))
    t.pack()
    t.insert('end', open("itemlog.txt",'r').read())

    # drop down selections
    ItemList = [
        "Aegis of the Legion",
        "B.F. Sword",
        "Black Cleaver",
        "Blood Thirster",
        "Boots of Speed",
        "Caulfields Warhammer",
        "Dead Mans Plate",
        "Deaths Dance",
        "Dusk Blade",
        "Edge of Night",
        "Essence Reaver",
        "Giants Belt",
        "Infinity Edge",
        "Jaurims Fist",
        "Kindle Gem",
        "Longsword",
        "Phage",
        "Pickaxe",
        "Ravenous Hydra",
        "Rejuvination Bead",
        "Ruby Crystal",
        "Sapphire Crystal",
        "Serrated Dirk",
        "Steraks Gage",
        "Tear of the Goddess",
        "Vampiric Sceptre",
        "Warmogs Armor",
        "Youmuus Ghostblade"
    ]
    items = tk.StringVar(shop)
    items.set("Select an Item")

    opt = tk.OptionMenu(left, items, *ItemList)
    opt.config(bg='white', width=15, height=1, font=('Helvetica', 12))
    opt["menu"].config(bg='white')
    opt.pack(padx=5, pady=15)

    # shop buttons
    def obtain():
        value=items.get()
        if value == "Aegis of the Legion":
            aegisofthelegion()
        if value == "B.F. Sword":
            bfsword()
        if value == "Black Cleaver":
            blackcleaver()
        if value == "Blood Thirster":
            bloodthirster()
        if value == "Boots of Speed":
            bootsofspeed()
        if value == "Caulfields Warhammer":
            caulfieldswarhammer()
        if value == "Dead Mans Plate":
            deadmansplate()
        if value == "Deaths Dance":
            deathsdance()
        if value == "Duskblade":
            duskblade()
        if value == "Edge of Night":
            edgeofnight()
        if value == "Essence Reaver":
            essencereaver()
        if value == "Giants Belt":
            giantsbelt()
        if value == "Infinity Edge":
            infinityedge()
        if value == "Jaurims Fist":
            jaurimsfist()
        if value == "Kindle Gem":
            kindlegem()
        if value == "Longsword":
            longsword()
        if value == "Phage":
            phage()
        if value == "Pickaxe":
            pickaxe()
        if value == "Ravenous Hydra":
            ravenoushydra()
        if value == "Rejuvination Bead":
            rejuvinationbead()
        if value == "Ruby Crystal":
            rubycrystal()
        if value == "Sapphire Crystal":
            sapphirecrystal()
        if value == "Serrated Dirk":
            serrateddirk()
        if value == "Steraks Gage":
            steraksgage()
        if value == "Tear of the Goddess":
            tearofthegoddess()
        if value == "Vampiric Sceptre":
            vampiricsceptre()
        if value == "Warmogs Armor":
            warmogsarmor()
        if value == "Youmuus Ghostblade":
            youmuusghostblade()

        t.insert(tk.END,message)

    obtain = tk.Button(left, text="Obtain Selected Item", bg="white", height=3, width=25, command=obtain)
    obtain.pack(padx=5, pady=2)

    # close shop
    def shopDestroy():
        from __main__ import adapLabel,hpStat,hpStatLabel,manaStat,manaStatLabel
        calcadap()
        adapLabel.config(text=adap)
        hpStat = (str(hp)+" / "+str(mhp))
        manaStat = (str(mana)+" / "+str(manam))
        hpStatLabel.config(text=hpStat)
        manaStatLabel.config(text=manaStat)
        shop.destroy()

    closeShop = tk.Button(left, text="Save & Close Shop", bg="white", height=3, width=25, command=shopDestroy)
    closeShop.pack(padx=5, pady=2)

    shop.mainloop()
