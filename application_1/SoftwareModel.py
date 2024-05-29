import os, json, sys, PyQt6.QtCore

# -----------------------------------------------------------------------------
# --- class Model
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
        self.position_produit: dict = {}
        self.position_grille: dict = {}

        self.filePathPlan : str = ""
        self.filePath: str = ""

        self.gridConfigured : bool = False
        self.gridConfiguredFinish : bool = False
        self.itemsPlaced : bool = False
        
        current_directory = sys.path[0]
        self.parent_directory = os.path.dirname(current_directory)

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
                "position_produit": self.position_produit,
                "position_grille": self.position_grille,

                "fichier_plan_chemin": self.filePathPlan,
                "fichier_chemin": self.filePath,

                "grille_configure": self.gridConfigured,
                "grille_configure_finit": self.gridConfiguredFinish,
                "elements_places": self.itemsPlaced

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
            self.position_produit = content["position_produit"]
            self.filePathPlan = content["fichier_plan_chemin"]
            self.gridConfigured = content["grille_configure"]
            self.gridConfiguredFinish = content["grille_configure_finit"]
            self.itemsPlaced = content["elements_places"]
        

    # supprimer le fichier du projet en cours en vérifiant qu'il existe.
    def supprimerProjet(self) -> None:
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
        self.filePath = self.parent_directory + "//Espace_de_travail//" + self.nom_projet+".json"
    
    def setFilePathPlan(self,fname):
        self.filePathPlan = fname
        
    def setFilePath(self,fname):
        self.filePath = fname
       
    def getProducts(self):
        return self.liste
       
    def getFullPathImage(self):
        full_path = self.parent_directory + "//Exemples de plans//" + self.filePathPlan
        return full_path
       
    def getPlacedProducts(self):
        listProducts = []
        for i in range(len(self.position_produit)):
            for j in range(len(self.position_produit[i])):
                testProduct = self.position_produit[i][j]
                if testProduct != 0:
                    for j in testProduct:
                        listProducts.append(j)
        return listProducts
       
    def toString(self) -> str:
        string = "Nom du projet : " + self.nom_projet + "\n" + "Auteur(s) : " + self.auteur + "\n" + "Date : " + str(self.date) + "\n" + "Nom du magasin : " + self.nom + "\n" + "Addresse du magasin : " + self.magasin + "\n"
        return string
        
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
