import sys
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import time

version = "v0.0.1"

# Check for updates
print("Checking for updates from GitHub.com/TristanPFox...")
os.system("git pull")

try:
    t
except NameError:
    t = int(0)
    qCD = int(0)
    wCD = int(0)
    eCD = int(0)
    rCD = int(0)
    f = open("itemlog.txt","w+")
    f.close()

# selLegend = "Jhin"

# main menu
mainBg = "#4dc1ff"
main = tk.Tk()
main.configure(bg=mainBg)
main.geometry('{}x{}'.format(600, 500))
main.title('League Tabletop Main Menu '+version)

# frame creation
mainLabelFrame = tk.Frame(main, bg=mainBg, height=200, width=550)
mainLegendFrame = tk.Frame(main, bg=mainBg, height=100, width=550)
mainDiffFrame = tk.Frame(main, bg=mainBg, height=100, width=550)
mainChapterFrame = tk.Frame(main, bg=mainBg, height=100, width=550)
mainRulesFrame = tk.Frame(main, bg=mainBg, height=100, width=550)
mainPartyFrame = tk.Frame(main, bg=mainBg, height=100, width=550)
mainPlayFrame = tk.Frame(main, bg=mainBg, height=100, width=550)
# weight adding to frames and assigning frames
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
main.rowconfigure(2, weight=1)
main.rowconfigure(3, weight=1)
main.rowconfigure(4, weight=1)
main.rowconfigure(5, weight=1)
main.rowconfigure(6, weight=1)
mainLabelFrame.grid(row=0, column=0)
mainLegendFrame.grid(row=1, column=0)
mainDiffFrame.grid(row=2, column=0)
mainChapterFrame.grid(row=3, column=0)
mainRulesFrame.grid(row=4, column=0)
mainPartyFrame.grid(row=5, column=0)
mainPlayFrame.grid(row=6, column=0)
# sub-frame grid creation and weight
mainLegendFrame.grid_rowconfigure(0, weight=1)
mainLegendFrame.grid_columnconfigure(0, weight=1)
mainLegendFrame.grid_columnconfigure(1, weight=1)
mainDiffFrame.grid_rowconfigure(0, weight=1)
mainDiffFrame.grid_columnconfigure(0, weight=1)
mainDiffFrame.grid_columnconfigure(1, weight=1)
mainChapterFrame.grid_rowconfigure(0, weight=1)
mainChapterFrame.grid_columnconfigure(0, weight=1)
mainChapterFrame.grid_columnconfigure(1, weight=1)
mainRulesFrame.grid_rowconfigure(0, weight=1)
mainRulesFrame.grid_rowconfigure(1, weight=1)
mainRulesFrame.grid_columnconfigure(0, weight=1)
mainRulesFrame.grid_columnconfigure(1, weight=1)
mainPartyFrame.grid_rowconfigure(0, weight=1)
mainPartyFrame.grid_columnconfigure(0, weight=1)
mainPartyFrame.grid_columnconfigure(1, weight=1)

# legend dropdown
welcomeLabel = tk.Label(mainLabelFrame, text='Table Top League Menu', bg=mainBg, height=2, font=("Helvetica", 18, "bold"))
welcomeLabel.pack()
legSelLabel = tk.Label(mainLegendFrame, text='Select a Legend:', bg=mainBg, height=2, font=("Helvetica", 14, "bold"))
legSelLabel.grid(row=0, column=0)
LegendList = [
    "Jhin",
    "Kayn",
    "Shen",
    "Zed"
]
chosenLegend = tk.StringVar(main)
chosenLegend.set("None Selected")
legendDrop = tk.OptionMenu(mainLegendFrame, chosenLegend, *LegendList)
legendDrop.config(bg='white', width=25, height=1, font=('Helvetica', 12))
legendDrop["menu"].config(bg='white')
legendDrop.grid(row=0, column=1, padx=10)
def useLegend():
    global selLegend,legCheck
    sl=chosenLegend.get()
    if sl == "Jhin":
        selLegend = "Jhin"
        legCheck = 1
    elif sl == "Kayn":
        selLegend = "Kayn"
        legCheck = 1
    elif sl == "Shen":
        selLegend = "Shen"
        legCheck = 1
    elif sl == "Zed":
        selLegend = "Zed"
        legCheck = 1
    else:
        legCheck = 0

