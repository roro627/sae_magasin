import os, json, sys, PyQt6.QtCore

# -----------------------------------------------------------------------------
# --- classe Model
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

        self.position_produit : list = []
        self.position_grille : list = [0,0]
        self.case_taille : int = 50

        self.filePathPlan : str = ""
        self.filePath: str = ""

        self.gridConfigured : bool = False
        self.gridConfiguredFinish : bool = False
        self.itemsPlaced : bool = False
        
        current_directory = sys.path[0]
        self.parent_directory = os.path.dirname(current_directory)

    def enregistrerProjet(self) -> None:
        '''
        Cette méthode permet de sauvegarder les informations du projet en cours dans un fichier écrit en JSON.
    
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        '''
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
                "case_taille": self.case_taille,

                "fichier_plan_chemin": self.filePathPlan,
                "fichier_chemin": self.filePath,

                "grille_configure": self.gridConfigured,
                "grille_configure_finit": self.gridConfiguredFinish,
                "elements_places": self.itemsPlaced

            }
            json.dump(content, f)

    def ouvrirProjet(self) -> None:
        '''
        Cette méthode permet de charger les informations du projet en cours depuis un fichier JSON.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        '''
        with open(self.filePath, "r", encoding="utf-8") as f:
            content = json.load(f)
            self.nom_projet = content["nom_projet"]
            self.auteur = content["auteur"]
            self.date = content["date"]
            self.nom = content["nom"]
            self.magasin = content["magasin"]
            self.liste = content["liste"]
            self.position_produit = content["position_produit"]
            self.position_grille = content["position_grille"]
            self.case_taille = content["case_taille"]
            self.filePathPlan = content["fichier_plan_chemin"]
            self.gridConfigured = content["grille_configure"]
            self.gridConfiguredFinish = content["grille_configure_finit"]
            self.itemsPlaced = content["elements_places"]
        

         
    def supprimerProjet(self) -> None:
        '''
        Cette méthode permet de supprimer le fichier JSON du projet en cours en vérifiant qu'il existe.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        '''
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
        Cette méthode permet d'ajouter un produit à la liste des produits du projet en cours.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    product (String) : Le nom du produit à ajouter.
        Return :None
        """
        self.liste.append(product)

    def removeProduct(self, product: str) -> None:
        """
        Cette méthode permet de supprimer un produit de la liste des produits du projet en cours.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    product (String) : Le nom du produit à supprimer.
        Return :None
        """
        self.liste.remove(product)

    def update(self, objet):
        '''
        Cette méthode permet de mettre à jour toutes les informations du projet en cours.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    objet (dict) : Dictionnaire contenant les informations du projet avec les clés :
                    nom_projet (String), auteur (String), date (String), nom (String), magasin (String).
        Return :None
        '''
        self.nom_projet = objet['nom_projet']
        self.auteur = objet['auteur']
        self.date = objet['date']
        self.nom = objet['nom']
        self.magasin = objet['magasin']
        self.filePath = self.parent_directory + "//Espace_de_travail//" + self.nom_projet+".json"
    
    def setFilePathPlan(self,fname):
        '''
        Cette méthode permet de mettre à jour le chemin vers le plan.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    fname (String) : Le nom du fichier du plan.
        Return :None
        '''
        self.filePathPlan = fname
        
    def setFilePath(self,fname):
        '''
        Cette méthode permet de mettre à jour le chemin vers le fichier JSON.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    fname (String) : Le nom du fichier JSON.
        Return :None
        '''
        self.filePath = fname
       
    def getProducts(self):
        '''
        Cette méthode permet de récupérer la liste des produits du projet en cours.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Retourne :list : La liste des produits (list[String]).
        '''
        return self.liste
       
    def getFullPathImage(self):
        '''
        Cette méthode permet de récupérer le chemin complet vers l'image du projet.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :String : Le chemin complet vers l'image du projet.
        '''
        full_path = self.parent_directory + "//Exemples de plans//" + self.filePathPlan
        return full_path
       
    def getPlacedProducts(self):
        """
        Cette méthode permet de récupérer la liste des produits placés dans le projet.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :list : La liste des produits placés (list[String]).
        """
        listProducts = []
        for i in range(len(self.position_produit)):
            for j in range(len(self.position_produit[i])):
                testProduct = self.position_produit[i][j]
                if testProduct != 0:
                    for j in testProduct:
                        listProducts.append(j)
        return listProducts
       
    def toString(self) -> str:
        """
        Cette méthode permet d'afficher les principaux attributs du projet.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :String : Les principaux attributs du projet sous forme de chaîne de caractères.
        """
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
