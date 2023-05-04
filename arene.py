#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

from joueur import *
import random;
                
class Arene:
    def __init__(self, tailleGrille, ia1, ia2):
        t                                         = tailleGrille-1
        self.j1                                   = Joueur("j1", random.randint(0,t), random.randint(0,t), ia1)
        self.j2                                   = Joueur("j2", random.randint(0,t), random.randint(0,t), ia2)
        self.tailleGrille                         = tailleGrille
        self.tour = random.randint(0, 1)
        
    def nouvellePartie(self):
        t                                         = self.tailleGrille-1
        self.grille                               = np.full((self.tailleGrille, self.tailleGrille), "V")
        self.j1.nouvelleTortue(random.randint(0,t), random.randint(0,t))
        self.j2.nouvelleTortue(random.randint(0,t), random.randint(0,t))
        
        self.grille[self.j1.trt.x, self.j1.trt.y] = "1"
        
        while self.grille[self.j2.trt.x, self.j2.trt.y] != "V":
            self.j2.trt.setPos(random.randint(0,t), random.randint(0,t))
        self.grille[self.j2.trt.x, self.j2.trt.y] = "2"
        
        for i in range(self.tailleGrille):
            x = random.randint(0, t)
            y = random.randint(0, t)

            while self.grille[x, y]!="V":
                x = random.randint(0, t)
                y = random.randint(0, t)
            self.grille[x, y] = "*"
        
    def gameOver(self):
        return self.j1.trt.vie==0 or self.j2.trt.vie==0
    
    def winner(self):
        if self.j1.trt.vie>0:
            return 1
        elif self.j2.trt.vie>0:
            return 2
        
        return 0        
    
    def affiche(self, mes):
        t   = int(mt.sqrt(np.size(self.grille)))
        print("-----",mes,"-----")
        print("----- J1 -----", "Endurence :", self.j1.trt.endurance, ", Vie :", self.j1.trt.vie)
        print("----- J2 -----", "Endurence :", self.j2.trt.endurance, ", Vie :", self.j2.trt.vie)

        for j in range(t):
            print ("--", end="")
        print("----")

        for i in range(t):
            print("| ", end="")
            for j in range(t):
                if self.grille[i,j]!="V":
                    print(self.grille[i,j], " ", sep="", end="")
                else:
                    print("  ", end="")
            print(" |", end="")
            print("")
        
        for j in range(t):
            print ("--", end="")
        print("----")



    def joue(self):
        while(self.gameOver()==False):
            if self.tour==0:
                self.j1.joue(self.j2, self.grille)
                self.tour += 1

            elif self.tour==1:
                self.j2.joue(self.j1, self.grille)
                self.tour -= 1

            elif self.tour==1:
                self.j2.joue(self.j1, self.grille)
                self.tour -= 1

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
        
        print("--- Fin de jeu --- Big Winner - ",winner,"---")