# difficulty dropdown
diffSelLabel = tk.Label(mainDiffFrame, text='Select a Difficulty:', bg=mainBg, height=2, font=("Helvetica", 14, "bold"))
diffSelLabel.grid(row=0, column=0)
diffList = [
    "Iron IV - Adaptive Difficulty: Off",
    "Plat II - Adaptive Difficulty: ON",
    "Challenger - Autofilled Teammate Picked Yasuo"
]
chosenDiff = tk.StringVar(main)
chosenDiff.set("None Selected")
diffDrop = tk.OptionMenu(mainDiffFrame, chosenDiff, *diffList)
diffDrop.config(bg='white', width=25, height=1, font=('Helvetica', 12))
diffDrop["menu"].config(bg='white')
diffDrop.grid(row=0, column=1, padx=10)
def useDiff():
    global selDiff,diffCheck
    ud=chosenDiff.get()
    if ud == "Iron IV - Adaptive Difficulty: Off":
        selDiff = "Iron"
        diffCheck = 1
    elif ud == "Plat II - Adaptive Difficulty: ON":
        selDiff = "Plat"
        diffCheck = 1
    elif ud == "Challenger - Autofilled Teammate Picked Yasuo":
        selDiff = "Challenger"
        diffCheck = 1
    else:
        diffCheck = 0
# gamemode dropdown
GMSelLabel = tk.Label(mainChapterFrame, text='Select a Chapter:', bg=mainBg, height=2, font=("Helvetica", 14, "bold"))
GMSelLabel.grid(row=0, column=0)
GMList = [
    "Ionia vs Noxus"
]
chosenGM = tk.StringVar(main)
chosenGM.set("None Selected")
GMDrop = tk.OptionMenu(mainChapterFrame, chosenGM, *GMList)
GMDrop.config(bg='white', width=25, height=1, font=('Helvetica', 12))
GMDrop["menu"].config(bg='white')
GMDrop.grid(row=0, column=1, padx=10)
def useGM():
    global selGM,gmCheck
    ugm=chosenGM.get()
    if ugm == "Ionia vs Noxus":
        selGM = "IvN"
        gmCheck = 1
    else:
        gmCheck = 0
# Rules and Items Buttons
def openItems():
    os.system('notepad items.txt')
def openRules():
    os.system('notepad rules.txt')
showRules = tk.Button(mainRulesFrame, text="Rules", width=25, height=3, command=openRules)
showRules.grid(row=0, column=0, padx=10, pady=5)
showItems = tk.Button(mainRulesFrame, text="Items", width=25, height=3, command=openItems)
showItems.grid(row=0, column=2, padx=10, pady=5)

def partyLeadCheck():
    if (var1.get() == 1):
        l = 'You are Party Lead'
        print(l)
        # add (open boss script) here

var1 = tk.IntVar()
plcButton = tk.Checkbutton(mainPartyFrame, text='Party Leader',variable=var1, onvalue=1, offvalue=0, bg=mainBg, font=('Helvetica', 12), command=partyLeadCheck)
plcButton.pack()

def gameInit():
    global legCheck,diffCheck,gmCheck
    useLegend()
    useDiff()
    useGM()
    print(str(legCheck), str(diffCheck), str(gmCheck))
    if ((legCheck==1) & (diffCheck==1) & (gmCheck==1)):
        print("All Selected!")
        main.destroy()
    else:
        tk.messagebox.showinfo(title="Not Ready!", message="Can't Start Yet!\nBe Sure to Select a Legend, Difficulty, and Chapter!")

startGame = tk.Button(mainPlayFrame, text="Start Game", width=25, height=3, command=gameInit)
startGame.grid(row=0, column=0, padx=10, pady=5)

main.mainloop()


from legends import p,qt,qd,qm,wt,wd,wm,et,ed,em,rt,rd,rm,lad,lap,lspd,lhp,lhpr,lm,lmr,lar,legPortrait

# Legend GUI
legend = tk.Tk()
legend.configure(bg="Grey2")
legend.geometry('{}x{}'.format(550, 800))
legend.title('League Tabletop Client '+version)

# main containers
portrait = tk.Frame(legend, bg='blue', height=150)
passive = tk.Frame(legend, bg='grey', height=50)
ability = tk.Frame(legend, bg='green', height=350)
footer = tk.Frame(legend, bg='yellow', height=50)

# layout of the main containers
legend.grid_rowconfigure(0, weight=0)
legend.grid_rowconfigure(1, weight=0)
legend.grid_rowconfigure(2, weight=1)
legend.grid_rowconfigure(3, weight=0)
legend.grid_columnconfigure(0, weight=1)
portrait.grid(row=0, sticky="nsew")
passive.grid(row=1, sticky="ew")
ability.grid(row=2, sticky="nsew")
footer.grid(row=3, sticky="nsew")

