#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

from tortue import *
from aim import *

class Joueur:
    def __init__(self, name, x, y, ia):
        self.name   = name
        self.points = 0
        self.trt    = Tortue(x, y)
        #self.trt.ajtArm("FAMAS", 4)
        #self.trt.ajtArm("BROWING M2", 72)
        #self.trt.ajtArm("FN MAG", 13)
        #self.trt.ajtArm("AK-47", 5)
        #self.trt.ajtArm("M16", 3)
        
        if ia=="expert":
            self.aim = IAExpert()
            self.trt.ajtArm("M16", 3)
            
        else:
            self.aim = IA(ia)

        self.partieCourante = []

    def affiche(self, mes, adv, grille, det=True):
        t   = int(mt.sqrt(np.size(grille)))
        jr  = grille[self.trt.x, self.trt.y]
        ad  = grille[adv.trt.x, adv.trt.y]

        print("-----",mes,"-----")

        if det==True:
            print("----- J", jr," -----", "Endurence :", self.trt.endurance, ", Vie :", self.trt.vie, ", Points :", self.points, sep="")
            print("----- J", ad," -----", "Endurence :", adv.trt.endurance, ", Vie :", adv.trt.vie, ", Points :", adv.points, sep="")

        for j in range(t):
            print ("--", end="")
        print("----")

        for i in range(t):
            print("| ", end="")
            for j in range(t):
                if grille[i,j]!="V":
                    print(grille[i,j], " ", sep="", end="")
                else:
                    print("  ", end="")
            print(" |", end="")
            print("")
        
        for j in range(t):
            print ("--", end="")
        print("----")

    def save(self, grille, act):
        grille.reshape(-1)
        res =[self.trt.vie, self.trt.endurance, act.value]
        self.partieCourante.append(np.append(grille, res))

    def joue(self, adv, grille):
        while adv.trt.vie>0 and self.trt.endurance>0:
            act                             = self.aim.prochainCoup(self.trt, adv.trt, grille)
            forSave                         = np.copy(grille)
            forSave[self.trt.x, self.trt.y] = "J"
            forSave[adv.trt.x, adv.trt.y]   = "A"
            self.save(forSave, act)
            Action(act).execAct(self.trt, adv.trt, grille)

            if (adv.trt.endurance+10)<100:
                adv.trt.endurance +=10
            else:
                adv.trt.endurance=100
                
        if adv.trt.vie==0:
            adv.trt.endurance=0
            grille[adv.trt.x, adv.trt.y] = "V"
            self.points += 1

    def joueDebug(self, adv, grille):
        while adv.trt.vie>0 and self.trt.endurance>0:
            act                             = self.aim.prochainCoup(self.trt, adv.trt, grille)
            forSave                         = np.copy(grille)
            forSave[self.trt.x, self.trt.y] = "J"
            forSave[adv.trt.x, adv.trt.y]   = "A"
            self.save(forSave, act)
            Action(act).execActDebug(self.trt, adv.trt, grille)

            if (adv.trt.endurance+10)<100:
                adv.trt.endurance +=10
            else:
                adv.trt.endurance=100
                
            self.affiche("Etat du jeu", adv, grille)

        if adv.trt.vie==0:
            adv.trt.endurance=0
            grille[adv.trt.x, adv.trt.y] = "V"
            self.points += 1

    def nouvelleTortue(self, x, y):
        self.trt.iniTortue()
        self.trt.setPos(x, y)
        self.partieCourante = []