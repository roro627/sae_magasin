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
        Ouvre le projet.
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
        Ajoute un produit à la liste des produits du projet en cours.
        Args:
            product (str): Le produit à ajouter.
        """
        self.liste.append(product)

    def removeProduct(self, product: str) -> None:
        """
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
        """
        full_path = self.parent_directory + "//Exemples de plans//" + self.filePathPlan
        return full_path
    
    def detectPositionProduct(self, product: str) -> tuple[int, int]:
        """
        Détecte la position d'un produit.
        Args:
            product (str): Le produit à détecter.
        Returns:
            tuple[int, int]: La position du produit.
        """
        for i in range(len(self.position_produit)):
            for j in range(len(self.position_produit[i])):
                testProduct = self.position_produit[i][j]
                if testProduct != 0 and product in testProduct:
                    return (i, j)
                
    def getProductPosition(self, product: str) -> tuple[int, int]:
        """
        Obtient la position d'un produit.
        Args:
            product (str): Le produit dont on veut obtenir la position.
        Returns:
            tuple[int, int]: La position du produit.
        """
        for i in range(len(self.position_produit)):
            for j in range(len(self.position_produit[i])):
                testProduct = self.position_produit[i][j]
                if testProduct != 0 and product in testProduct:
                    return (i, j)
                
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
       
    def __str__(self) -> str:
        """
        Renvoie une représentation sous forme de chaîne de caractères du modèle.
        Returns:
            str: La représentation sous forme de chaîne de caractères.
        """
        string = "Nom du projet : " + self.nom_projet + "\n" + "Auteur(s) : " + self.auteur + "\n" + "Date : " + str(self.date) + "\n" + "Nom du magasin : " + self.nom + "\n" + "Addresse du magasin : " + self.magasin + "\n" + "Liste des produits : " + str(self.liste) + "\n" + "Position des produits : " + str(self.position_produit) + "\n" + "Position de la grille : " + str(self.position_grille) + "\n" + "Chemin du plan : " + self.filePathPlan + "\n" + "Chemin du fichier : " + self.filePath + "\n"
        return string