# distributing equal weight (priority) to all frame columns
passive.grid_rowconfigure(0, weight=1)
passive.grid_columnconfigure(0, weight=1)
passive.grid_columnconfigure(1, weight=1)
passive.grid_columnconfigure(2, weight=1)
passive.grid_columnconfigure(3, weight=1)
ability.grid_rowconfigure(0, weight=1)
ability.grid_rowconfigure(1, weight=1)
ability.grid_columnconfigure(0, weight=1)
ability.grid_columnconfigure(1, weight=1)
footer.grid_rowconfigure(0, weight=1)
footer.grid_rowconfigure(1, weight=1)
footer.grid_columnconfigure(0, weight=1)
footer.grid_columnconfigure(1, weight=1)
footer.grid_columnconfigure(2, weight=1)
footer.grid_columnconfigure(3, weight=1)
footer.grid_columnconfigure(4, weight=1)

# portrait
#tk.Label(bg=loginBg).pack() # Spacer
image = Image.open("portraits/"+legPortrait)
image = image.resize((550,400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
portrait = tk.Label(portrait,image=photo, bg="grey", text="\n\n\n")
portrait.image = photo
portrait.pack()

# passive
passiveTitle = tk.Label(passive, text="Passive:", bg='grey',  font=("Helvetica", 14, "bold"))
passiveTitle.grid(row=0, column=0, pady=5)
passiveLabel = tk.Label(passive, text=p, bg='grey', font=("Helvetica", 10, "bold"))
passiveLabel.grid(row=0, column=1, columnspan=3, pady=5)

# ability button adjustments
apx = 10
apy = 0
ah = 4
abg = "white"
afg = "black"

# use shop
import shop
def startshop():
    shop.openShop()

# footer stats
try:
    adap
except NameError:
    shop.calcadap()
from shop import adap

statsLabel = tk.Label(footer, text='AD / AP / Speed', bg='cyan')
statsLabel.grid(row=0, column=0, pady=0, sticky="nsew")
adapLabel = tk.Label(footer, text=adap, bg='cyan')
adapLabel.grid(row=1, column=0, pady=0, sticky="nsew")

# shop button
shopButton = tk.Button(footer, text='Open Shop/Items', height=2, bg="white", fg="black", command=startshop)
shopButton.grid(row=0, column=1, sticky="ew", padx=15, pady=10, rowspan=2)

# battle menu
def openBattle():
    global hpStat, hpStatLabel, manaStat, manaStatLabel
    # main containers
    battle = tk.Tk()
    battle.configure(bg="Grey2")
    battle.geometry('{}x{}'.format(600, 400))
    battle.title('Battle Menu')
    nameFrame = tk.Frame(battle, bg='cyan')
    questFrame = tk.Frame(battle, bg='lime')
    dmgFrame = tk.Frame(battle, bg='pink')
    statsFrame = tk.Frame(battle, bg='white')

    # layout of containers
    battle.grid_rowconfigure(0, weight=0)
    battle.grid_rowconfigure(1, weight=1)
    battle.grid_rowconfigure(2, weight=1)
    battle.grid_rowconfigure(3, weight=1)
    battle.grid_columnconfigure(0, weight=1)
    nameFrame.grid(row=0, column=0, sticky='nsew')
    questFrame.grid(row=1, column=0, sticky='nsew')
    dmgFrame.grid(row=2, column=0, sticky='nsew')
    statsFrame.grid(row=3, column=0, sticky='nsew')
    questFrame.grid_rowconfigure(0, weight=1)
    questFrame.grid_columnconfigure(0, weight=1)
    questFrame.grid_columnconfigure(1, weight=1)
    questFrame.grid_columnconfigure(2, weight=1)
    questFrame.grid_columnconfigure(3, weight=1)
    dmgFrame.grid_rowconfigure(0, weight=1)
    dmgFrame.grid_columnconfigure(0, weight=1)
    dmgFrame.grid_columnconfigure(1, weight=1)
    dmgFrame.grid_columnconfigure(2, weight=1)
    dmgFrame.grid_columnconfigure(3, weight=1)
    statsFrame.grid_rowconfigure(0, weight=1)
    statsFrame.grid_rowconfigure(1, weight=1)
    statsFrame.grid_columnconfigure(0, weight=1)

    # Labels and buttons
    nameLabel = tk.Label(nameFrame, text=selLegend, bg='cyan', font=("Helvetica", 18, "bold"))
    nameLabel.pack()
    objOne = tk.Button(questFrame, text="Objective 1 Complete", bg="white", height=3, width=25)
    objOne.grid(row=0, column=0, padx=5, pady=2)
    objTwo = tk.Button(questFrame, text="Objective 2 Complete", bg="white", height=3, width=25)
    objTwo.grid(row=0, column=1, padx=5, pady=2)
    objThree = tk.Button(questFrame, text="Objective 3 Complete", bg="white", height=3, width=25)
    objThree.grid(row=0, column=2, padx=5, pady=2)
    objBoss = tk.Button(questFrame, text="Boss Complete", bg="white", height=3, width=25)
    objBoss.grid(row=0, column=3, padx=5, pady=2)
    dmgLabel = tk.Label(dmgFrame, text="Damage Taken", bg='pink', font=("Helvetica", 14, "bold"))
    dmgLabel.grid(row=0, column=0, padx=5)
    dmgTaken = tk.StringVar(dmgFrame)
    dmgEntry = tk.Entry(dmgFrame, textvariable=dmgTaken, font=("Helvetica", 12, "bold"), width=24)
    dmgEntry.grid(row=0, column=1, columnspan=2, ipadx=3, padx=10, pady=3)
    dmgButton = tk.Button(dmgFrame, text="Calculate Damage", bg="white", height=3, width=25)
    dmgButton.grid(row=0, column=3, padx=5)
    hpStatLabel = tk.Label(statsFrame, text=hpStat, bg='red', fg='white', font=("Helvetica", 16, "bold"))
    hpStatLabel.grid(row=0, column=0)
    manaStatLabel = tk.Label(statsFrame, text=manaStat, bg='blue', fg='white', font=("Helvetica", 16, "bold"))
    manaStatLabel.grid(row=1, column=0)

    def takeDamage():
        global hp, mhp, hpStat, hpStatLabel
        from shop import mhp,ar
        dmg = dmgTaken.get()

        if int(dmg) < int(0): #if negative dmg, then heal
            print("Dmg under 0 = Heal")
            if int(hp)<int(mhp): #check if health is lower than max
                heal = int(hp)-int(mhp)
                print("Missing HP:",heal)
                if int(heal)>=int(dmg): # prevent over healing
                    hp = int(mhp)
                    print("Healed to Max")
                else:
                    hp = int(hp)-int(dmg)
                    print("Healed")
                hpStat = (str(hp)+" / "+str(mhp))
                hpStatLabel.configure(text=hpStat)
            else:
                print("Healing error")
        else:
            print("Health:",hp,"+ Armor:",ar,"- Damage:",dmg)
            if int(ar)<int(dmg):
                dmg = int(dmg)-int(ar)
                hp = int(hp)-int(dmg)
            else:
                print("Armor blocked all damage")
                tk.messagebox.showinfo(title="You're Hard", message="Armor negated all damage")
            # check for death
            if int(hp) <= int(0):
                hp = int(0)
                tk.messagebox.showinfo(title="Defeated", message="You're dead as fuck, whatta little bitch baby \n Client Closing...")
                legend.destroy()
                battle.destroy()
            hpStat = (str(hp)+" / "+str(mhp))
            hpStatLabel.configure(text=hpStat)
    # give damage command after def has been made
    dmgButton.config(command=takeDamage)


    battle.mainloop()


battleButton = tk.Button(footer, text='Battle Menu', bg='white', fg='black', height=2, command=openBattle)
battleButton.grid(row=0, column=2, rowspan=2, sticky='ew')

# set stats
try:
    hpStat, dmgTaken, manaStat
except NameError:
    global hp,mhp,mana,manam,ar
    import shop
    shop.calcadap()
    from shop import hp,mhp,mana,manam,ar
    hpStat = (str(hp)+" / "+str(mhp))
    manaStat = (str(mana)+" / "+str(manam))

# q ability
def useQ():
    global t, qCD, qt, mana, manam, manaStat
    if int(mana) >= int(qm):
        mana = int(mana) - int(qm)
        qUsed = int(t)
        qEnd = int(t) + int(qt)
        qCD = int(qEnd) - int(qUsed)
        qButton.config(text=str(qCD))
        print(qUsed, qEnd, qCD)
        qButton.config(command="")
        manaStat = (str(mana)+" / "+str(manam))
        manaStatLabel.config(text=manaStat)
    else:
        tk.messagebox.showinfo(title="Mana Warning!", message="Not enough mana for Q Ability")

qButton = tk.Button(ability, text="Use Q", bg=abg, fg=afg, height=ah, font=("Helvetica", 14, "bold"), command=useQ)
qButton.grid(row=0, column=0, sticky="ew", padx=apx, pady=apy)

# w ability
def useW():
    global t, wCD, wt, mana, manaStat
    if int(mana) >= int(wm):
        mana = int(mana) - int(wm)
        wUsed = int(t)
        wEnd = int(t) + int(wt)
        wCD = int(wEnd) - int(wUsed)
        wButton.config(text=str(wCD))
        print(wUsed, wEnd, wCD)
        wButton.config(command="")
        manaStat = (str(mana)+" / "+str(manam))
        manaStatLabel.config(text=manaStat)
    else:
        tk.messagebox.showinfo(title="Mana Warning!", message="Not enough mana for W Ability")

wButton = tk.Button(ability, text="Use W", bg=abg, fg=afg, height=ah, font=("Helvetica", 14, "bold"), command=useW)
wButton.grid(row=0, column=1, sticky="ew", padx=apx, pady=apy)

# e ability
def useE():
    global t, eCD, et, mana, manaStat
    if int(mana) >= int(em):
        mana = int(mana) - int(em)
        eUsed = int(t)
        eEnd = int(t) + int(et)
        eCD = int(eEnd) - int(eUsed)
        eButton.config(text=str(eCD))
        print(eUsed, eEnd, eCD)
        eButton.config(command="")
        manaStat = (str(mana)+" / "+str(manam))
        manaStatLabel.config(text=manaStat)
    else:
        tk.messagebox.showinfo(title="Mana Warning!", message="Not enough mana for E Ability")


eButton = tk.Button(ability, text="Use E", bg=abg, fg=afg, height=ah, font=("Helvetica", 14, "bold"), command=useE)
eButton.grid(row=1, column=0, sticky="ew", padx=apx, pady=apy)

# r ability
def useR():
    global t, rCD, rt, mana, manaStat
    import shop
    shop.calcadap()
    from shop import ucd
    if int(mana) >= int(rm):
        mana = int(mana) - int(rm)
        rUsed = int(t)
        rEnd = int(t) + int(rt)
        rCD = int(rEnd) - int(rUsed) - int(ucd)
        rButton.config(text=str(rCD))
        print(rUsed, rEnd, rCD, ucd)
        rButton.config(command="")
        manaStat = (str(mana)+" / "+str(manam))
        manaStatLabel.config(text=manaStat)
    else:
        tk.messagebox.showinfo(title="Mana Warning!", message="Not enough mana for R Ability")

rButton = tk.Button(ability, text="Use R", bg=abg, fg=afg, height=ah, font=("Helvetica", 14, "bold"), command=useR)
rButton.grid(row=1, column=1, sticky="ew", padx=apx, pady=apy)

# Turn timer
def nextTurn():
    #increase turn timer
    global t
    t = t + int(1)
    turnCounter.config(text=str(t))
    import shop
    shop.calcadap()
    from shop import mhp,hpr,manam,mr
    # apply health regen
    global hp, hpStat
    if int(hp) < int(mhp):
        hp = int(hp)+int(hpr)
        hpStat = (str(hp)+" / "+str(mhp))
        hpStatLabel.configure(text=hpStat)
    # apply mana regen
    global mana, manaStat
    if int(mana) < int(manam):
        mana = int(mana)+int(mr)
        manaStat = (str(mana)+" / "+str(manam))
        manaStatLabel.config(text=manaStat)
    # decrease ability Cooldowns
    global qCD
    if int(qCD) != int(0):
        qCD = int(qCD) - int(1)
        if int(qCD) != int(0):
            qButton.config(text=str(qCD))
        else:
            qButton.config(text="Use Q")
            qButton.config(command=useQ)
    global wCD
    if int(wCD) != int(0):
        wCD = int(wCD) - int(1)
        if int(wCD) != int(0):
            wButton.config(text=str(wCD))
        else:
            wButton.config(text="Use W")
            wButton.config(command=useW)
    global eCD
    if int(eCD) != int(0):
        eCD = int(eCD) - int(1)
        if int(eCD) != int(0):
            eButton.config(text=str(eCD))
        else:
            eButton.config(text="Use E")
            eButton.config(command=useE)
    global rCD
    if int(rCD) != int(0):
        rCD = int(rCD) - int(1)
        if int(rCD) != int(0):
            rButton.config(text=str(rCD))
        else:
            rButton.config(text="Use R")
            rButton.config(command=useR)

turnNext = tk.Button(footer, text='Next Turn', height=2, bg="white", fg="black", command=nextTurn)
turnNext.grid(row=0, column=3, sticky="ew", padx=15, pady=10, rowspan=2)
turnLabel = tk.Label(footer, text='Turn #', bg='cyan')
turnLabel.grid(row=0, column=4, sticky="nsew")
turnCounter = tk.Label(footer, text=str(t), bg='cyan')
turnCounter.grid(row=1, column=4, sticky="nsew")

legend.mainloop()
