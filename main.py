#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:48:15 2023

@author: yyouss
"""
import sys
import modele as md;

if __name__ == "__main__":
    debug = False
    size  = 5
    ia1 = ""
    ia2 = ""
    
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
                print("---Bienvenu sur Turtle Wars ---\n---By Mahamt Youssouf : @yyouss---")
                print("--size (-s) pour fixer la taille")
                print("--debug (-d) pour utiliser le mode debug")
                exit()
            
            elif arg=="--aim1":
                ia1 =sys.argv[i+1]
            
            elif arg=="--aim2":
                ia2 =sys.argv[i+1]
                
    if debug==True:
        monAr = md.Arene(size, ia1, ia2)
        monAr.joueDebugIA()
    else:
        monAr = md.Arene(size, ia1, ia2)
        #monAr.joue()