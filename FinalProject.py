"""
Nathan Miller
Final Project
Programming for IT CIS-153
a gui that allows users to select a character from the video game "League of Legends", which will then display info on said character, such as:
name, title, class, backstory, tips(from both ally and enemy perspective), abilities, and features artwork of the character as a background.
"""


import os
import json
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def main():
    def loadSplash():
        
        #takes entry data, puts it into an image url, customized by entry, uses image as background for data
        champInput = champEntry.get()
        champInput = str(champInput).capitalize()
        champInput = champInput.replace(" ","")
        
        
        
        #testing for champions with spaces in their names. Fixes capitalization for dictionary key usage and file path recognition.
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
        
        
        
        
        
        
        
        #pulls image info from web into variable
        champURL = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champInput}_0.jpg"        
        getArt = requests.get(champURL)        
        artData = BytesIO(getArt.content)
        bgImage = Image.open(artData)
        bgFULL = ImageTk.PhotoImage(bgImage)

        #places the image into a label        
        splashArt.configure(width='1215', height='717')
        splashArt.create_image(0, 0, anchor=NW, image=bgFULL)
        splashArt.image = bgFULL
        

        


            
        #####champion data            
        try:
            dir = os.path.dirname(os.path.realpath('FinalProject.py'))
             
            #reformats entry to fit filename    
            champInputJSON = champInput + ".json"
            locateChampData = os.path.join(dir , 'ddragon\\13.23.1\\data\\en_US\\champion' , champInputJSON)

            
            #loads file with corresponding name
            fhand = open(locateChampData , encoding="utf8")
            fileLoad = json.load(fhand)
            fhand.close()
            newDict = fileLoad['data']
            
            

            #initial dictionary read from champion JSON
            champDict = newDict[champInput]
            
            
            
            #data drawn to canvas
            #name and title
            cnameData = str(champDict['name'] + ",\n" + champDict['title'].replace("<br>"," "))                     
            splashArt.create_text(10, 10, width=300,
            text=cnameData, fill="white", font=("Arial Black", 26), anchor='nw')


            #tags (type of character/class)
            tagList = champDict['tags']
            
            tagString = ", "            
            tagString = tagString.join(str(t) for t in tagList)
            
            tagData = str("Class:\n" + tagString)
            splashArt.create_text(400, 10,
            text=tagData, fill="white", font=("Arial", 22), anchor='nw')

            
            #background story
            loreData = str("About:\n" + champDict['lore'] + '\n')
            splashArt.create_text(750, 10, width=450,
            text=loreData, fill="white", font=("Arial", 12), anchor='nw')
            
            
            #tips for playing the character
            allytipList = champDict['allytips']
            
            allytipString = ", "            
            allytipString = allytipString.join(str(t) for t in allytipList)
            
            allytipData = str("Tips for playing " + champInput + ":\n" + allytipString)
            splashArt.create_text(10, 160, width=300,
            text=allytipData, fill="white", font=("Arial", 12), anchor='nw')
            
            
            #tips for playing against the character
            enemytipList = champDict['enemytips']
            
            enemytipString = ", "            
            enemytipString = enemytipString.join(str(t) for t in enemytipList)
            
            enemytipData = str("Tips for playing against " + champInput + ":\n" + enemytipString)
            splashArt.create_text(400, 160, width=300,
            text=enemytipData, fill="white", font=("Arial", 12), anchor='nw')




            #passive ability
            passiveDict = champDict['passive']
            
            pdesc = str(passiveDict['name'] + "\n" + passiveDict['description'].replace("<br>"," "))
            splashArt.create_text(10, 400, width=200,
            text=pdesc, fill="white", font=("Arial", 12), anchor='nw')
            
            
            
            
            #data for main abilities
            spellDict = champDict['spells']
            
            

            qspell = spellDict[0]  
            qdesc = str(qspell['name'] + "\n" + qspell['description'].replace("<br>"," "))
            splashArt.create_text(260, 400, width=200,
            text=qdesc, fill="white", font=("Arial", 12), anchor='nw')
            

                     
            wspell = spellDict[1]
            wdesc = str(wspell['name'] + "\n" + wspell['description'].replace("<br>"," "))
            splashArt.create_text(510, 400, width=200,
            text=wdesc, fill="white", font=("Arial", 12), anchor='nw')
            
            

            espell = spellDict[2]
            edesc = str(espell['name'] + "\n" + espell['description'].replace("<br>"," "))
            splashArt.create_text(760, 400, width=200,
            text=edesc, fill="white", font=("Arial", 12), anchor='nw')
            
            

            rspell = spellDict[3]
            rdesc = str(rspell['name'] + "\n" + rspell['description'].replace("<br>"," "))
            splashArt.create_text(1010, 400, width=200,
            text=rdesc, fill="white", font=("Arial", 12), anchor='nw')
            

        #in the case of incorrect entry
        except FileNotFoundError:
            print("Champion not found.")

        return

    
    

        
        

    #gui setup
    root = Tk()
    root.title("Final Project")

    #entry for champion name
    champLabel = Label(root, text="Enter a champion:")
    champLabel.pack(pady=10,padx=10)
    champEntry = Entry(root, width=50)
    champEntry.pack(pady=10,padx=10)

    #button to load champion data
    loadChampData = Button(root, text="Load Champion Data", command=loadSplash)
    loadChampData.pack(pady=10)


    #label to display the image
    #splashArt = Label(root)
    splashArt = Canvas(root)
    splashArt.pack()
    


    root.mainloop()
    
    return
main()

