import os.path
import numpy as np

def save(fileName, data):
        if os.path.isfile(fileName + '.npy')==False:
                np.save(fileName, data)
                #print(data)
        else:
                forSave = np.load(fileName + '.npy')
                data = np.append(forSave, data, axis=0)
                np.save(fileName, data)
       
def archives(fileName):
        if os.path.isfile(fileName + '.npy')==True:
                arcv = np.load(fileName + '.npy')
                print(arcv)
                print("Taille de l'archive :", arcv.size)

def loopUnRooling4Save(fileName, monAr, size):
        l = int(size/4)*4
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                i += 4

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()

                i += 1

        save(fileName, monAr.getGammes())

def loopUnRooling4DebugSave(fileName, monAr, size):
        l = int(size/4)*4
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                i += 4

        while i < size:
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()

                i += 1

        save(fileName, monAr.getGammes())

def loopUnRooling4(fileName, monAr, size):
        l = int(size/4)*4
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                i += 4

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()

                i += 1

def loopUnRooling4Debug(fileName, monAr, size):
        l = int(size/4)*4
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                i += 4

        while i < size:
                monAr.nouvellePartie()
                monAr.joueDebug()

                i += 1

def loopUnRooling8Debug(fileName, monAr, size):
        l = int(size/8)*8
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                
                i += 8

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                i += 1

def loopUnRooling8DebugSave(fileName, monAr, size):
        l = int(size/8)*8
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joueDebug()
                monAr.save()
                
                i += 8

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                i += 1

        
        save(fileName, monAr.getGammes())

def loopUnRooling8Save(fileName, monAr, size):
        l = int(size/8)*8
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()

                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                i += 8

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                i += 1

        
        save(fileName, monAr.getGammes())

def loopUnRooling8(fileName, monAr, size):
        l = int(size/8)*8
        i = 0
        
        while i < l:
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()

                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                
                monAr.nouvellePartie()
                monAr.joue()
                
                i += 8

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()
                
                i += 1