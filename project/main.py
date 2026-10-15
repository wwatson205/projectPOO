import json


class Capteur:

    def __init__(self, nom, mesures_brutes):
        # Initialise le nom du capteur et ses mesures brutes.
        self.nom = nom
        self.brute = mesures_brutes

        # Cree une liste vide pour stocker les mesures nettoyees.
        self.mesures_propres = []

    def nettoyer(self):
        # Garde uniquement les valeurs numeriques autorisees.
        propre = []

        # Parcourt toutes les mesures brutes du capteur.
        for valeurs in self.brute:

            # Pour la luminosite, accepte les nombres entiers et decimaux.
            if self.nom == "luminosite_atelier":
                if type(valeurs) == float or type(valeurs) == int:
                    # Ajoute la valeur a la liste des mesures propres.
                    propre.append(valeurs)

            else:
                # Pour les autres capteurs, accepte uniquement les float.
                if type(valeurs) == float:
                    # Ajoute la valeur valide a la liste.
                    propre.append(valeurs)

        # Enregistre les mesures nettoyees dans l'objet.
        self.mesures_propres = propre

        # Retourne la liste des mesures nettoyees.
        return propre

    def nb_valides(self):
        # Retourne le nombre de mesures propres.
        return len(self.mesures_propres)

    def nb_anomalies(self):
        # Calcule le nombre de mesures rejetees.
        # On soustrait le nombre de mesures valides aux mesures brutes.
        return len(self.brute) - len(self.mesures_propres)

    def moyenne(self):
        # Verifie si la liste des mesures propres est vide.
        if len(self.mesures_propres) == 0:
            return None

        # Calcule la moyenne : somme des valeurs divisee par leur nombre.
        return sum(self.mesures_propres) / len(self.mesures_propres)

    def mini(self):
        # Verifie qu'il existe au moins une mesure valide.
        if len(self.mesures_propres) == 0:
            return None

        # Retourne la plus petite valeur de la liste.
        return min(self.mesures_propres)

    def maxi(self):
        # Verifie qu'il existe au moins une mesure valide.
        if len(self.mesures_propres) == 0:
            return None

        # Retourne la plus grande valeur de la liste.
        return max(self.mesures_propres)

    def amplitude(self):
        # Verifie qu'il existe au moins une mesure valide.
        if len(self.mesures_propres) == 0:
            return None

        # Calcule l'amplitude : maximum moins minimum.
        amp = max(self.mesures_propres) - min(self.mesures_propres)

        # Arrondit le resultat a deux chiffres apres la virgule.
        return round(amp, 2)


    def charger(self, path):
        # Ouvre le fichier JSON et recupere les donnees.
        with open(path, "r", encoding="utf-8") as file:
            donnees = json.load(file)

            # Cree un dictionnaire pour stocker les capteurs.
            capteurs = {}

            # Parcourt les noms et les mesures de chaque capteur.
            for nom, mesures in donnees.items():

                # Cree un objet Capteur pour chaque liste.
                capteur = Capteur(nom, mesures)

                # Nettoie les mesures du capteur.
                capteur.nettoyer()

                # Ajoute le capteur dans le dictionnaire.
                capteurs[nom] = capteur

            return capteurs



capteur = Capteur("", [])
capteurs = capteur.charger("mesures_capteurs_reseau.json")

for nom, capteur in capteurs.items():
    print("Capteur :", nom)
    print("Mesures propres :", capteur.mesures_propres)
    print("Nombre de valeurs valides :", capteur.nb_valides())
    print("Nombre d'anomalies :", capteur.nb_anomalies())
    print("Moyenne :", capteur.moyenne())
    print("Minimum :", capteur.mini())
    print("Maximum :", capteur.maxi())
    print("Amplitude :", capteur.amplitude(),"\n") # pour sauter une ligne et laisser de la place pour les autres dicos
    
