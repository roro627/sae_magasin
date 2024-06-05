import os
import json
import sys
from PyQt6.QtCore import QDate
from PlateauToGraph import main as PlateauToGraph

class ClientSoftwareModel:
    def __init__(self) -> None:
        """
        Initialise le modèle du logiciel client.
        """
        self.nom_projet: str = ""
        self.auteur: str = ""
        self.date: QDate = QDate(0, 0, 0)
        self.nom: str = ""
        self.magasin: str = ""
        self.liste: list[str] = []
        self.position_produit: list = []
        self.position_grille: dict = {}
        self.productHovered: str = ""

        self.case_taille: int = 0
        self.nombre_cases_x: int = 0
        self.nombre_cases_y: int = 0
        
        self.filePathPlan: str = ""
        self.filePath: str = ""
        
        current_directory = sys.path[0]
        self.parent_directory = os.path.dirname(current_directory)
        
    def ouvrirProjet(self) -> None:
        """
<<<<<<< HEAD
        Ouvre le projet.
=======
        Cette méthode permet d'ouvrir un projet à partir du fichier JSON spécifié et met à jour les données du modèle.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
        Return:None
>>>>>>> 9cc8c83ed9f27f5f73bf2c47bc0c910c99752554
        """
        with open(self.filePath, "r", encoding="utf-8") as f:
            content = json.load(f)
            self.nom_projet = content["nom_projet"]
            self.auteur = content["auteur"]
            self.date = content["date"]
            self.nom = content["nom"]
            self.magasin = content["magasin"]
            self.liste = content["liste"]
            self.position_produit = content["position_produit"]
            self.case_taille = content["case_taille"]
            self.filePathPlan = content["fichier_plan_chemin"]
            self.position_grille = content["position_grille"]
            self.nombre_cases_x = len(self.position_produit[0])
            self.nombre_cases_y = len(self.position_produit)
            
    def addProduct(self, product: str) -> None:
        """
<<<<<<< HEAD
        Ajoute un produit à la liste des produits du projet en cours.
        Args:
            product (str): Le produit à ajouter.
=======
        Cette méthode permet d'ajouter un produit à la liste des produits du projet en cours.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
                    product (str) : Le nom du produit à ajouter.
        Return:None
>>>>>>> 9cc8c83ed9f27f5f73bf2c47bc0c910c99752554
        """
        self.liste.append(product)

    def removeProduct(self, product: str) -> None:
        """
<<<<<<< HEAD
        Supprime un produit de la liste des produits du projet en cours.
        Args:
            product (str): Le produit à supprimer.
        """
        self.liste.remove(product)

    def setFilePathPlan(self, fname: str) -> None:
        """
        Définit le chemin du fichier du plan.
        Args:
            fname (str): Le chemin du fichier.
        """
        self.filePathPlan = fname
        
    def setFilePath(self, fname: str) -> None:
        """
        Définit le chemin du fichier.
        Args:
            fname (str): Le chemin du fichier.
        """
        self.filePath = fname
       
    def getProducts(self) -> list[str]:
        """
        Renvoie la liste des produits.
        Returns:
            list[str]: La liste des produits.
        """
        return self.liste
       
    def getFullPathImage(self) -> str:
        """
        Renvoie le chemin complet de l'image.
        Returns:
            str: Le chemin complet de l'image.
=======
        Cette méthode permet de supprimer un produit de la liste des produits du projet en cours.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
                    product (str) : Le nom du produit à supprimer.
        Return:None
        """
        self.liste.remove(product)

    
    def setFilePathPlan(self,fname):
        """
        Cette méthode permet de définir le chemin du fichier de plan.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
                    fname (str) : Le chemin du fichier de plan.
        Return:None
        """
        self.filePathPlan = fname
        
    def setFilePath(self,fname):
        """
        Cette méthode permet de définir le chemin du fichier.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
                    fname (str) : Le chemin du fichier.
        Return:None
        """
        self.filePath = fname
       
    def getProducts(self):
        """
        Cette méthode permet de récupérer la liste des produits du projet en cours.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
        Return:list[str] : La liste des produits.
        """
        return self.liste
       
    def getFullPathImage(self):
        """
        Cette méthode permet de récupérer le chemin complet de l'image du plan.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
        Return:full_path (str) : Le chemin complet de l'image.
>>>>>>> 9cc8c83ed9f27f5f73bf2c47bc0c910c99752554
        """
        full_path = self.parent_directory + "//Exemples de plans//" + self.filePathPlan
        return full_path
    
