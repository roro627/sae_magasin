from PyQt6.QtWidgets import QApplication

import sys,os

from ClientSoftwareModel import ClientSoftwareModel
from ClientSoftwareView import ClientSoftwareView
from PlateauToGraph import *


class ClientSoftwareController:
   def __init__(self) -> None:
      """
      Initialise le contrôleur du logiciel client.
      """

      # Initialiser la vue et le modèle
      self.view = ClientSoftwareView()
      self.model = ClientSoftwareModel()

      # Connecter les signaux de la vue aux slots du contrôleur
      self.view.pathClicked.connect(self.drawPath)
      self.view.openProjectDialog.openClicked.connect(self.openProject)
      self.view.productList.itemAdded.connect(self.newItem)
      self.view.productList.itemDelet.connect(self.itemRemove)
      self.view.productList.itemHovered.connect(self.itemHover)
      self.view.picture.mouseClicked.connect(self.setPoint)
      self.view.unfocus.connect(self.deletRedSquare)
      
   
   def openProject(self, fpath: str) -> None:
      """
      Ouvre un projet.
      Args:
         fpath (str): Le chemin du fichier du projet.
      """
      self.model.setFilePath(fpath)
      self.model.ouvrirProjet()
      self.updateProductList()
      self.view.listShopping.list_widget.clear()
      self.view.picture.setPixmap(self.model.getFullPathImage(),self.model.case_taille,self.model.nombre_cases_x,self.model.nombre_cases_y)
      
   
   def newItem(self, item: str) -> None:
      """
      Ajoute un nouvel élément.
      Args:
         item (str): L'élément à ajouter.
      """
      self.view.listShopping.add_product(item)

   def itemRemove(self, item: str) -> None:
      """
      Supprime un élément.
      Args:
         item (str): L'élément à supprimer.
      """
      self.view.listShopping.remove_product(item)
   
   def updateProductList(self) -> None:
      """
      Met à jour la liste des produits.
      """
      self.view.productList.updateAvailableProducts(self.model.getProducts())
   
   def itemHover(self, item: str) -> None:
        """
        Gère l'événement de survol d'un élément.
        Args:
           item (str): L'élément survolé.
        """
        # Effacer l'ancien produit
        old_graphic_item = self.model.getOldGraphicItem()
        if old_graphic_item is not None:
            self.view.picture.clearProduct(old_graphic_item)
        
        # Dessiner le nouveau produit
        new_graphic_item = self.view.picture.drawProduct(self.model.getProductPosition(item),self.model.position_grille,self.model.case_taille,self.model.nombre_cases_x,self.model.nombre_cases_y)
        
        # Mettre à jour l'ancien élément 
        self.model.setOldGraphicItem(new_graphic_item)
      
   def deletRedSquare(self):
      """
      Cette méthode permet de supprimer le carré rouge qui indique qu'un produit a été survolé.
        
      Paramètres :self (ClientSoftwareController) : L'instance de la classe.
      Return :None
      """
      old_graphic_item = self.model.getOldGraphicItem()
      if old_graphic_item is not None:
         self.view.picture.clearProduct(old_graphic_item)
         self.model.setOldGraphicItem(None)
      
   def setPoint(self,pos: tuple[int,int]) -> None:
      """
      Cette méthode permet de définir un point de départ ou d'arrivée sur l'image.
      
      Paramètres:
         pos (tuple[int,int]): Les coordonnées du point.
      """
      pos = self.model.getIndex(pos)
      if self.view.start_point:
         self.view.setStartPoint(str(pos))
         self.model.setStartPoint(pos)
      elif self.view.end_point:
         self.view.setEndPoint(str(pos))
         self.model.setEndPoint(pos)
      self.view.resetPoint()
        
   def drawPath(self) -> None:
      """
      Dessine le chemin entre le point de départ et le point d'arrivée en passant par chaque produit de la liste de course.
      
      Paramètres:
         start (tuple[int, int]): Le point de départ.
         end (tuple[int, int]): Le point d'arrivée.
      """
      shoppingList = self.view.listShopping.get_products()
      path = self.model.getFinalPath(self.model.start_point, self.model.end_point,shoppingList)
      
      old_path_item = self.model.getOldpathItem()
      if old_path_item is not None:
         self.view.picture.clearProduct(old_path_item)
      newPathItem = self.view.picture.drawPath(path,self.model.position_grille,self.model.case_taille,self.model.nombre_cases_x,self.model.nombre_cases_y)
      self.model.setOldpathItem(newPathItem)
      
   def show(self) -> None:
      """
      Affiche la vue.
      """
      self.view.show()
      
if __name__ == '__main__':
   
   with_Test = False
   
   app = QApplication(sys.argv)
   controller = ClientSoftwareController()
   
   controller.openProject(r"C:\Users\romai\Documents\MEGA\ecole\semestre_2\sae\sae_magasin\github\sae_magasin\Espace_de_travail\demonstration ajout map.json")
   
   
   if with_Test:
      # Création d’une liste de course alétoire (minimum 20 produits) pour effectuer les tests
      # (ne coche pas les éléments de la liste de produit dispo du magasin)
      import random
      test_liste_course = []
      controller.openProject(r"c:\Users\romai\Documents\MEGA\ecole\semestre_2\sae\sae_magasin\github\sae_magasin//Espace_de_travail//Test Mag 1.json")
      test_liste_course = controller.model.liste
      # mélange la liste et choisit les 20 derniers éléments
      random.shuffle(test_liste_course)
      test_liste_course = test_liste_course[:20]
      for item in test_liste_course:
         controller.newItem(item)
   
   
   controller.show()
   sys.exit(app.exec())