#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

import numpy as np;
from enum import Enum;

class typeAct(Enum):
    AUTRE    = 0
    MONTE    = 1
    DESCENDS = 2
    GAUCHE   = 3
    DROITE   = 4
    TIRE     = 5

class Action:
    def __init__(self, act):
        self.action = act

    def swap(self, x1, y1, x2, y2, grille):
        t   = grille[0].size
        res = False
        if (x2>=0) and (x2<t) and (y2>=0) and (y2<t) and (grille[x2, y2]==0) and (grille[x1, y1]==1 or grille[x1, y1]==2):
            val = grille[x1, y1]
            grille[x1, y1] = 0
            grille[x2, y2] = val
            res = True
        
        return res

    def execAct(self, jr, adv, grille):
        x =jr.x
        y =jr.y
        ply = grille[x, y]

        if self.action==typeAct.MONTE:
            if jr.monte()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.descends()
            else:
                jr.endurance = 0
                
        elif self.action==typeAct.DESCENDS:
            if jr.descends()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.monte()
            else:
                jr.endurance = 0
                
        elif self.action==typeAct.GAUCHE:
            if jr.gauche()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.droite()
            else:
                jr.endurance = 0

        elif self.action==typeAct.DROITE:
            if jr.droite()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.gauche()
            else:
                jr.endurance = 0
                
        elif self.action==typeAct.TIRE:
            if jr.tire(adv)==False:
                jr.endurance = 0
        else:
            jr.endurance = 0
            jr.vie = 0
    
    def execActDebug(self, jr, adv, grille):
        x =jr.x
        y =jr.y
        ply = int(grille[x, y])

        if self.action==typeAct.MONTE:
            if jr.monte()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    print("J", ply, " impossible de MONTE", sep="")
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.descends()
                else:
                    print("J", ply, " MONTE : (",x,",",y,") => (",jr.x,",",jr.y,")", sep="")
            else:
                jr.endurance = 0
                
        elif self.action==typeAct.DESCENDS:
            if jr.descends()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    print("J", ply, " impossible de DESCENDRE", sep="")
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.monte()
                else:
                    print("J", ply, " DESCENDS : (",x,",",y,") => (",jr.x,",",jr.y,")", sep="")
            else:
                jr.endurance = 0
                
        elif self.action==typeAct.GAUCHE:
            if jr.gauche()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    print("J", ply, " impossible d'aller à GAUCHE", sep="")
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.droite()
                else:
                    print("J", ply, " GAUCHE : (",x,",",y,") => (",jr.x,",",jr.y,")", sep="")
            else:
                jr.endurance = 0

        elif self.action==typeAct.DROITE:
            if jr.droite()==True:
                if self.swap(x, y, jr.x, jr.y, grille)==False:
                    print("J", ply, " impossible d'aller à DROITE", sep="")
                    jr.endurance += (2 * jr.chargeTotal()) + 10
                    jr.gauche()
                else:
                    print("J", ply, " DROITE : (",x,",",y,") => (",jr.x,",",jr.y,")", sep="")
            else:
                jr.endurance = 0
                
        elif self.action==typeAct.TIRE:
            if jr.tire(adv)==True:
                print("J", ply, " TIRE", sep="")
            else:
                jr.endurance = 0
                print("J", ply, " impossible de TIRE", sep="")
        else:
            jr.endurance = 0
            jr.vie = 0
            print("J", ply, " impossible de faire une action, Abandon...", sep="")