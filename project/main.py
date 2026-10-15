import json

class Capteur: #Une classe capteur qui encapsulele nom d'un capteur, ses mesures brutes

    def __init__(self, nom, mesures_brutes):
        self.nom = nom
        self.brute = mesures_brutes
        self.nettoyer = []

    def nettoyer(self): #fonction qui garde uniquement les valeurs numériques, 
        for valeurs in self.brute:
            if type(valeurs) == float:
                self.nettoyer.append(valeurs)
        return self.nettoyer
         # il faut parcourir les valeurs de chaque liste et enlever les None, null, str, et int (sauf lumi) tout float

    def nb_valides(self):
        return len(self.nettoyer) 
        #fonction qui garde et compte uniquement les valeurs valides, 

    def nb_anomalies(self):
        return len(self.brute) - len(self.nettoyer)
        # anomalies de fonction nb

    def moyenne(self):  #fonction qui fait la moyenne des valeurs depuis valeur valide sum (de tout) diviser par len de tout ( nb de val)
        return sum(self.nettoyer) / len(self.nettoyer)

    def mini(self): #fonction qui renvoie la plus petite valeur faire un min(de tout)
        return min(self.nettoyer)

    def maxi(self): #fonction qui renvoie la plus grande valeur faire un max(de tout)
        return max(self.nettoyer)

    def amplitude(self): # fonction diff entre vmax et vmin qu'on a recup plus haut
        return max(self.nettoyer) - min(self.nettoyer)

    # def charger(self, path): #fonction qui charge le fichier json
    #     with open(path, 'r', encoding="utf-8") as file:
    #         donnees = json.load(file)

    #     capteurs = {}

    #     for nom, mesures in donnees.items():
    #         capteur = Capteur(nom, mesures)
    #         capteur.nettoyer()
    #         capteurs[nom] = capteur

    #     return capteurs


capteur = Capteur("temperature_bureau", [22.5, 22.3,])

print(capteur.nettoyer())