#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:50:07 2021

@author: Emeline
"""

import tkinter as tk
import random

#global variables
error=0
wTG=""
length = 0
missingLetters=0
languages=['english','french']
currentLanguage='english'
# load list of words
with open('liste_mots.txt') as f:
    frenchWords=f.readlines()
    
with open('ukenglish.txt') as f:
    englishWords=f.readlines()

listEnglishWords=[word.strip('\n').upper() for word in englishWords]
listFrenchWords=[word.strip('\n').upper() for word in frenchWords]

dic={'english':listEnglishWords,'french':listFrenchWords} 
messages={'english':["Choose a letter","Congratulations. Click on New game to start a new game.","Hanged! Click on New game to start a new game."],"french":["Choisissez une lettre","Bravo. Cliquez sur New Game pour une nouvelle partie","Dommage. Cliquez sur recommencer pour une nouvelle partie"]}
############################################################################
# Functions
############################################################################
# display the solution
def solution():
    for count,letter in enumerate(wTG):
        labChar[count].configure(text=letter,fg='red')
    labImage.configure(image=images[7])

# Randomly choose a word
def chooseWord():
    global length,currentLanguage
    words=dic[currentLanguage]
    word=words[random.randint(0,len(words))] 
    wTG=word.rstrip( )
    length=len(wTG)
    return wTG

def initiate():
    global length,labChar
    labChar=[]
    for i in range(length):
        labChar.append(tk.Label(can,text='_',font=("Helvetica", 25)))
    for i in range(len(labChar)):
        labChar[i].pack(side=tk.LEFT)

def playFrench():
    '''
    Launches a new game with languages settings = french 

    Returns
    -------
    None.

    '''
    global currentLanguage
    currentLanguage='french'
    game()
 
def playEnglish():
    '''
    Launches a new game with languages settings =english

    Returns
    -------
    None.

    '''
    global currentLanguage
    currentLanguage='english'
    game()   
 
def game():
    global error,wTG,can,missingLetters
    can.destroy()
    can = tk.Canvas(window,bg='black',height=800,width=500)
    can.pack(side=tk.TOP)
    error=0
    labImage.configure(image=images[error])
    wTG=chooseWord()
    missingLetters=len(wTG)
    initiate()
    labMessage.configure(text=messages[currentLanguage][0])
    for i in range(26):
        butLetters[i].configure(bg='white', fg='black')

# verify whether the letter is in the word
def verifyNew(x):
    letter=chr(x)
    indice=x-65
    global error,wTG,missingLetters
    if missingLetters>0:
        letterIn=False
        if error<7:
            for count, char in enumerate(wTG) :
                if char==letter:
                    labChar[count].configure(text=letter)
                    missingLetters-=1
                    letterIn=True
                    butLetters[indice].configure(bg='blue', fg='white')
            if not letterIn:
                error+=1
                labImage.configure(image=images[error])
                butLetters[indice].configure(bg='red', fg='white')
            if missingLetters==0:
                labMessage.configure(text=messages[currentLanguage][1])
        if error==7:
            solution()
            labMessage.configure(text=messages[currentLanguage][2])
            

############################################################################
# graphics window
############################################################################
window = tk.Tk()
window.title("Hangman-game")

top = tk.Menu(window)
window.config(menu=top)
jeu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=jeu)
jeu.add_command(label='New game', command=game)
jeu.add_command(label='Close', command=window.destroy)
settings = tk.Menu(top, tearoff=False)
top.add_cascade(label='Language', menu=settings)
settings.add_command(label='English', command=playEnglish)
settings.add_command(label='French', command=playFrench)

frame=tk.Frame(window)
frame.pack(side=tk.TOP)
can = tk.Canvas(window,bg='black',height=500,width=500)
can.pack(side=tk.LEFT)
frame2=tk.Frame(window)
frame2.pack(side=tk.BOTTOM)

labMessage=tk.Label(frame,text="Choose a letter")
labMessage.pack(side=tk.TOP)


#buttons letters
butLetters=[tk.Button(frame,text=chr(65+i),bg='white', fg='black',command=lambda x=65+i:verifyNew(x)) for i in range(26)]
for i in range(len(butLetters)):
    butLetters[i].pack(side=tk.LEFT)

#labels 
# load list of images
images=[]
for card in range(8):
    name='Images/pendu_'+str(card)+'.gif'
    loadedCard=tk.PhotoImage(file=name)
    images.append(loadedCard)

labImage=tk.Label(window,image=images[0])
labImage.pack(fill=tk.BOTH)

# Representation of the word to be guessed
labChar=[]
for i in range(length):
    labChar.append(tk.Label(can,text='_',font=("Helvetica", 25)))
for i in range(len(labChar)):
    labChar[i].pack(side=tk.LEFT)

# start-up
game()
window.mainloop()
