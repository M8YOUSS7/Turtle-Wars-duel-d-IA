#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

from arme import *

class Tortue:
    def __init__(self,  x, y):
        self.vie       = 100
        self.endurance = 100
        self.x         = x
        self.y         = y
        self.listArm   = []
        
    def getPos(self):
        return self.x, self.y

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def iniTortue(self, x, y):
        self.x =x
        self.y =y
        self.vie = 100
        self.endurance = 100
     
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
        if (self.endurance-end)>0:
            if (adv.vie-dgt)>0:
                adv.vie       -= dgt
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