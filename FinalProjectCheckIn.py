"""
a gui that allows users to choose a character, which will then display info on said character, such as:
name, title, tags(class i think idk needs more info), lore(doesnt show full lore idk why), tips(from both ally and enemy perspective, inconsistent), spells


need to make tkinter gui for champ search, then create page for champ with a decent layout

check to see if its possible to use icons/images for champ/spells idk

"""

###### some of this first few lines of code may be incorrect, need to double check

import os
import json
import tkinter


def championInfo():
    try:
        dir = os.path.dirname(os.path.realpath('FinalProject.py'))
        champInput = input('input a champion: ').capitalize()
        champInput = champInput.replace(" ","")
        
        
        
        ###testing for champions with spaces in their names. Fixes capitalization for dictionary key usage.
        if champInput == "Aurelionsol":
            champInput = "AurelionSol"
        if champInput == "Drmundo":
            champInput = "DrMundo"
        if champInput == "Jarvaniv" or champInput == "Jarvan":
            champInput = "JarvanIV"
        if champInput == "Kogmaw":
            champInput = "KogMaw"
        if champInput == "Ksante":
            champInput = "KSante"
        if champInput == "Leesin":
            champInput = "LeeSin"
        if champInput == "Masteryi":
            champInput = "MasterYi"
        if champInput == "Missfortune":
            champInput = "MissFortune"
        ###unique character id that does not match character's name.
        if champInput == "Wukong" or champInput == "Monkeyking":
            champInput = "MonkeyKing"
        if champInput == "Reksai":
            champInput = "RekSai"
        if champInput == "Tahmkench":
            champInput = "TahmKench"
        if champInput == "Twistedfate":
            champInput = "TwistedFate"
        if champInput == "Xinzhao":
            champInput = "XinZhao"
            
            
        champInputJSON = champInput + ".json"
        locateChampData = os.path.join(dir , 'ddragon\\13.23.1\\data\\en_US\\champion' , champInputJSON)

        
        
        fhand = open(locateChampData , encoding="utf8")
        fileLoad = json.load(fhand)
        fhand.close()
        newDict = fileLoad['data']
        

        champDict = newDict[champInput]
        print(champDict['name'])
        print(champDict['title'])
        print("class: " , champDict['tags'], '\n')
        print("About:\n" , champDict['lore'], '\n')
        print("Tips for playing \b", champInput , ":\n" , champDict['allytips'], '\n')
        print("Tips for playing against \b", champInput , ":\n" , champDict['enemytips'], '\n')




        passiveDict = champDict['passive']
        print(passiveDict['name'])
        print(passiveDict['description'],'\n')
        
        
        ### SPELLS ARE A LIST OF DICTIONARIES, EACH SPELL IS A PART OF THE LIST
        spellDict = champDict['spells']

        ######section for spells
        qspell = spellDict[0]
        print(qspell['name'])
        qdesc = qspell['description'].replace("<br>"," ")
        print(qdesc , '\n')

        wspell = spellDict[1]
        print(wspell['name'])
        wdesc = wspell['description'].replace("<br>"," ")
        print(wdesc , '\n')

        espell = spellDict[2]
        print(espell['name'])
        edesc = espell['description'].replace("<br>"," ")
        print(edesc , '\n')

        rspell = spellDict[3]
        print(rspell['name'])
        rdesc = rspell['description'].replace("<br>"," ")
        print(rdesc, '\n')



    except FileNotFoundError:
        print("Champion not found.")
        
        
    return

championInfo()





#############################
#SET UP GUI
#############################




