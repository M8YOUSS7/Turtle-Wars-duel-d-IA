# Turtle-Wars-duel-d-IA

# Done :
IA['Perceptron', 'Expert', 'NaiveArmeLourd', 'NaiveArmeLegere', 'Manuelle']
Class['Turtle Wars']= [arme, tortue, joueur, obstacle, action, arene]

Une arene es constitué d'une grille d'emplacements des éléments et de deux joueurs. Dans la grille 0 désigne la case vide et 1 ou  2 designe une tortue(joueur) et  3 represente n'importe quel obstacle.

Le jeu début avec deux joueurs, qui ont 100 en "vie" et 100 en "endurance"
Une arme est classé selon son poids.(T1 => 2 de dégats pour poids < 5, T2 => 4 de dégats pour poids < 10 et T3 => 8 de dégats pour poids >= 15)

#Les action possibles dans l'ordre sont :
  #0 => autre
  #1 => monter
  #2 => descendre
  #3 => gauche
  #4 => droite
  #5 => tire

Lors qu'un joeur tante de sortir de l'arêne, il perds 10 en "endurance".

Lors qu'un joueur attaque l'autre perds en "endurance" et son adversaire perds en "vie".

Naturelement les joueurs chercheront à s'appropcher l'un de l'autre afin de se tirer deçu. Voici l'idée de la primiere IA. 

Lancer l'application avec pyhon3 main.py --help pour plus d'information.

Prblemme de map couper en deux regler avec djikstra.
# To do :
#1)  Deep Learning
  #1=> Sauvegarde des parties => done
  #2=> Recuperations depuis la base de tous les données => done
  #3=> perceptron => done
  #4=> resaux de neuronne
  
#2)Interface Graphique (Simple) done.
#3)IA: Monte Carlo.
