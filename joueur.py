#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

from tortue import *
from aim import *

class Joueur:
    def __init__(self, name, x, y, ia, fileName =''):
        self.name   = name
        self.points = 0
        self.trt    = Tortue(x, y)
        
        if ia.lower()=="expert":
            self.aim = IAExpert()
            self.trt.ajtArm("AK-47", 5)
        elif ia.lower()=="perceptron":
            self.aim = IAPerceptron(fileName)
            self.trt.ajtArm("AK-47", 5)
        elif ia.lower()=="armelegere":
            self.aim = IANaiveArmeLegere()
            self.trt.ajtArm("M16", 3)
        elif ia.lower()=="armelourde":
            self.aim = IANaiveArmeLourde()
            self.trt.ajtArm("FN MAG", 13)
        elif ia.lower()=="manuelle":
            self.aim    = IAManelle()
            arm         = 0

            while(arm!=1 and arm!=2 and arm!=2 and arm!=3 and arm!=4 and arm!=5):
                print('Les armes disponibles sont ', '1 : BROWING M2, Categorie 3.', '2 : FN MAG, Categorie 3.', '3 : AK-47, Categorie 2.', '4 : FAMAS, Categorie 1.', '5 : M16, Categorie 1.',  '**Par defaut le AK-47 vous es affecté.**', sep='\n')
                arm = int(input('Veillez saisir le code de l\'arme que vous voulez :'))
                
                if arm==1:
                    self.trt.ajtArm("BROWING M2", 72)
                elif arm==2:
                    self.trt.ajtArm("FN MAG", 13)
                elif arm==3:
                    self.trt.ajtArm("AK-47", 5)
                elif arm==4:
                    self.trt.ajtArm("FAMAS", 4)
                else:
                    self.trt.ajtArm("AK-47", 5)
                
        else:
            self.aim = IA(ia)

        self.partieCourante = []

    def affiche(self, mes, adv, grille, det=True):
        t   = grille[0].size
        jr  = int(grille[self.trt.x, self.trt.y])
        ad  = int(grille[adv.trt.x, adv.trt.y])

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
                if grille[i,j]==0:
                    print("  ", end="")
                elif grille[i,j]==3:
                    print("* ", end="")
                else:
                    print(int(grille[i,j]), " ", sep="", end="")
                    
            print(" |", end="")
            print("")
        
        for j in range(t):
            print ("--", end="")
        print("----")

    def save(self, grille, act):
        grille.reshape(-1)
        res =[self.trt.endurance, self.trt.vie, act.value]
        if res not in self.partieCourante:
            self.partieCourante.append(np.append(grille, res))

    def joue(self, adv, grille):
        while adv.trt.vie>0 and self.trt.endurance>0:
            act                             = self.aim.prochainCoup(self.trt, adv.trt, grille)
            forSave                         = np.copy(grille)
            forSave[self.trt.x, self.trt.y] = 1
            forSave[adv.trt.x, adv.trt.y]   = 2
            self.save(forSave, act)
            Action(act).execAct(self.trt, adv.trt, grille)

            if (adv.trt.endurance+20)<100:
                adv.trt.endurance +=20
            else:
                adv.trt.endurance=100
                
    def joueDebug(self, adv, grille):
        while adv.trt.vie>0 and self.trt.endurance>0:
            act                             = self.aim.prochainCoup(self.trt, adv.trt, grille)
            forSave                         = np.copy(grille)
            forSave[self.trt.x, self.trt.y] = 1
            forSave[adv.trt.x, adv.trt.y]   = 2
            self.save(forSave, act)
            Action(act).execActDebug(self.trt, adv.trt, grille)

            if (adv.trt.endurance+20)<100:
                adv.trt.endurance +=20
            else:
                adv.trt.endurance=100
                
            self.affiche("Etat du jeu", adv, grille)

    def nouvelleTortue(self, x, y):
        self.trt.iniTortue(x, y)
        self.partieCourante = []