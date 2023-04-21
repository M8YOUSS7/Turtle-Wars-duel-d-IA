#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:58:57 2023
@author: yyouss

dTest = random.randint(1,5)
            
            if dTest==1:
                return typeAct.MONTE
            elif dTest==2:
                return typeAct.DESCENDS
            elif dTest==3:
                return typeAct.GAUCHE
            elif dTest==4:
                return typeAct.DROITE
            else:
                if xTest<0:
                    return typeAct.MONTE
                elif yTest<0:
                    return typeAct.GAUCHE
                elif xTest>0:
                    return typeAct.DESCENDS
                elif yTest>0:
                    return typeAct.DROITE
"""
import random;
from enum import Enum;

class typeAct(Enum):
    MONTE    = 1
    DESCENDS = 2
    GAUCHE   = 3
    DROITE   = 4
    TIRE     = 5


class IA:
    def __init__(self, name):
        self.name = name
    
    def prochainCoup(self, jr, adv, grille):
        return
    
class IAExpert(IA):
    def __init__(self):
        IA.__init__(self, "expert")
    
    def ligVide(self, x1, x2, y, grille):
        return (grille[x1:x2, y]=="V").all()

    def colVide(self, x, y1, y2, grille):
        return (grille[x, y1:y2]=="V").all()

    def prochainCoup(self, jr, adv, grille):
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        
        if xTest==0:
            if yTest==-1 or yTest==1:
                return typeAct.TIRE
            
            elif yTest>1 and self.colVide(jr.x, adv.y+1, jr.y, grille):
                return typeAct.TIRE
            
            elif yTest>1 and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                dTest = random.randint(1,3)
                
                if dTest==1:
                    return typeAct.MONTE
                elif dTest==2:
                    return typeAct.DESCENDS
                else:
                   return typeAct.GAUCHE 
            
            elif yTest<-1 and self.colVide(jr.x, jr.y+1, adv.y, grille):
                return typeAct.TIRE

            elif yTest<-1 and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                dTest = random.randint(1,3)
                
                if dTest==1:
                    return typeAct.MONTE
                elif dTest==2:
                    return typeAct.DESCENDS
                else:
                   return typeAct.DROITE

            else:
                dTest = random.randint(1,4)
                
                if dTest==1:
                    return typeAct.MONTE
                elif dTest==2:
                    return typeAct.DESCENDS
                elif dTest==3:
                    return typeAct.GAUCHE
                else:
                   return typeAct.DROITE
            
        elif yTest==0:
            if xTest==-1 or xTest==1:
                return typeAct.TIRE
            
            elif xTest>1 and self.ligVide(adv.x+1, jr.x, jr.y, grille):
                return typeAct.TIRE
            
            elif xTest>1 and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                dTest = random.randint(1,3)
                
                if dTest==1:
                    return typeAct.DROITE
                elif dTest==2:
                    return typeAct.GAUCHE
                else:
                    return typeAct.MONTE
            
            elif xTest<-1 and self.ligVide(jr.x+1, adv.x, jr.y, grille):
                return typeAct.TIRE

            elif xTest<-1 and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                dTest = random.randint(1,3)
                
                if dTest==1:
                    return typeAct.DROITE
                elif dTest==2:
                    return typeAct.GAUCHE
                else:
                    return typeAct.DESCENDS

            else:
                dTest = random.randint(1,3)
                
                if dTest==1:
                    return typeAct.MONTE
                elif dTest==2:
                    return typeAct.DESCENDS
                elif dTest==3:
                    return typeAct.GAUCHE
                else:
                   return typeAct.DROITE
        else:
            if xTest<0:
                if yTest<0:
                    dTest = random.randint(1,2)
                
                    if dTest==1:
                        return typeAct.DROITE
                    elif dTest==2:
                        return typeAct.DESCENDS
                        
                else:
                    dTest = random.randint(1,2)
                
                    if dTest==1:
                        return typeAct.GAUCHE
                    elif dTest==2:
                        return typeAct.DESCENDS
                
            elif yTest<0 and xTest>0:
                dTest = random.randint(1,2)
            
                if dTest==1:
                    return typeAct.DROITE
                elif dTest==2:
                    return typeAct.MONTE
                    
                
            elif xTest>0 and yTest>0:
                dTest = random.randint(1,2)
            
                if dTest==1:
                    return typeAct.GAUCHE
                elif dTest==2:
                    return typeAct.MONTE
        
