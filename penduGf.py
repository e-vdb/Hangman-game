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
# load list of words
with open('liste_mots.txt') as f:
    words=f.readlines()
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
    global length
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
        
def game():
    global error,wTG,can,missingLetters
    can.destroy()
    can = tk.Canvas(window,bg='black',height=800,width=500)
    can.pack(side=tk.TOP)
    error=0
    labImage.configure(image=images[error])
    #for count in range(length):
        #labChar[count].configure(text='_')
    wTG=chooseWord()
    missingLetters=len(wTG)
    initiate()
    labMessage.configure(text="Choisissez une lettre")
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
                labMessage.configure(text="Bravo. Cliquez sur recommencer pour une nouvelle partie")
        if error==7:
            solution()
            labMessage.configure(text="Dommage. Cliquez sur recommencer pour une nouvelle partie")
            

############################################################################
# graphics window
############################################################################
window = tk.Tk()
window.title("Jeu du pendu")
frame=tk.Frame(window)
frame.pack(side=tk.TOP)
can = tk.Canvas(window,bg='black',height=500,width=500)
can.pack(side=tk.LEFT)
frame2=tk.Frame(window)
frame2.pack(side=tk.BOTTOM)

labMessage=tk.Label(frame,text="Choisissez une lettre")
labMessage.pack(side=tk.TOP)
#button commencer-abandonner-quitter
butStart=tk.Button(frame2,text="Recommencer",command=game)
butStart.pack(side=tk.LEFT)

butSol=tk.Button(frame2,text="Abandonner",command=solution, bg='red', fg='white')
butSol.pack(side=tk.LEFT)

butExit=tk.Button(frame2,text="Quitter",command=window.destroy, bg='blue', fg='white')
butExit.pack(side=tk.LEFT)

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