<<<<<<< HEAD
    def detectPositionProduct(self, product: str) -> tuple[int, int]:
        """
        Détecte la position d'un produit.
        Args:
            product (str): Le produit à détecter.
        Returns:
            tuple[int, int]: La position du produit.
=======
    def detectPositionProduct(self,product):
        """
        Cette méthode permet de déterminer la position d'un produit dans la grille.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
                    product (str) : Le nom du produit à localiser.
        Return:tuple[int, int] : Les coordonnées (x, y) du produit dans la grille.
>>>>>>> 9cc8c83ed9f27f5f73bf2c47bc0c910c99752554
        """
        for i in range(len(self.position_produit)):
            for j in range(len(self.position_produit[i])):
                testProduct = self.position_produit[i][j]
                if testProduct != 0 and product in testProduct:
                    return (i, j)
                
<<<<<<< HEAD
    def getProductPosition(self, product: str) -> tuple[int, int]:
        """
        Obtient la position d'un produit.
        Args:
            product (str): Le produit dont on veut obtenir la position.
        Returns:
            tuple[int, int]: La position du produit.
=======
    def getProductPosition(self,product):
        """
        Cette méthode permet de récupérer la position d'un produit dans la grille.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
                    product (str) : Le nom du produit.
        Return:tuple[int, int] : Les coordonnées (x, y) du produit dans la grille.
>>>>>>> 9cc8c83ed9f27f5f73bf2c47bc0c910c99752554
        """
        for i in range(len(self.position_produit)):
            for j in range(len(self.position_produit[i])):
                testProduct = self.position_produit[i][j]
                if testProduct != 0 and product in testProduct:
                    return (i, j)
                
<<<<<<< HEAD
    def getFinalPath(self, start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Obtient le chemin final.
        Args:
            start (tuple[int, int]): Le point de départ.
            end (tuple[int, int]): Le point d'arrivée.
        Returns:
            list[tuple[int, int]]: Le chemin final.
        """
        return PlateauToGraph(self.position_produit, self.liste, start, end)
=======
    def getFinalPath(self,start,end):
        """
        Cette méthode permet de calculer le chemin final à partir du point de départ et du point d'arrivée dans la grille.
        
        Paramètres :self (ClientSoftwareModel) : L'instance de la classe.
                    start (tuple[int, int]) : Les coordonnées (x, y) du point de départ.
                    end (tuple[int, int]) : Les coordonnées (x, y) du point d'arrivée.
        Return:str : Le chemin final calculé.
        """
        return PlateauToGraph(self.position_produit,self.liste,start,end)
>>>>>>> 9cc8c83ed9f27f5f73bf2c47bc0c910c99752554
       
    def __str__(self) -> str:
        """
        Renvoie une représentation sous forme de chaîne de caractères du modèle.
        Returns:
            str: La représentation sous forme de chaîne de caractères.
        """
        string = "Nom du projet : " + self.nom_projet + "\n" + "Auteur(s) : " + self.auteur + "\n" + "Date : " + str(self.date) + "\n" + "Nom du magasin : " + self.nom + "\n" + "Addresse du magasin : " + self.magasin + "\n" + "Liste des produits : " + str(self.liste) + "\n" + "Position des produits : " + str(self.position_produit) + "\n" + "Position de la grille : " + str(self.position_grille) + "\n" + "Chemin du plan : " + self.filePathPlan + "\n" + "Chemin du fichier : " + self.filePath + "\n"
        return string