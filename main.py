#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:48:15 2023

@author: yyouss
"""
import sys
import arene as Arn;
import tools as tl;

def tournois(config, nbParties, fileName):
    arene1 = Arn.Arene(config, "expert", "expert", fileName)
    arene2 = Arn.Arene(config, "expert", "perceptron", fileName)
    arene3 = Arn.Arene(config, "expert", "armelegere", fileName)
    arene4 = Arn.Arene(config, "expert", "armelourde", fileName)
    arene5 = Arn.Arene(config, "perceptron", "perceptron", fileName)
    arene6 = Arn.Arene(config, "perceptron", "armelegere", fileName)
    arene7 = Arn.Arene(config, "perceptron", "armelourde", fileName)
    arene8 = Arn.Arene(config, "armelegere", "armelourde", fileName)
    arene9 = Arn.Arene(config, "armelegere", "armelegere", fileName)
    arene10 = Arn.Arene(config, "armelourde", "armelourde", fileName)
    
    tl.loopUnRooling8(fileName, arene1, nbParties)
    tl.loopUnRooling8(fileName, arene2, nbParties)
    tl.loopUnRooling8(fileName, arene3, nbParties)
    tl.loopUnRooling8(fileName, arene4, nbParties)
    tl.loopUnRooling8(fileName, arene5, nbParties)
    tl.loopUnRooling8(fileName, arene6, nbParties)
    tl.loopUnRooling8(fileName, arene7, nbParties)
    tl.loopUnRooling8(fileName, arene8, nbParties)
    tl.loopUnRooling8(fileName, arene9, nbParties)
    tl.loopUnRooling8(fileName, arene10, nbParties)
    print("*** Début de tournois *** Nombre de parties pour chaque duel :", nbParties, " *** taille d'arène :", config, " ***", sep="")
    print("En ",nbParties, " parties, ", arene1.j1.aim.name, " à gagnée ", arene1.j1.points, " et ", arene1.j2.aim.name, " à gagnée ", arene1.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene2.j1.aim.name, " à gagnée ", arene2.j1.points, " et ", arene2.j2.aim.name, " à gagnée ", arene2.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene3.j1.aim.name, " à gagnée ", arene3.j1.points, " et ", arene3.j2.aim.name, " à gagnée ", arene3.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene4.j1.aim.name, " à gagnée ", arene4.j1.points, " et ", arene4.j2.aim.name, " à gagnée ", arene4.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene5.j1.aim.name, " à gagnée ", arene5.j1.points, " et ", arene5.j2.aim.name, " à gagnée ", arene5.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene6.j1.aim.name, " à gagnée ", arene6.j1.points, " et ", arene6.j2.aim.name, " à gagnée ", arene6.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene7.j1.aim.name, " à gagnée ", arene7.j1.points, " et ", arene7.j2.aim.name, " à gagnée ", arene7.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene8.j1.aim.name, " à gagnée ", arene8.j1.points, " et ", arene8.j2.aim.name, " à gagnée ", arene8.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene9.j1.aim.name, " à gagnée ", arene9.j1.points, " et ", arene9.j2.aim.name, " à gagnée ", arene9.j2.points, sep="")
    print("En ",nbParties, " parties, ", arene10.j1.aim.name, " à gagnée ", arene10.j1.points, " et ", arene10.j2.aim.name, " à gagnée ", arene10.j2.points, sep="")
    print("*** Fin du tournois à bientôt ***")

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
    twt = False
    
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

            elif arg=="--tournois" or arg=="-twt":
                twt = True
                loop = int(sys.argv[i+1])

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
    
    elif twt==True:
        tournois(size, loop, fileName)
        exit()

    elif debug==True:
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