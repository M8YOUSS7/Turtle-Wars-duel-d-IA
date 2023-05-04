#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:48:15 2023

@author: yyouss
"""
import sys
import arene as Arn;

if __name__ == "__main__":
    debug = False
    size  = 5
    ia1   = "expert"
    ia2   = "expert"
    save  = False
    loop  = 1
    
    """
        Récupération des args
    """
    if len(sys.argv)>1:
        for i, arg in enumerate(sys.argv):
            if arg=="--debug" or arg=="-d":
                debug = True
            
            elif arg=="--size" or arg=="-s":
                if int(sys.argv[i+1])>1:
                    size = int(sys.argv[i+1])
                else:
                    print("Taille innapropriée :", sys.argv[i+1], "\nTaille doit être superieur à 1 !")
                    exit()
            
            elif arg=="--help" or arg=="-h":
                print("---Bienvenu sur Turtle Wars --- By Mahamt Youssouf : #yyouss@etud.univ-angers.fr---")
                print("--size (-s) pour fixer la taille")
                print("--debug (-d) pour utiliser le mode debug")
                print("--aim1 (--aim2) pour speciffier quel IA dois utiliser le joueur 1(2)")
                print("--save (-S) pour sauvegarder (la)les parties jouer")
                print("--loop (-l) pour jouer plusieurs parties")
                exit()
            
            elif arg=="--aim1":
                ia1 =sys.argv[i+1]
            
            elif arg=="--aim2":
                ia2 =sys.argv[i+1]
            
            elif arg=="--save" or arg=="-S":
                save = True

            elif arg=="--loop" or arg=="-l":
                loop = int(sys.argv[i+1])
                
    monAr = Arn.Arene(size, ia1, ia2)

    if debug==True:
        if save==True:
            for i in range(loop):
                monAr.nouvellePartie()
                monAr.joueDebugIA()

            print("En",loop, "parties, J1 à gagnée", monAr.j1.points, " et J2 à gagnée", monAr.j2.points)
            
        else:
            for i in range(loop):
                monAr.nouvellePartie()
                monAr.joueDebugIA()

            print("En",loop, "parties, J1 à gagnée", monAr.j1.points, " et J2 à gagnée", monAr.j2.points)

    else:
        if save==True:
            for i in range(loop):
                monAr.nouvellePartie()
                monAr.joue()
        else:
            for i in range(loop):
                monAr.nouvellePartie()
                monAr.joue()