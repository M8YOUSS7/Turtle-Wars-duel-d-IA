#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:58:57 2023
        self.id = grille[jr.x, jr.y]
        xTest = self.trt.x - adv.trt.x
        yTest = self.trt.y - adv.trt.y
        
        if self.enLigneDeMire(adv)==True:
            ""if xTest==0:
                if (yTest<0 and grille[self.trt.x, (adv.trt.y+1):(self.trt.y)]=="V") or (yTest>0 and grille[self.trt.x, (self.trt.y+1):(adv.trt.y)]=="V"):
                    self.trt.tire(adv.trt)
            elif yTest==0:
                if (xTest<0 and grille[(adv.trt.x+1):(self.trt.x), self.trt.y]=="V") or (yTest>0 and grille[(self.trt.x+1):(adv.trt.x), self.trt.y]=="V"):
                    self.trt.tire(adv.trt)
            else:""
            self.trt.tire(adv.trt)
        else:
            
            if xTest<0 or yTest<0:
                if grille[self.trt.x+1:adv.trt.x , self.trt.y]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.x = adv.trt.x
                    grille[self.trt.x, self.trt.y] = id
                    
                elif grille[self.trt.x , self.trt.y+1:adv.trt.y]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.y = adv.trt.y
                    grille[self.trt.x, self.trt.y] = id
                    
                else:
                    dTest = random.randint(0,1)
                    
                    if dTest==0:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.monte()
                        grille[self.trt.x, self.trt.y] = id
                    else:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.droite()
                        grille[self.trt.x, self.trt.y] = id
                    
            elif xTest>0 or yTest>0:
                if grille[adv.trt.x:self.trt.x-1 , self.trt.y]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.x = adv.trt.x
                    grille[self.trt.x, self.trt.y] = id
                    
                elif grille[self.trt.x , adv.trt.y:self.trt.y-1]=="V":
                    id = grille[self.trt.x, self.trt.y]
                    grille[self.trt.x, self.trt.y] = "V"
                    self.trt.y = adv.trt.y
                    grille[self.trt.x, self.trt.y] = id
                
                else:
                    dTest = random.randint(0,1)
                    
                    if dTest==0:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.descends()
                        grille[self.trt.x, self.trt.y] = id
                    else:
                        id = grille[self.trt.x, self.trt.y]
                        grille[self.trt.x, self.trt.y] = "V"
                        self.trt.gauche()
                        grille[self.trt.x, self.trt.y] = id
        

@author: yyouss
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
            
            elif yTest>1 and self.colVide(jr.x, jr.y, adv.y, grille)==True:
                return typeAct.TIRE
            
            elif yTest<-1 and self.colVide(jr.x, adv.y, jr.y, grille)==True:
                return typeAct.TIRE

            else:
                dTest = random.randint(1,2)
                
                if dTest==1:
                    return typeAct.GAUCHE
                elif dTest==2:
                    return typeAct.DROITE
            
            
            
        elif yTest==0:
            if xTest==-1 or xTest==1:
                return typeAct.TIRE
            
            elif xTest>1 and self.ligVide(jr.x, adv.x, jr.y, grille):
                return typeAct.TIRE
            
            elif xTest<-1 and self.ligVide(adv.x, jr.x, jr.y, grille):
                return typeAct.TIRE

            else:
                dTest = random.randint(1,2)
                
                if dTest==1:
                    return typeAct.MONTE
                elif dTest==2:
                    return typeAct.DESCENDS
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
