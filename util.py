# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint
def randomNumber():
    num = randint(1, 100)
    print("Debug Log %d"%num)
    return num
    
def game(user,comp):
    #comp = randomNumber()
    #user = int(input("Guess the number"))
    flag = False
    while(flag!=True):
        if comp < user:
            print("Sorry!! Lower Your Guess")
            user = int(input("Guess the number"))
        elif comp > user:
            print("Sorry!! Higher Your Guess")
            user = int(input("Guess the number"))
        else:
            print("Eureka!!!!")
            flag=True
