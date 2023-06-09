#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

from joueur import *
import random;
                
class Arene:
    def __init__(self, tailleGrille, ia1, ia2, fileName =''):
        t                                         = tailleGrille-1
        self.j1                                   = Joueur("j1", random.randint(0,t), random.randint(0,t), ia1, fileName)
        self.j2                                   = Joueur("j2", random.randint(0,t), random.randint(0,t), ia2, fileName)
        self.tailleGrille                         = tailleGrille
        self.tour                                 = random.randint(0, 1)
        self.gammes                               = []

    def parcours(self, x, y, dejaVu):
        if x<0 or x>=self.tailleGrille or y<0 or y>=self.tailleGrille or self.grille[x][y]==3 or (x,y) in dejaVu:
            return []
        else:
            dejaVu.append((x, y))
            
            for z in self.parcours(x+1, y, dejaVu):
                if z not in dejaVu:
                    dejaVu.append(z)
            
            for z in self.parcours(x-1, y, dejaVu):
                if z not in dejaVu:
                    dejaVu.append(z)

            for z in self.parcours(x, y+1, dejaVu):
                if z not in dejaVu:
                    dejaVu.append(z)
                
            for z in self.parcours(x, y-1, dejaVu):
                if z not in dejaVu:
                    dejaVu.append(z)

            return dejaVu


    def nouvellePartie(self):
        t                                         = self.tailleGrille-1
        self.grille                               = np.zeros((self.tailleGrille, self.tailleGrille))
        self.j1.nouvelleTortue(random.randint(0,t), random.randint(0,t))
        self.j2.nouvelleTortue(random.randint(0,t), random.randint(0,t))
        
        self.grille[self.j1.trt.x, self.j1.trt.y]  = 1
        
        while self.grille[self.j2.trt.x, self.j2.trt.y] != 0:
            self.j2.trt.setPos(random.randint(0,t), random.randint(0,t))
        self.grille[self.j2.trt.x, self.j2.trt.y]  = 2
        
        for i in range(self.tailleGrille):
            x = random.randint(0, t)
            y = random.randint(0, t)

            while self.grille[x, y]!=0:
                x = random.randint(0, t)
                y = random.randint(0, t)
            self.grille[x, y] = 3
        
        while self.grille[x, y]==3:
                x = random.randint(0, t)
                y = random.randint(0, t)

        while len(self.parcours(x, y, [])) != (self.grille.size - self.tailleGrille):
            self.nouvellePartie()
        
    def gameOver(self):
        return self.j1.trt.vie==0 or self.j2.trt.vie==0
    
    def winner(self):
        if self.j1.trt.vie==0:
            self.j1.trt.endurance=0
            self.grille[self.j1.trt.x, self.j1.trt.y] = 0
            self.j2.points += 1
            return 2
        elif self.j2.trt.vie==0:
            self.j2.trt.endurance=0
            self.grille[self.j2.trt.x, self.j2.trt.y] = 0
            self.j1.points += 1
            return 1

    def joue(self):
        while(self.gameOver()==False):
            if self.tour==0:
                self.j1.joue(self.j2, self.grille)
                self.tour += 1

            else:
                self.j2.joue(self.j1, self.grille)
                self.tour -= 1

        self.winner()

    def joueDebug(self):
        self.j1.affiche("Debut de jeu", self.j2, self.grille, False)

        while(self.gameOver()==False):
            if self.tour==0:
                self.j1.joueDebug(self.j2, self.grille)
                self.tour += 1

            else:
                self.j2.joueDebug(self.j1, self.grille)
                self.tour -= 1

        winner = self.winner()

        print("--- Fin de jeu --- Big Winner - ",winner,"---")
    
    def save(self):
        if self.j2.trt.vie==0:
            for e in self.j1.partieCourante:
                self.gammes.append(e)

        elif self.j1.trt.vie==0:
            for e in self.j2.partieCourante:
                self.gammes.append(e)

    def getGammes(self):
        return np.array(self.gammes)