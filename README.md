# Turtle-Wars-duel-d-IA

Class['Turtle Wars']= [arme, tortue, joueur, obstacle, action, arene]

Une arene es constituer d'une grille d'emplacements des elements et de deux joueurs. Dans la grille 'V' designe la case vide et '1' ou  '2' designe une tortue(joueur) et  'O' represente n'importe quel obstacle.

Naturelement les joueurs chercheront à s'appropcher l'un à l'autre afin de se tirer decu. Voici l'idee de la primiere IA. 

Lancer l'application avec pyhon3 main.py --help pour plus d'information.

Le jeu debut avec deux joueurs, qui ont 100 en "vie" et 100 en "endurance"
Une arme a un nom et un poids et est claasé selon son poids.(T1 => 2 de degats pour poids < 5, T2 => 4 de degats pour poids < 10 et T3 => 8 de degats pour poids >= 15)
Lors qu'un joeur tante de sortir de l'arene, il perds 10 en ednurance.
