import json

class Capteur:

    def __init__(self, nom, mesures_brutes):
        self.nom = nom
        self.brute = mesures_brutes
        self.nettoyer = []

    def nettoyer(self): 
        propre = []
        for valeurs in self.brute:
            if type(valeurs) == float:
                propre.append(valeurs)
        self.nettoyer = propre
        return propre

    def nb_valides(self):
        return len(self.nettoyer)

    def nb_anomalies(self):
        return len(self.brute) - len(self.nettoyer)

    def moyenne(self):
        return sum(self.nettoyer) / len(self.nettoyer)

    def mini(self):
        return min(self.nettoyer)

    def maxi(self):
        return max(self.nettoyer)

    def amplitude(self):
        return max(self.nettoyer) - min(self.nettoyer)

    def charger(self, path):
        with open(path, 'r', encoding="utf-8") as file:
            donnees = json.load(file)

        capteurs = {}

        for nom, mesures in donnees.items():
            capteur = Capteur(nom, mesures)
            capteur.nettoyer()
            capteurs[nom] = capteur

        return capteurs


capteur = Capteur("temperature_bureau", [
    22.5,
    22.3,
])

print(capteur.nettoyer())