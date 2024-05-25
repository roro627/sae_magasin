import os, json, sys, PyQt6.QtCore

class ClientSoftwareModel():
    
    def __init__(self) -> None:

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
        
        current_directory = sys.path[0]
        self.parent_directory = os.path.dirname(current_directory)
        
    def ouvrirProjet(self) -> None:
        with open(self.filePath, "r", encoding="utf-8") as f:
            content = json.load(f)
            self.nom_projet = content["nom_projet"]
            self.auteur = content["auteur"]
            self.date = content["date"]
            self.nom = content["nom"]
            self.magasin = content["magasin"]
            self.liste = content["liste"]
            self.filePathPlan = content["fichier_plan_chemin"]
            
    
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
       
    def __str__(self):
        string = "Nom du projet : " + self.nom_projet + "\n" + "Auteur(s) : " + self.auteur + "\n" + "Date : " + str(self.date) + "\n" + "Nom du magasin : " + self.nom + "\n" + "Addresse du magasin : " + self.magasin + "\n" + "Liste des produits : " + str(self.liste) + "\n" + "Position des produits : " + str(self.position_produit) + "\n" + "Position de la grille : " + str(self.position_grille) + "\n" + "Chemin du plan : " + self.filePathPlan + "\n" + "Chemin du fichier : " + self.filePath + "\n"
        return string
    
    
if __name__ == "__main__":
    model = ClientSoftwareModel()
    model.update({"nom_projet":"test","auteur":"test","date":"2021-10-10","nom":"test","magasin":"test"})
    print(model)
    model.ouvrirProjet()
    print(model)
    model.addProduct("test")
    print(model.getProducts())
    model.removeProduct("test")
    print(model.getProducts())
    model.setFilePathPlan("test")
    print(model.getFullPathImage())
    model.setFilePath("test")
    print(model.getFullPathImage())
    model.setFilePath(r"C:\Users\romai\Documents\MEGA\ecole\semestre_2\sae\sae_magasin\github\sae_magasin\Espace_de_travail\test_multi_pc.json")
    model.ouvrirProjet()
    print(model)