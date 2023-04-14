#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""
import numpy as np;
import random;
from enum import Enum;

Directions=Enum("Directions", ["HAUT", "BAS", "GAUCHE", "DROITE"])

class Tortue:
    def __init__(self,  x, y, vie, endurance, nbArme):
        self.vie       = vie
        self.endurance = endurance
        self.x         = x
        self.y         = y
        self.nbArme    = nbArme
        self.listArm   = []
        
    def getPos(self):
        return (self.x, self.y)
    
    def monte(self):
        if self.y > 0:
            self.y -= 1
        
    def descends(self):
        self.y += 1
        
    def gauche(self):
        if self.x > 0:
            self.x -=1
        
    def droite(self):
        self.x += 1

    def tire(self, trt):
        for i in range(self.nbArme):
            trt.vie -= 10
        
class typeAct(Enum):
    MONTE    = 1
    DESCENDS = 2
    GAUCHE   = 3
    DROITE   = 4
    SAUTE    = 5
    TIRE     = 6
    
class Action:
    def __init__(self, act):
        self.action = act

    def execAct(self, trt):
        if self.action==typeAct.MONTE:
            trt.monte()
            trt.endurance -= 1
        elif self.action==typeAct.DESCENDS:
            trt.descends()
            trt.endurance -= 1
        elif self.action==typeAct.GAUCHE:
            trt.gauche()
            trt.endurance -= 1
        elif self.action==typeAct.DROITE:
            trt.droite()
            trt.endurance -= 1
        elif self.action==typeAct.SAUTE:
            trt.endurance -= 2
        elif self.action==typeAct.TIRE:
            trt.endurance -= 2

class Joueur:
    def __init__(self, name, x, y):
        self.name   = name
        self.points = 0
        self.trt    = Tortue(x, y, 100, 100, 1)

    def enLigneDeMire(self, adv):
        return self.trt.x==adv.trt.x or self.trt.y==adv.trt.y

    def joue(self, adv, grille):
        if self.enLigneDeMire(adv)==True:
            self.trt.tire(adv.trt)

        else:
            xTest = self.trt.x - adv.trt.x
            yTest = self.trt.y - adv.trt.y
            
            if xTest<0 or yTest<0:
                if grille[self.trt.x+1:adv.trt.x , self.trt.y]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.x = adv.trt.x
                    grille[self.trt.x, self.trt.y] = id
                    
                elif grille[self.trt.x , self.trt.y+1:adv.trt.y]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.y = adv.trt.y
                    grille[self.trt.x, self.trt.y] = id
                    
                else:
                    dTest = random.randint(0,1)
                    
                    if dTest==0:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.monte()
                        grille[self.trt.x, self.trt.y] = id
                    else:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.droite()
                        grille[self.trt.x, self.trt.y] = id
                    
            elif xTest>0 or yTest>0:
                if grille[adv.trt.x:self.trt.x-1 , self.trt.y]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.x = adv.trt.x
                    grille[self.trt.x, self.trt.y] = id
                    
                elif grille[self.trt.x , adv.trt.y:self.trt.y-1]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.y = adv.trt.y
                    grille[self.trt.x, self.trt.y] = id
                
                else:
                    dTest = random.randint(0,1)
                    
                    if dTest==0:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.descends()
                        grille[self.trt.x, self.trt.y] = id
                    else:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.gauche()
                        grille[self.trt.x, self.trt.y] = id
                        
class Arene:
    def __init__(self, tailleGrille):
        self.grille                               = np.full((tailleGrille, tailleGrille), "V")
        t                                         = tailleGrille-1
        self.j1                                   = Joueur("j1", random.randint(0,t), random.randint(0,t))
        self.j2                                   = Joueur("j2", random.randint(0,t), random.randint(0,t))
        self.grille[self.j1.trt.x, self.j1.trt.y] = "1"
        self.grille[self.j2.trt.x, self.j2.trt.y] = "2"
        
        
        #for i in range(tailleGrille):
           # x = random.randint(0,t)
          #  y = random.randint(0,t)
         #   if self.grille[x, y]=="V":
        #        self.grille[x, y] = "O"
        
        self.tour =0
        
    def gameOver(self):
        return self.j1.trt.vie<=0 or self.j2.trt.vie<=0
    
    def winner(self):
        if self.j1.trt.vie>0:
            return 1
        elif self.j2.trt.vie>0:
            return 2
        else:
            return 0
    
    def joue(self):
        while(self.gameOver()==False):
            if self.tour==0:
                self.j1.joue(self.j2, self.grille)
                print("J",self.tour+1,"\n", self.grille)
                self.tour += 1
            elif self.tour==1:
                self.j2.joue(self.j1, self.grille)
                print("J",self.tour+1,"\n", self.grille)
                self.tour -= 1
                
        if self.winner()==1:
            self.grille[self.j2.trt.x, self.j2.trt.y] = "V"
        elif self.winner()==2:
            self.grille[self.j1.trt.x, self.j1.trt.y] = "V"
            