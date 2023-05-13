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
                print(arcv.size)

def loopUnRooling4(fileName, monAr, size):
        l = (size/4)*4
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
                
                save(fileName, monAr.getGammes())
                i += 4

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()

                save(fileName, monAr.getGammes())
                i += 1

def loopUnRooling8(fileName, monAr, size):
        l = (size/8)*8
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
                
                save(fileName, monAr.getGammes())
                i += 8

        while i < size:
                monAr.nouvellePartie()
                monAr.joue()
                monAr.save()
                
                save(fileName, monAr.getGammes())
                i += 1