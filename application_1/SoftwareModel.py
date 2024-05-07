import os,json,sys

# -----------------------------------------------------------------------------
# --- class Outil
# -----------------------------------------------------------------------------

class projet():
    
    # constructeur
    def __init__(self) -> None:
        
        # attributs
        
        self.nom_projet: str = ""
        self.auteur: str = ""
        # TODO: METTRE TYPE DATE
        self.date = ""
        self.nom: str = ""
        self.magasin: str = ""
        self.liste: list[str] = []
        
        self.filePath:str = ""
        
    
    # sauvegarder les informations du projet en cours dans un fichier ecrit en json.
    def saveFile(self) -> None :
        with open(self.filePath, 'w', encoding='utf-8') as f:
            content = {"nom_projet": self.nom_projet,
                        "auteur": self.auteur,
                        "date": self.date,
                        "nom": self.nom,
                        "magasin": self.magasin,
                        "liste": self.liste}
            json.dump(content, f)
            
    # charger les informations du projet en cours depuis un fichier json.
    def loadFile(self) -> None :
        with open(self.filePath, 'r', encoding='utf-8') as f:
            content = json.load(f)
            self.nom_projet = content["nom_projet"]
            self.auteur = content["auteur"]
            self.date = content["date"]
            self.nom = content["nom"]
            self.magasin = content["magasin"]
            self.liste = content["liste"]
            
    # supprimer le fichier du projet en cours en vérifiant qu'il existe.
    def deleteFile(self) -> None :
        if self.filePath != "" and os.path.exists(self.filePath):
            os.remove(self.filePath)
            
            self.nom_projet = ""
            self.auteur = ""
            self.date = ""
            self.nom = ""
            self.magasin = ""
            self.liste = []
            
            self.filePath = ""
    
            
    # ajouter un produit a la liste des produits du projet en cours.
    def addProduct(self,product) -> None :
        self.liste.append(product)
        
    # supprimer un produit de la liste des produits du projet en cours.
    def removeProduct(self,product) -> None :
        self.liste.remove(product)
        
    
    def update(self,objet):
        self.nom_projet = objet.nom_projet
        self.auteur = objet.auteur
        self.date = objet.date
        self.nom = objet.nom
        self.magasin = objet.magasin
        self.liste = objet.liste
        self.filePath = objet.filePath
    
if __name__ == "__main__":
    # test de la classe Projet
    print('TEST: class Projet')
    mon_projet_test = projet()
    mon_projet_test.filePath = sys.path[0] + '/projet_test.json'
    mon_projet_test.nom_projet = 'Projet de test'
    mon_projet_test.auteur = 'Moi'
    mon_projet_test.date = '2021-10-01'
    mon_projet_test.nom = 'MonNom'
    mon_projet_test.magasin = 'MonMagasin'
    
    mon_projet = projet()
    
    # avant update
    print('mon_projet :', mon_projet.__dict__)    
    mon_projet.update(mon_projet_test)
    # après update
    print('mon_projet :', mon_projet.__dict__)
