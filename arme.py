#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

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