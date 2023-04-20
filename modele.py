#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""
import numpy as np;
import random;
from enum import Enum;
import aim;

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
        if self.y>0:
            self.y -= 1
            self.endurance -= 30
        
    def descends(self):
        self.y += 1
        self.endurance -= 30
        
    def gauche(self):
        if self.x > 0:
            self.x -=1
            self.endurance -= 30
        
    def droite(self):
        self.x += 1
        self.endurance -= 30

    def tire(self, trt):
        self.endurance -= 40
        for i in range(self.nbArme):
            trt.vie -= 25
    
class Action:
    def __init__(self, act):
        self.action = act

    def swap(self, x1, y1, x2, y2, grille):
        val = grille[x1, y1]
        grille[x1, y1] = grille[x2, y2]
        grille[x2, y2] = val

    def testPosVide(self, x1, x2, y1, y2, grille):
        return grille[x1:x2, y1:y2]=="V"

    def execAct(self, jr, adv, grille):
        if self.action==aim.typeAct.MONTE:
            x =jr.x
            y =jr.y
            jr.monte()
            self.swap(x, y, jr.x, jr.y, grille)
            
        elif self.action==aim.typeAct.DESCENDS:
            x =jr.x
            y =jr.y
            jr.descends()
            self.swap(x, y, jr.x, jr.y, grille)

        elif self.action==aim.typeAct.GAUCHE:
            x =jr.x
            y =jr.y
            jr.gauche()
            self.swap(x, y, jr.x, jr.y, grille)

        elif self.action==aim.typeAct.DROITE:
            x =jr.x
            y =jr.y
            jr.droite()
            self.swap(x, y, jr.x, jr.y, grille)
            
        elif self.action==aim.typeAct.TIRE:
            jr.tire(adv)
    
    def execActDebug(self, jr, adv, grille):
        if self.action==aim.typeAct.MONTE:
            x =jr.x
            y =jr.y
            jr.monte()
            self.swap(x, y, jr.x, jr.y, grille)
            print("MONTE")
            
        elif self.action==aim.typeAct.DESCENDS:
            x =jr.x
            y =jr.y
            jr.descends()
            self.swap(x, y, jr.x, jr.y, grille)
            print("DESCENDS")
            
        elif self.action==aim.typeAct.GAUCHE:
            x =jr.x
            y =jr.y
            jr.gauche()
            self.swap(x, y, jr.x, jr.y, grille)
            print("VAS A GAUCHE")

        elif self.action==aim.typeAct.DROITE:
            x =jr.x
            y =jr.y
            jr.droite()
            self.swap(x, y, jr.x, jr.y, grille)
            print("VAS A DROITE")
            
        elif self.action==aim.typeAct.TIRE:
            jr.tire(adv)
            print("TIRE")
    
class Joueur:
    def __init__(self, name, x, y, ia):
        self.name   = name
        self.points = 0
        self.trt    = Tortue(x, y, 100, 100, 1)
        
        if ia=="expert":
            self.aim = aim.IAExpert()
        else :
            self.aim = aim.IA(ia)

    def joue(self, adv, grille):
        return self.aim.prochainCoup(self.trt, adv.trt, grille)
        """while(self.trt.endurance > 1):
            coup = self.aim.prochainCoup(self.trt, adv.trt, grille)
            match coup:
                case typeAct.TIRE:
                    self.trt.tire(adv.trt)
                case typeAct.DESCENDS:
                    self.trt.descends()
"""
                
class Arene:
    def __init__(self, tailleGrille, ia1, ia2):
        self.grille                               = np.full((tailleGrille, tailleGrille), "V")
        t                                         = tailleGrille-1
        self.j1                                   = Joueur("j1", random.randint(0,t), random.randint(0,t), ia1)
        self.j2                                   = Joueur("j2", random.randint(0,t), random.randint(0,t), ia2)
        self.grille[self.j1.trt.x, self.j1.trt.y] = "1"
        self.grille[self.j2.trt.x, self.j2.trt.y] = "2"
        
        """
        for i in range(tailleGrille):
            x = random.randint(0,t)
            y = random.randint(0,t)
            if self.grille[x, y]=="V":
                self.grille[x, y] = "O"
        """
        self.tour =0
        
    def gameOver(self):
        return self.j1.trt.vie<=0 or self.j2.trt.vie<=0
    
    def winner(self):
        if self.j1.trt.vie>0:
            return 1
        elif self.j2.trt.vie>0:
            return 2
        
        return 0        
    
    def joue(self):
        while self.gameOver()==False:
            if self.tour==0:
                self.j1.joue(self.j2, self.grille)
                self.tour += 1

            elif self.tour==1:
                self.j2.joue(self.j1, self.grille)
                self.tour -= 1
                
        if self.winner()==1:
            self.grille[self.j2.trt.x, self.j2.trt.y] = "V"
        elif self.winner()==2:
            self.grille[self.j1.trt.x, self.j1.trt.y] = "V"

    def joueWithDebug(self):
        print("----- Debut de jeu -----\n")
        print(self.grille)
        print("----- J1 -----\n")
        print(self.j1.trt.endurance)
        print(self.j1.trt.vie)
        print("----- J2 -----\n")
        print(self.j2.trt.endurance)
        print(self.j2.trt.vie)

        while(self.gameOver()==False):
            if self.tour==0:
                self.j1.joue(self.j2, self.grille)
                print("----- Etat du jeu -----\n")
                print(self.grille)
                print("----- J1 -----\n")
                print(self.j1.trt.endurance)
                print(self.j1.trt.vie)
                print("----- J2 -----\n")
                print(self.j2.trt.endurance)
                print(self.j2.trt.vie)
                self.tour += 1
            elif self.tour==1:
                self.j2.joue(self.j1, self.grille)
                print("----- Etat du jeu -----\n")
                print(self.grille)
                print("----- J1 -----\n")
                print(self.j1.trt.endurance)
                print(self.j1.trt.vie)
                print("----- J2 -----\n")
                print(self.j2.trt.endurance)
                print(self.j2.trt.vie)
                self.tour -= 1

        winner = self.winner()
        if winner==1:
            self.grille[self.j2.trt.x, self.j2.trt.y] = "V"
        elif winner==2:
            self.grille[self.j1.trt.x, self.j1.trt.y] = "V"
        
        print("----- Fin de jeu -----\n")
        print(self.grille)
        print("----- J1 -----\n")
        print(self.j1.trt.endurance)
        print(self.j1.trt.vie)
        print("----- J2 -----\n")
        print(self.j2.trt.endurance)
        print(self.j2.trt.vie)
        print("--- Big Winner - ",winner,"---")
        
    def joueDebugIA(self):
        print("----- Debut de jeu -----\n")
        print(self.grille)
        print("----- J1 -----")
        action = Action(self.j1.joue(self.j2, self.grille))
        action.execActDebug(self.j1.trt, self.j2.trt, self.grille)
        print(self.grille)