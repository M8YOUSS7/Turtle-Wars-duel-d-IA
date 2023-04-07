#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""
import numpy as np;


class Tortue:
    def __init__(self,  x, y, vie, endurance):
        self.vie       = vie
        self.endurance = endurance
        self.x         = x
        self.y         = y
        
    def getPos():
        return (self.x, self.y)
    
    def monte():
        if self.y > 0:
            self.y -= 1
        
    def decends():
        self.y += 1
        
    def gauche():
        if self.x > 0:
            self.x -=1
        
    def droite():
        self.x += 1
        
class Action:
    def __init__(self, typeAct, tortue):
        self.typeAct = typeAct
        self.tortue  = tortue
        
class Joueur:
    def __init__(self, name):
        self.name = name
        
class Arene:
    def __init__(self, tailleGrille):
        self.j1     = Joueur("j1")
        self.j2     = Joueur("j2")
        self.grille = np.arange(0, tailleGrille**2)
        self.grille.reshape(tailleGrille)
        
