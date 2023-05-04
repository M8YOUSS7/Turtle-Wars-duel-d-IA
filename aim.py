#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:58:57 2023
@author: yyouss

    --> Faut-il verifer si le coup es jouable avant de transmettre ?

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
from action import *

class IA:
    def __init__(self, name):
        self.name = name
    
    def ligVide(self, x1, x2, y, grille):
        return (grille[x1:x2, y]=="V").all()

    def colVide(self, x, y1, y2, grille):
        return (grille[x, y1:y2]=="V").all()

    def deplacements(self, x, y, grille):
        res = []
        t   = mt.sqrt(np.size(grille))

        if x-1 >=0 and grille[x-1,y] == "V":
            res.append(typeAct.MONTE)
        
        if x+1 <t and grille[x+1,y] == "V":
            res.append(typeAct.DESCENDS)
        
        if y-1 >=0 and grille[x,y-1] == "V":
            res.append(typeAct.GAUCHE)
        
        if y+1 <t and grille[x,y+1] == "V":
            res.append(typeAct.DROITE)

        return res

    def prochainCoup(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)

        return typeAct.AUTRE
    
class IAExpert(IA):
    def __init__(self):
        IA.__init__(self, "expert")


    def sapprocher(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        
        if len(pTest)>0:
            if xTest==0:
                if yTest>=1 and self.colVide(jr.x, adv.y+1, jr.y, grille):
                    return typeAct.TIRE
                
                elif yTest>1 and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==1:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        if typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                
                elif yTest<=-1 and self.colVide(jr.x, jr.y+1, adv.y, grille):
                    return typeAct.TIRE

                elif yTest<-1 and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    dTest = random.randint(1,3)
                    
                    if dTest==1:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]

                else:
                    return pTest[random.randint(0,len(pTest)-1)]
                
            elif yTest==0:
                if xTest>=1 and self.ligVide(adv.x+1, jr.x, jr.y, grille):
                    return typeAct.TIRE
                
                elif xTest>1 and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    dTest = random.randint(1,3)
                    
                    if dTest==1:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                
                elif xTest<=-1 and self.ligVide(jr.x+1, adv.x, jr.y, grille):
                    return typeAct.TIRE

                elif xTest<-1 and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    dTest = random.randint(1,3)
                    
                    if dTest==1:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]

                else:
                    return pTest[random.randint(0,len(pTest)-1)]
            else:
                if xTest<0:
                    if yTest<0:
                        dTest = random.randint(1,2)
                    
                        if dTest==1:
                            if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                        elif dTest==2:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                            
                    else:
                        dTest = random.randint(1,2)
                    
                        if dTest==1:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                        elif dTest==2:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                    
                elif yTest<0 and xTest>0:
                    dTest = random.randint(1,2)
                
                    if dTest==1:
                        if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                        
                elif xTest>0 and yTest>0:
                    dTest = random.randint(1,2)
                
                    if dTest==1:
                        if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
        else:
            return typeAct.AUTRE

    def seloigner(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        
        if len(pTest)>0:
            if xTest==0:
                if yTest>=1 and self.colVide(jr.x, adv.y+1, jr.y, grille):
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        if dTest==0 and typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                
                elif yTest>=1 and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        if dTest==0 and typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]

                    else:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                
                elif yTest<=-1 and self.colVide(jr.x, jr.y+1, adv.y, grille):
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        if dTest==0 and typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]

                elif yTest<=-1 and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        if dTest==0 and typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                
            elif yTest==0:
                if xTest>=1 and self.ligVide(adv.x+1, jr.x, jr.y, grille):
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        if dTest==0 and typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        if dTest==0 and typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                
                elif xTest>=1 and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        if dTest==0 and typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        if dTest==0 and typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                
                elif xTest<=-1 and self.ligVide(jr.x+1, adv.x, jr.y, grille):
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        if dTest==0 and typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        if dTest==0 and typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]

                elif xTest<=-1 and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    dTest = random.randint(0,9)
                    
                    if dTest==1:
                        dTest = random.randint(0,1)
                        if dTest==1 and typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        if dTest==0 and typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    else:
                        if dTest==0 and typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]

            else:
                if xTest<0:
                    if yTest<0:
                        dTest = random.randint(1,2)
                    
                        if dTest==1:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                        elif dTest==2:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                            
                    else:
                        dTest = random.randint(1,2)
                    
                        if dTest==1:
                            if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                        elif dTest==2:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return pTest[random.randint(0,len(pTest)-1)]
                    
                elif yTest<0 and xTest>0:
                    dTest = random.randint(1,2)
                
                    if dTest==1:
                        if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                        
                elif xTest>0 and yTest>0:
                    dTest = random.randint(1,2)
                
                    if dTest==1:
                        if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
                    elif dTest==2:
                        if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                        else:
                            return pTest[random.randint(0,len(pTest)-1)]
        else:
            return typeAct.AUTRE

    def prochainCoup(self, jr, adv, grille):
        if jr.endurance>10:
            return self.sapprocher(jr, adv, grille)
        else:
            return self.seloigner(jr, adv, grille)