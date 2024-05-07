import os,json

# -----------------------------------------------------------------------------
# --- class Outil
# -----------------------------------------------------------------------------

class Outil():
    
    # constructeur
    def __init__(self) -> None:
        
        # attributs
        
        # liste des produits
        self.nom_projet: str = ""
        self.auteur: str = ""
        self.date: str = ""
        self.nom: str = ""
        self.magasin: str = ""
        self.liste: list[str] = []
        
        
        
    def getListe(self) -> list :
        return self.liste
    
    # sauvegarder les informations du projet en cours dans un fichier ecrit en json.
    def saveFile(self,filePath) -> None :
        with open(filePath, 'w') as f:
            content = {"nom_projet": "Projet 1",
                        "auteur": "Moi",
                        "date": "2021-10-01",
                        "nom": "Lambert",
                        "magasin": "Brico",
                        "liste": self.liste}
            json.dump(content, f)
            
    # charger les informations du projet en cours depuis un fichier json.
    def loadFile(self,filePath) -> None :
        with open(filePath, 'r') as f:
            content = json.load(f)
            self.nom_projet = content["nom_projet"]
            self.auteur = content["auteur"]
            self.date = content["date"]
            self.nom = content["nom"]
            self.magasin = content["magasin"]
            self.liste = content["liste"]
            
    # ajouter un produit a la liste des produits du projet en cours.
    def addProduct(self,product) -> None :
        self.liste.append(product)