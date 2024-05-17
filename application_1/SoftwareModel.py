import os, json, sys, PyQt6.QtCore

# -----------------------------------------------------------------------------
# --- class Outil
# -----------------------------------------------------------------------------


class SoftwareModel:

    # constructeur
    def __init__(self) -> None:

        # attributs

        self.nom_projet: str = ""
        self.auteur: str = ""
        self.date : PyQt6.QtCore.QDate = PyQt6.QtCore.QDate(0, 0, 0)
        self.nom: str = ""
        self.magasin: str = ""
        self.liste: list[str] = []
        self.postion_produit: dict = {}
        self.position_grille: dict = {}

        self.filePathPlan : str = ""
        self.filePath: str = ""

    # sauvegarder les informations du projet en cours dans un fichier ecrit en json.
    def enregistrerProjet(self) -> None:
        with open(self.filePath, "w", encoding="utf-8") as f:
            content = {
                "nom_projet": self.nom_projet,
                "auteur": self.auteur,
                "date": str(self.date),
                "nom": self.nom,
                "magasin": self.magasin,
                "liste": self.liste,
                "position_produit": self.postion_produit,
                "position_grille": self.position_grille,

                "fichier_plan_chemin": self.filePathPlan,
                "fichier_chemin": self.filePath
            }
            json.dump(content, f)

    # charger les informations du projet en cours depuis un fichier json.
    def ouvrirProjet(self) -> None:
        with open(self.filePath, "r", encoding="utf-8") as f:
            content = json.load(f)
            self.nom_projet = content["nom_projet"]
            self.auteur = content["auteur"]
            self.date = content["date"]
            self.nom = content["nom"]
            self.magasin = content["magasin"]
            self.liste = content["liste"]
        

    # supprimer le fichier du projet en cours en vérifiant qu'il existe.
    def deleteFile(self) -> None:
        if self.filePath != "" and os.path.exists(self.filePath):
            os.remove(self.filePath)

            self.nom_projet = ""
            self.auteur = ""
            self.date = ""
            self.nom = ""
            self.magasin = ""
            self.liste = []

            self.filePath = ""


    def addProduct(self, product: str) -> None:
        """
        Ajoute un produit à la liste des produits du projet en cours.
        """
        self.liste.append(product)

    def removeProduct(self, product: str) -> None:
        """
        Supprime un produit de la liste des produits du projet en cours.
        """
        self.liste.remove(product)

    def update(self, objet):
        self.nom_projet = objet['nom_projet']
        self.auteur = objet['auteur']
        self.date = objet['date']
        self.nom = objet['nom']
        self.magasin = objet['magasin']
        self.filePath = os.path.dirname(sys.path[0]) + "//Espace_de_travail//" + self.nom_projet+".json"
    
    def setFilePathPlan(self,fname):
        self.filePathPlan = fname
        
    def setFilePath(self,fname):
        self.filePath = fname
        
if __name__ == "__main__":
    # test de la classe SoftwareModel
    print("TEST: class SoftwareModel")
    mon_projet_test = SoftwareModel()
    mon_projet_test.filePath = sys.path[0] + "//projet_test.json"
    mon_projet_test.nom_projet = "Projet de test"
    mon_projet_test.auteur = "Moi"
    mon_projet_test.date = "2021-10-01"
    mon_projet_test.nom = "MonNom"
    mon_projet_test.magasin = "MonMagasin"

    mon_projet = SoftwareModel()

    # avant update
    print("mon_projet :", mon_projet.__dict__)
    mon_projet.update(mon_projet_test)
    # après update
    print("mon_projet :", mon_projet.__dict__)
