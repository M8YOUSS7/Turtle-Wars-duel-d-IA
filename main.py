#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:48:15 2023

@author: yyouss
"""
import sys
import arene as Arn;
import tools as tl;

if __name__ == "__main__":
    debug = False
    size  = 9
    ia1   = "expert"
    ia2   = "expert"
    save  = False
    loop  = 1
    archives = False
    u4=False
    u8=False
    
    """
        Récupération des args
    """
    if len(sys.argv)>1:
        for i, arg in enumerate(sys.argv):
            if arg=="--debug" or arg=="-d":
                debug = True
            
            elif arg=="--size" or arg=="-s":
                size = int(sys.argv[i+1])
                while size<=1:
                    print("Taille innapropriée :", size)
                    size = int(input("Entrez une taille supérieur à 1\n"))
            
            elif arg=="--aim1":
                ia1 =sys.argv[i+1]
            
            elif arg=="--aim2":
                ia2 =sys.argv[i+1]
            
            elif arg=="--save" or arg=="-S":
                save = True

            elif arg=="--loop" or arg=="-l":
                loop = int(sys.argv[i+1])

            elif arg=="--arcv" or arg=="-a":
                archives = True
            
            elif arg=="--unrol4" or arg=="-u4":
                u4 = True
                
            elif arg=="--unrol8" or arg=="-u8":
                u4 = True

            elif arg=="--help" or arg=="-h":
                print("---Bienvenu sur Turtle Wars --- By Mahamt Youssouf : #yyouss@etud.univ-angers.fr---")
                print("--size (-s) pour fixer la taille")
                print("--debug (-d) pour utiliser le mode debug")
                print("--aim1 (--aim2) pour speciffier quel IA dois utiliser le joueur 1(2).", "Utilser uen des IA implemnter suivants : Expert, Perceptron, ArmeLegere, ArmeLourde, Manuelle.", sep="\n")
                print("--save (-S) pour sauvegarder (la)les parties jouer")
                print("--loop (-l) pour jouer plusieurs parties")
                print("--arcv (-a) pour consulter les parties sauvegardées")
                print("--unrol4 (-u4) pour un depliage par de boucle 4")
                print("--unrol8 (-u8) pour un depliage par boucle 8")
                exit()
                
    fileName = "./DATA/data{}".format(size)
    monAr    = Arn.Arene(size, ia1, ia2, fileName)

    if archives==True:
        tl.archives(fileName)
        exit()

    if debug==True:
        if save==True:
            if u8==True and loop>=8:
                tl.loopUnRooling8DebugSave(fileName, monAr, loop)
            elif u4==True and loop>=4:
                tl.loopUnRooling4DebugSave(fileName, monAr, loop)
            else:
                for i in range(loop):
                    monAr.nouvellePartie()
                    monAr.joueDebug()
                    monAr.save()
                
                tl.save(fileName, monAr.getGammes())
    
        else:
            if u8==True and loop>=8:
                tl.loopUnRooling8Debug(fileName, monAr, loop)
            elif u4==True and loop>=4:
                tl.loopUnRooling4Debug(fileName, monAr, loop)
            else:
                for i in range(loop):
                    monAr.nouvellePartie()
                    monAr.joueDebug()

        print("En ",loop, " parties, ", monAr.j1.aim.name, " à gagnée ", monAr.j1.points, " et ", monAr.j2.aim.name, " à gagnée ", monAr.j2.points, sep="")

    else:
        if save==True:
            if u8==True and loop>=8:
                tl.loopUnRooling8Save(fileName, monAr, loop)
            elif u4==True and loop>=4:
                tl.loopUnRooling4Save(fileName, monAr, loop)
            else:
                for i in range(loop):
                    monAr.nouvellePartie()
                    monAr.joue()
                    monAr.save()
                
                tl.save(fileName, monAr.getGammes())

        else:
            if u8==True and loop>=8:
                tl.loopUnRooling8(fileName, monAr, loop)
            elif u4==True and loop>=4:
                tl.loopUnRooling4(fileName, monAr, loop)
            else:
                for i in range(loop):
                    monAr.nouvellePartie()
                    monAr.joue()