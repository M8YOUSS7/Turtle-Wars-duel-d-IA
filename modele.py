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
import math as mt;

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
        self.x -= 1
        self.endurance -= 30
        
    def descends(self):
        self.x += 1
        self.endurance -= 30
        
    def gauche(self):
        self.y -= 1
        self.endurance -= 30
        
    def droite(self):
        self.y += 1
        self.endurance -= 30

    def tire(self, trt):
        for i in range(self.nbArme):
            trt.vie -= 25
        self.endurance -= 40
    
class Action:
    def __init__(self, act):
        self.action = act

    def swap(self, x1, y1, x2, y2, grille):
        t   = mt.sqrt(np.size(grille))
        res = False
        if (x2>=0) and (x2<t) and (y2>=0) and (y2<t) and (grille[x2, y2]=="V"):
            val = grille[x1, y1]
            grille[x1, y1] = "V"
            grille[x2, y2] = val
            res = True
        
        return res

    def execAct(self, jr, adv, grille):
        x =jr.x
        y =jr.y
        
        if self.action==aim.typeAct.MONTE:
            jr.monte()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.descends()
                jr.endurance += 50
            
        elif self.action==aim.typeAct.DESCENDS:
            jr.descends()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.monte()
                jr.endurance += 50

        elif self.action==aim.typeAct.GAUCHE:
            jr.gauche()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.droite()
                jr.endurance += 50

        elif self.action==aim.typeAct.DROITE:
            jr.droite()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.gauche()
                jr.endurance += 50
            
        elif self.action==aim.typeAct.TIRE:
            jr.tire(adv)
    
    def execActDebug(self, jr, adv, grille):
        x =jr.x
        y =jr.y
        ply = grille[x, y]

        if self.action==aim.typeAct.MONTE:    
            jr.monte()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.descends()
                jr.endurance += 50
            
            print("J", ply, " MONTE : (",x,",",y,") => (",jr.x,",",jr.y,")")
            
        elif self.action==aim.typeAct.DESCENDS:
            jr.descends()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.monte()
                jr.endurance += 50

            print("J", ply, " DESCENDS : (",x,",",y,") => (",jr.x,",",jr.y,")")
            
        elif self.action==aim.typeAct.GAUCHE:
            jr.gauche()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.droite()
                jr.endurance += 50

            print("J", ply, " GAUCHE : (",x,",",y,") => (",jr.x,",",jr.y,")")

        elif self.action==aim.typeAct.DROITE:
            jr.droite()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.gauche()
                jr.endurance += 50

            print("J", ply, " DROITE : (",x,",",y,") => (",jr.x,",",jr.y,")")
            
        elif self.action==aim.typeAct.TIRE:
            jr.tire(adv)
            print("J", ply, " TIRE")
    
class Joueur:
    def __init__(self, name, x, y, ia):
        self.name   = name
        self.points = 0
        self.trt    = Tortue(x, y, 100, 100, 1)
        
        if ia=="expert":
            self.aim = aim.IAExpert()
        else:
            self.aim = aim.IA(ia)

    def joue(self, adv, grille):
        while self.trt.endurance>0:
            act = Action(self.aim.prochainCoup(self.trt, adv.trt, grille))
            act.execActDebug(self.trt, adv.trt, grille)

            if (adv.trt.endurance+40)<100:
                adv.trt.endurance +=40
            else:
                adv.endurance=100

                
class Arene:
    def __init__(self, tailleGrille, ia1, ia2):
        self.grille                               = np.full((tailleGrille, tailleGrille), "V")
        t                                         = tailleGrille-1
        self.j1                                   = Joueur("j1", random.randint(0,t), random.randint(0,t), ia1)
        self.j2                                   = Joueur("j2", random.randint(0,t), random.randint(0,t), ia2)
        self.grille[self.j1.trt.x, self.j1.trt.y] = "1"
        self.grille[self.j2.trt.x, self.j2.trt.y] = "2"
        
        
        for i in range(tailleGrille):
            x = random.randint(0,t)
            y = random.randint(0,t)
            if self.grille[x, y]=="V":
                self.grille[x, y] = "O"
        
        self.tour =0
        
    def gameOver(self):
        return self.j1.trt.vie<=0 or self.j2.trt.vie<=0
    
    def winner(self):
        if self.j1.trt.vie>0:
            return 1
        elif self.j2.trt.vie>0:
            return 2
        
        return 0        
    
    def affiche(self, mes):
        print("-----",mes,"-----")
        print(self.grille)

        print("----- J1 -----")
        print("Endurence :", self.j1.trt.endurance, ", Vie :", self.j1.trt.vie)
        
        print("----- J2 -----")
        print("Endurence :", self.j2.trt.endurance, ", Vie :", self.j2.trt.vie)


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
        self.affiche("Debut de jeu")

        while(self.gameOver()==False):
            if self.tour==0:
                self.j1.joue(self.j2, self.grille)
                self.affiche("Etat du jeu")
                self.tour += 1

            elif self.tour==1:
                self.j2.joue(self.j1, self.grille)
                self.affiche("Etat du jeu")
                self.tour -= 1

        winner = self.winner()
        if winner==1:
            self.grille[self.j2.trt.x, self.j2.trt.y] = "V"
        elif winner==2:
            self.grille[self.j1.trt.x, self.j1.trt.y] = "V"
        
        print("--- Fin de jeu --- Big Winner - ",winner,"---")