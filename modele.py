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

class Arme:
    def __init__(self, nom, poids):
        self.nom       = nom
        self.poids     = poids
        
        if poids<5:
            self.degat = 15
            self.charge = 2
            
        elif poids<10:
            self.degat = 25
            self.charge = 4
            
        else:
            self.degat = 35
            self.charge = 8
        
        def getDegats(self):
            return self.degat
        
        def getCharge(self):
            return self.charge
    
class Tortue:
    def __init__(self,  x, y, vie, endurance):
        self.vie       = vie
        self.endurance = endurance
        self.x         = x
        self.y         = y
        self.listArm   = []
        
    def getPos(self):
        return (self.x, self.y)
    
    def monte(self):
        end = self.chargeTotal()+10
        if (self.endurance-end)>0:
            self.x -= 1
            self.endurance -= end
            return True
        else:
            return False
        
    def descends(self):
        end = self.chargeTotal()+10
        if (self.endurance-end)>0:
            self.x += 1
            self.endurance -= end
            return True
        else:
            return False
        
    def gauche(self):
        end = self.chargeTotal()+10
        if (self.endurance-end)>0:
            self.y -= 1
            self.endurance -= end
            return True
        else:
            return False
        
    def droite(self):
        end = self.chargeTotal()+10
        if (self.endurance-end)>0:
            self.y += 1
            self.endurance -= end
            return True
        else:
            return False
        
    def tire(self, adv):
        dgt = self.degatTotal()
        end = self.chargeTotal()+10
        if self.endurance-end>0:
            if (adv.vie-dgt)>=0:
                adv.vie       -= dgt
                self.endurance -= end
            else:
                adv.vie        = 0
                self.endurance -= end
            
            return True
        else:
            return False
        
    def ajtArm(self, nom, poids):
        self.listArm.append(Arme(nom, poids))
        
    def chargeTotal(self):
        res = 0
        for arm in self.listArm:
            res += arm.charge
        return res
    
    def degatTotal(self):
        res = 0
        for arm in self.listArm:
            res += arm.degat
        return res
    
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
                jr.endurance += (2 * jr.chargeTotal()) + 10
            
        elif self.action==aim.typeAct.DESCENDS:
            jr.descends()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.monte()
                jr.endurance += (2 * jr.chargeTotal()) + 10

        elif self.action==aim.typeAct.GAUCHE:
            jr.gauche()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.droite()
                jr.endurance += (2 * jr.chargeTotal()) + 10

        elif self.action==aim.typeAct.DROITE:
            jr.droite()
            if self.swap(x, y, jr.x, jr.y, grille)==False:
                jr.gauche()
                jr.endurance += (2 * jr.chargeTotal()) + 10
            
        elif self.action==aim.typeAct.TIRE:
            jr.tire(adv)
    
    def execActDebug(self, jr, adv, grille):
        x =jr.x
        y =jr.y
        ply = grille[x, y]

        if self.action==aim.typeAct.MONTE:
            if jr.monte()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.descends()
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    print("J", ply, " impossible de MONTE")
                else:
                    print("J", ply, " MONTE : (",x,",",y,") => (",jr.x,",",jr.y,")")
            else:
                jr.endurance = 0
                
        elif self.action==aim.typeAct.DESCENDS:
            if jr.descends()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.monte()
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    print("J", ply, " impossible de DESCENDRE")
                else:
                    print("J", ply, " DESCENDS : (",x,",",y,") => (",jr.x,",",jr.y,")")
            else:
                jr.endurance = 0
                
        elif self.action==aim.typeAct.GAUCHE:
            if jr.gauche()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.droite()
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    print("J", ply, " impossible d'aller à GAUCHE")
                else:
                    print("J", ply, " GAUCHE : (",x,",",y,") => (",jr.x,",",jr.y,")")
            else:
                jr.endurance = 0
        elif self.action==aim.typeAct.DROITE:
            if jr.droite()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.gauche()
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    print("J", ply, " impossible d'aller à DROITE")
                else:
                    print("J", ply, " DROITE : (",x,",",y,") => (",jr.x,",",jr.y,")")
            else:
                jr.endurance = 0
        elif self.action==aim.typeAct.TIRE:
            if jr.tire(adv)==True:
                print("J", ply, " TIRE")
            else:
                jr.endurance = 0
                print("J", ply, " impossible de TIRE")
                

class Joueur:
    def __init__(self, name, x, y, ia):
        self.name   = name
        self.points = 0
        self.trt    = Tortue(x, y, 100, 100)
        #self.trt.ajtArm("FAMAS", 4)
        #self.trt.ajtArm("BROWING M2", 72)
        #self.trt.ajtArm("FN MAG", 13)
        #self.trt.ajtArm("AK-47", 5)
        #self.trt.ajtArm("M16", 3)
        
        if ia=="expert":
            self.aim = aim.IAExpert()
            self.trt.ajtArm("M16", 3)
            
        else:
            self.aim = aim.IA(ia)

    def joue(self, adv, grille):
        while adv.trt.vie>0 and self.trt.endurance>0:
            act = Action(self.aim.prochainCoup(self.trt, adv.trt, grille))
            act.execActDebug(self.trt, adv.trt, grille)

            if (adv.trt.endurance+10)<=100:
                adv.trt.endurance +=10
            else:
                adv.trt.endurance=100
                
        if adv.trt.vie==0:
            adv.trt.endurance=0
            grille[adv.trt.x, adv.trt.y] = "V"

                
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
        return self.j1.trt.vie==0 or self.j2.trt.vie==0
    
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