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

    def affiche(self, mes, adv, grille):
        t   = int(mt.sqrt(np.size(grille)))
        print("-----",mes,"-----")
        print("----- J1 -----", "Endurence :", self.trt.endurance, ", Vie :", self.trt.vie, ", Points :", self.points)
        print("----- J2 -----", "Endurence :", adv.trt.endurance, ", Vie :", adv.trt.vie, ", Points :", adv.points)

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

    def joue(self, adv, grille):
        while adv.trt.vie>0 and self.trt.endurance>0:
            act = Action(self.aim.prochainCoup(self.trt, adv.trt, grille))
            act.execActDebug(self.trt, adv.trt, grille)
            self.affiche("Etat du jeu", adv, grille)

            if (adv.trt.endurance+10)<=100:
                adv.trt.endurance +=10
            else:
                adv.trt.endurance=100
                
        if adv.trt.vie==0:
            adv.trt.endurance=0
            grille[adv.trt.x, adv.trt.y] = "V"
            self.points += 1

    def nouvelleTortue(self, x, y):
        self.trt.iniTortue()
        self.trt.setPos(x, y)