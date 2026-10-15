import json

class Capteur:

    def __init__(self,nom, mesures_brutes):

        self.nom = nom
        self.brute = mesures_brutes
        self.nettoyer = []

    def nettoyer(self): #fonction qui garde uniquement les valeurs numériques, 
        self.nettoyer = propre
        propre = []
        for valeurs in mesures_brutes:
            if type(valeurs) == float:
                propre.append(valeurs)
        # il faut parcourir les valeurs de chaque liste et enlever les None, null, str, et int (sauf lumi) tout float

    def nb_valides(self): 
        return len(propre) #fonction qui garde et compte uniquement les valeurs valides, 


    def nb_anomalies(self):

        return len(mesures_brutes) - len(propre) # fonction nb anomalies

  
    def moyenne(self): #fonction qui fait la moyenne des valeurs depuis valeur valide sum (de tout) diviser par len de tout ( nb de val)
        return sum(propre) - len(propre)


    
    def mini(self): #fonction qui renvoie la plus petite valeur faire un min(de tout)
        return min(propre)


    
    def maxi(self): #fonction qui renvoie la plus grande valeur faire un max(de tout)
        return max(propre)

    
    def amplitude(self): # fonction diff entre vmax et vmin qu'on a recup plus haut
        return max(propre) - min(propre)


    
    def charger(self,path):              #fonction qui charge le fichier json
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)


        capteur = {}

        for nom, mesures in donnees.items():
            capteur = Capteur(nom,mesures)
            capteur.nettoyer()

            capteurs[nom] = capteur
        return capteurs


capteur = Capteur("temperature_bureau", [
    22.5,
    22.3,
  ])
print(capteur.nettoyer())

