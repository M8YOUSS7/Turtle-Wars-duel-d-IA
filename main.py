#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:48:15 2023

@author: yyouss
"""
import modele as md;

if __name__ == "__main__":

    monAr = md.Arene(5)
    print("-----· Debut de jeu -----·\n")
    print(monAr.grille)
    
    monAr.joue()
    
    
    print("-----· Fin de jeu -----·\n")
    print(monAr.grille)