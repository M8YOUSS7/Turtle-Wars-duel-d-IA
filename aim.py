#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:58:57 2023
@author: yyouss
"""
import random;
from action import *

class IA:
    def __init__(self, name):
        self.name = name
    
    def ligVide(self, x1, x2, y, grille):
        return (grille[x1:x2, y]==0).all()

    def colVide(self, x, y1, y2, grille):
        return (grille[x, y1:y2]==0).all()

    def deplacements(self, x, y, grille):
        res = []
        t   = mt.sqrt(np.size(grille))

        if x-1 >=0 and grille[x-1,y] == 0:
            res.append(typeAct.MONTE)
        
        if x+1 <t and grille[x+1,y] == 0:
            res.append(typeAct.DESCENDS)
        
        if y-1 >=0 and grille[x,y-1] == 0:
            res.append(typeAct.GAUCHE)
        
        if y+1 <t and grille[x,y+1] == 0:
            res.append(typeAct.DROITE)

        return res

    def prochainCoup(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)

        return pTest[random.randint(0,len(pTest)-1)]

class IAExpert(IA):
    def __init__(self):
        IA.__init__(self, "expert")

    def sapprocher(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        """
            Position de l'adversaire par rapport au joueur
        """
        mmCol   = True if xTest==0 else False
        mmLigne = True if yTest==0 else False
        enHaut  = True if xTest>0 else False
        enBas   = True if xTest<0 else False
        aGauche = True if yTest>0 else False
        aDroite = True if yTest<0 else False
        
        if len(pTest)>0:
            unChoix = pTest[random.randint(0,len(pTest)-1)]
            if mmCol==True:
                if yTest==1 or yTest==-1 or (aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True) or (aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==True):
                    return typeAct.TIRE
                
                elif aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix

                elif aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                
            elif mmLigne==True:
                if xTest==1 or xTest==-1 or (enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==True) or (enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==True):
                    return typeAct.TIRE
                
                elif enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix
                        else:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix

                elif enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix
                        else:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix

            elif enHaut==True and aGauche==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix
                else:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix
            
            elif enHaut==True and aDroite==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix
                else:
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix

            elif enBas==True and aGauche==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix
                else:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix

            elif enBas==True and aDroite==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix
                else:
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix

        else:
            return typeAct.AUTRE

    def seloigner(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        """
            Position de l'adversaire par rapport au joueur
        """
        mmCol   = True if xTest==0 else False
        mmLigne = True if yTest==0 else False
        enHaut  = True if xTest>0 else False
        enBas   = True if xTest<0 else False
        aGauche = True if yTest>0 else False
        aDroite = True if yTest<0 else False
        
        if len(pTest)>0:
            unChoix = pTest[random.randint(0,len(pTest)-1)]
            if mmCol==True:
                if yTest==1 or (aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True):
                    dTest = random.randint(0,9)

                    if dTest==0:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return unChoix
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                
                elif aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    dTest = random.randint(0,9)

                    if dTest==0:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix

                    else:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return unChoix
                
                elif yTest==-1 or (aDroite==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True):
                    dTest = random.randint(0,9)

                    if dTest==0:
                        if typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return unChoix
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix
                
                elif aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    dTest = random.randint(0,9)

                    if dTest==0:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix

                    else:
                        if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        else:
                            return unChoix

            elif mmLigne==True:
                if xTest==-1 or (enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==True):
                    dTest = random.randint(0,9)

                    if dTest==0:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix
                        else:
                            if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix
                
                elif enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    dTest = random.randint(0,9)

                    if dTest==0:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix
                        else:
                            if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix

                    else:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix
                
                elif xTest==1 or (enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==True):
                    dTest = random.randint(0,9)

                    if dTest==0:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix
                    else:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix
                        else:
                            if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix

                elif enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    dTest = random.randint(0,9)

                    if dTest==0:
                        dTest = random.randint(0,1)
                        if dTest==1:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix
                        else:
                            if typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix
                    else:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix
                            
            elif enHaut==True and aGauche==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix
                else:
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix
            
            elif enHaut==True and aDroite==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix
                else:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix

            elif enBas==True and aGauche==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix
                else:
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix

            elif enBas==True and aDroite==True:
                dTest = random.randint(0,1)
                
                if dTest==1:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix
                else:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix
        else:
            return typeAct.AUTRE

    def prochainCoup(self, jr, adv, grille):
        if jr.endurance>=20:
            return self.sapprocher(jr, adv, grille)
        else:
            return self.seloigner(jr, adv, grille)

import os.path
from sklearn.linear_model import Perceptron




class IAPerceptron(IA):
    def __init__(self):
        IA.__init__(self, "perceptron")

        self.X =[]
        self.y =[]

        self.clf = clf = Perceptron(tol=1e-3, random_state=0)

    def numToAct(self, num):
            if num==1:
                return typeAct.MONTE
            elif num==2:
                return typeAct.DESCENDS
            elif num==3:
                return typeAct.GAUCHE
            elif num==4:
                return typeAct.DROITE
            elif num==5:
                return typeAct.TIRE
            else:
                return typeAct.AUTRE

    def prochainCoup(self, fileName, jr, adv, grille):
        if os.path.isfile(fileName + '.npy')==True:
            data = data = np.load(fileName + '.npy')
            for e in data:
                self.X.append(e[:-1])
                self.y.append(e[-1])
            
            self.clf.fit(self.X, self.y)

            aPredir                 = grille
            #le cas ou le joeur 2 serai le perceptron
            if aPredir[jr.x, jr.y]!=1:
                aPredir[jr.x, jr.y]     = 1
                aPredir[adv.x, adv.y]   = 2
            aPredir                 = aPredir.reshape(-1)
            aPredir                 = np.append(aPredir, [jr.endurance, jr.vie])

            r = self.clf.predict([aPredir])

            
            return self.numToAct(r[0])
        else:
            return IA.prochainCoup(jr, adv, grille)

class IANaiveArmeLegere(IA):
    def __init__(self):
        IA.__init__(self, "IA Naive Arme Legère")

    def sapprocher(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        """
            Position de l'adversaire par rapport au joueur
        """
        mmCol   = True if xTest==0 else False
        mmLigne = True if yTest==0 else False
        enHaut  = True if xTest>0 else False
        enBas   = True if xTest<0 else False
        aGauche = True if yTest>0 else False
        aDroite = True if yTest<0 else False

        xTestAbs = abs(xTest)
        yTestAbs = abs(yTest)
        

        if len(pTest)>0:
            unChoix = pTest[random.randint(0,len(pTest)-1)]
            if mmCol==True:
                if yTest==1 or yTest==-1 or (aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True) or (aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==True):
                    return typeAct.TIRE
                
                elif aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix

                elif aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                
            elif mmLigne==True:
                if xTest==1 or xTest==-1 or (enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==True) or (enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==True):
                    return typeAct.TIRE
                
                elif enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix
                        else:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix

                elif enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix
                        else:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix

            elif xTestAbs > yTestAbs:
                if enBas==True and typeAct.DESCENDS in pTest:
                    return typeAct.DESCENDS

                elif enHaut==True and typeAct.MONTE in pTest:
                    return typeAct.MONTE

                else:
                    return unChoix

            elif xTestAbs < yTestAbs:
                if aGauche==True and typeAct.GAUCHE in pTest:
                    return typeAct.GAUCHE

                elif aDroite==True and typeAct.DROITE in pTest:
                    return typeAct.DROITE
                    
                else:
                    return unChoix
        else:
            return typeAct.AUTRE

    def seloigner(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        """
            Position de l'adversaire par rapport au joueur
        """
        mmCol   = True if xTest==0 else False
        mmLigne = True if yTest==0 else False
        enHaut  = True if xTest>0 else False
        enBas   = True if xTest<0 else False
        aGauche = True if yTest>0 else False
        aDroite = True if yTest<0 else False

        xTestAbs = abs(xTest)
        yTestAbs = abs(yTest)
        
        if len(pTest)>0:
            unChoix = pTest[random.randint(0,len(pTest)-1)]
            if mmCol==True:
                if yTest==1 or (aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True):
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix
                
                elif aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix
                
                elif yTest==-1 or (aDroite==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True):
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix
                
                elif aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix

            elif mmLigne==True:
                if xTest==-1 or (enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==True):
                    if typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix
                
                elif enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix
                
                elif xTest==1 or (enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==True):
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix

                elif enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix
                            
            elif xTestAbs > yTestAbs:
                if enBas==True:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix

                elif enHaut==True:
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix

            elif xTestAbs < yTestAbs:
                if aGauche==True:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix

                elif aDroite==True:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix

        else:
            return typeAct.AUTRE

    def prochainCoup(self, jr, adv, grille):
        if jr.endurance>11:
            return self.sapprocher(jr, adv, grille)
        else:
            return self.seloigner(jr, adv, grille)

class IANaiveArmeLourde(IA):
    def __init__(self):
        IA.__init__(self, "IA Naive Arme Lourde")

    def sapprocher(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        """
            Position de l'adversaire par rapport au joueur
        """
        mmCol   = True if xTest==0 else False
        mmLigne = True if yTest==0 else False
        enHaut  = True if xTest>0 else False
        enBas   = True if xTest<0 else False
        aGauche = True if yTest>0 else False
        aDroite = True if yTest<0 else False

        xTestAbs = abs(xTest)
        yTestAbs = abs(yTest)
        

        if len(pTest)>0:
            unChoix = pTest[random.randint(0,len(pTest)-1)]
            if mmCol==True:
                if yTest==1 or yTest==-1 or (aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True) or (aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==True):
                    return typeAct.TIRE
                
                elif aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            else:
                                return unChoix

                elif aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                        else:
                            if typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            else:
                                return unChoix
                
            elif mmLigne==True:
                if xTest==1 or xTest==-1 or (enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==True) or (enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==True):
                    return typeAct.TIRE
                
                elif enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.MONTE in pTest:
                            return typeAct.MONTE
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix
                        else:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.MONTE in pTest:
                                return typeAct.MONTE
                            else:
                                return unChoix

                elif enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    dTest = random.randint(0,3)
                    
                    if dTest==0:
                        if typeAct.DESCENDS in pTest:
                            return typeAct.DESCENDS
                        elif typeAct.DROITE in pTest:
                            return typeAct.DROITE
                        elif typeAct.GAUCHE in pTest:
                            return typeAct.GAUCHE
                        else:
                            return unChoix

                    else:
                        dTest = random.randint(0,1)
                        
                        if dTest==0:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix
                        else:
                            if typeAct.GAUCHE in pTest:
                                return typeAct.GAUCHE
                            elif typeAct.DROITE in pTest:
                                return typeAct.DROITE
                            elif typeAct.DESCENDS in pTest:
                                return typeAct.DESCENDS
                            else:
                                return unChoix

            elif xTestAbs > yTestAbs:
                if aGauche==True and typeAct.GAUCHE in pTest:
                    return typeAct.GAUCHE

                elif aDroite==True and typeAct.DROITE in pTest:
                    return typeAct.DROITE
                    
                else:
                    return unChoix

            elif xTestAbs < yTestAbs:
                if enBas==True and typeAct.DESCENDS in pTest:
                    return typeAct.DESCENDS

                elif enHaut==True and typeAct.MONTE in pTest:
                    return typeAct.MONTE

                else:
                    return unChoix

        else:
            return typeAct.AUTRE

    def seloigner(self, jr, adv, grille):
        pTest = self.deplacements(jr.x, jr.y, grille)
        xTest = jr.x - adv.x
        yTest = jr.y - adv.y
        """
            Position de l'adversaire par rapport au joueur
        """
        mmCol   = True if xTest==0 else False
        mmLigne = True if yTest==0 else False
        enHaut  = True if xTest>0 else False
        enBas   = True if xTest<0 else False
        aGauche = True if yTest>0 else False
        aDroite = True if yTest<0 else False

        xTestAbs = abs(xTest)
        yTestAbs = abs(yTest)
        
        if len(pTest)>0:
            unChoix = pTest[random.randint(0,len(pTest)-1)]
            if mmCol==True:
                if yTest==1 or (aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True):
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix
                
                elif aGauche==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==False:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix
                
                elif yTest==-1 or (aDroite==True and self.colVide(jr.x, adv.y+1, jr.y, grille)==True):
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix
                
                elif aDroite==True and self.colVide(jr.x, jr.y+1, adv.y, grille)==False:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix

            elif mmLigne==True:
                if xTest==-1 or (enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==True):
                    if typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix
                
                elif enHaut==True and self.ligVide(adv.x+1, jr.x, jr.y, grille)==False:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix
                
                elif xTest==1 or (enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==True):
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix

                elif enBas==True and self.ligVide(jr.x+1, adv.x, jr.y, grille)==False:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix
                            
            elif xTestAbs > yTestAbs:
                if enBas==True:
                    if typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    else:
                        return unChoix

                elif enHaut==True:
                    if typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    else:
                        return unChoix

            elif xTestAbs < yTestAbs:
                if aGauche==True:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.DROITE in pTest:
                        return typeAct.DROITE
                    else:
                        return unChoix

                elif aDroite==True:
                    if typeAct.MONTE in pTest:
                        return typeAct.MONTE
                    elif typeAct.DESCENDS in pTest:
                        return typeAct.DESCENDS
                    elif typeAct.GAUCHE in pTest:
                        return typeAct.GAUCHE
                    else:
                        return unChoix

        else:
            return typeAct.AUTRE

    def prochainCoup(self, jr, adv, grille):
        if jr.endurance>32:
            return self.sapprocher(jr, adv, grille)
        else:
            return self.seloigner(jr, adv, grille)


class IAManelle(IA):
    def __init__(self):
        nom = input('Votre nom :')
        IA.__init__(self, nom)

    def prochainCoup(self, jr, adv, grille):
        cp=0
        while(cp!=1 and cp!=2 and cp!=2 and cp!=3 and cp!=4 and cp!=5):
            print("Entrée : ", "1 : pour Monter", "2 : pour Descendre", "3 : pour aller à Gauche", "4 : pour aller à Droite", "5 : pour Tirée", "-1 pour avoir une indice", sep="\n")
            cp = int(input(""))

            if cp==1:
                return typeAct.MONTE
            elif cp==2:
                return typeAct.DESCENDS
            elif cp==3:
                return typeAct.GAUCHE
            elif cp==4:
                return typeAct.DROITE
            elif cp==5:
                return typeAct.TIRE
            elif cp==-1:
                for d in self.deplacements(jr.x, jr.y, grille):
                    print(d)
            else:
                print("Coup invalid reessayer !")
