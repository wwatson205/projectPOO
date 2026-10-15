import json

class Capteur:

    def __init__(self,nom, mesures_brutes):

        self.nom = nom
        self.brute = mesures_brutes
        self.nettoyer = nettoyer()

    def nettoyer(self): #fonction qui garde uniquement les valeurs numériques, 
        # il faut parcourir les valeurs de chaque liste et enlever les None, null, str, et int (sauf lumi) tout float

    def nb_valides(self): #fonction qui garde et compte uniquement les valeurs valides, 
        # parcourir toutes les valeurs valides et faire +1 au compteur des que valeur est valide

    def nb_anomalies(self):# fonction nb anomalies
         # parcourir toutes les valeurs non valides et faire +1 au compteur des que valeur est non val
  
    def moyenne(self): #fonction qui fait la moyenne des valeurs depuis valeur valide sum (de tout) diviser par len de tout ( nb de val)

    def mini(self): #fonction qui renvoie la plus petite valeur faire un min(de tout)

    def maxi(self): #fonction qui renvoie la plus grande valeur faire un max(de tout)

    def amplitude(self): # fonction diff entre vmax et vmin qu'on a recup plus haut

    def charger(self,path): #fonction qui charge le fichier json

