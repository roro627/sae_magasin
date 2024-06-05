from PyQt6.QtWidgets import QApplication

import sys,os

from ClientSoftwareModel import ClientSoftwareModel
from ClientSoftwareView import ClientSoftwareView
from PlateauToGraph import *

"""
TODO Pour tout les fichier:
- ouvir un fichier json grace à openproject et update le model
   - implémenter la méthode openProject et supprimer le systeme actuel. fait
   - dans l'update mettre à jour le model.fait et les widgets. fait
- relier la liste de course à chaque sélection de produit dans la liste de produit dispo du magasin. fait
- afficher un point sur chaque position de produit sélectionné dans la liste de course
- supprimer un point sur chaque position de produit désélectionné dans la liste de course
- implémenter dijkstra pour trouver le plus court chemin. plus ou moins fait
- afficher le chemin sur l'image.
- Detecter le survol d'un produit. fait
- Trouver la position du produit survolé. fait
- Afficher un point sur l'image lors du survol d'un produit. fait
"""

class ClientSoftwareController:
   def __init__(self) -> None:
      """
      Initialise le contrôleur du logiciel client.
      """

      # Initialiser la vue et le modèle
      self.view = ClientSoftwareView()
      self.model = ClientSoftwareModel()

      # Connecter les signaux de la vue aux slots du contrôleur
      self.view.pathClicked.connect(self.pathDraw)
      self.view.openProjectDialog.openClicked.connect(self.openProject)
      self.view.productList.itemAdded.connect(self.newItem)
      self.view.productList.itemDelet.connect(self.itemRemove)
      self.view.productList.itemHovered.connect(self.itemHover)
      
   
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
        
   def drawPath(self, start: tuple[int, int], end: tuple[int, int]) -> None:
      """
      Dessine le chemin.
      Args:
         start (tuple[int, int]): Le point de départ.
         end (tuple[int, int]): Le point d'arrivée.
      """
      path = self.model.getFinalPath(start,end)
      self.view.picture.drawPath(path,self.model.position_grille,self.model.case_taille,self.model.nombre_cases_x,self.model.nombre_cases_y)
      
   
   def pathDraw(self):
      """
      Cette méthode permet de générer et dessiner le chemin optimisé pour récupérer les produits dans le plateau.
        
      Paramètres :self (ClientSoftwareController) : L'instance de la classe.
      Return :None
      """
      plateau2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, ["Rosbeef"], ["R\u00f4ti de veau"], 0, 0, ["Magret de canard"], 0, ["Foie gras"], 0, ["Chorizo"], 0, ["Surimi"], 0, 0, 0, 0, 0, 0, 0, ["Gingembre"], 0, 0, 0, ["Flageolets"], ["Germe de soja"], 0, 0, 0, 0], [0, 0, 0, 0, 0, ["R\u00f4ti de porc"], ["R\u00f4ti fum\u00e9"], 0, 0, ["Merguez"], 0, ["G\u00e9siers de canard"], 0, ["Cordon bleu"], 0, ["Agneau"], 0, 0, 0, 0, 0, 0, 0, ["Haricot"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Fenouil"], 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, ["Wings poulet"], ["Viande des grisons"], 0, ["Steak hach\u00e9"], 0, 0, ["Mortadelle"], 0, ["Grenouille (cuisses)"], 0, 0, ["C\u00f4te de boeuf"], 0, ["Aiguillette de boeuf"], 0, ["Coquille St-Jacques"], 0, 0, ["Salsifis"], 0, ["Poivron"], 0, 0, 0, ["\u00c9chalote", "\u00c9pinards"], ["Endive"], 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, ["Saucisson sec"], 0, 0, ["Mousse de foie"], 0, ["Hamburger"], 0, 0, ["C\u00f4telettes d'agneau"], 0, ["Aiguillette de poulet"], 0, ["Crabe"], 0, 0, ["Tomate"], 0, ["Pois mangetout"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, ["Mouton"], 0, ["Hot-dog"], 0, 0, ["C\u00f4tes de porc"], 0, ["Andouille"], 0, ["Crevettes"], 0, 0, ["Topinambour"], 0, ["Pois gourmand"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, ["Veau"], ["Tripes"], 0, ["Saucisson \u00e0 l'ail"], 0, 0, ["Museau de porc"], 0, ["Jambon cru"], 0, 0, ["C\u00f4tes de veau"], 0, ["Andouillette"], 0, ["\u00c9crevisses"], 0, 0, ["Bigorneaux"], 0, ["Poireau"], 0, 0, 0, ["Chou-rouge"], 0, ["Ciboulette"], 0, 0, 0], [0, 0, 0, 0, 0, 0, ["Saucisses"], 0, 0, ["Nuggets"], 0, ["Jambon cuit"], 0, 0, ["Croc's jambon"], 0, ["Bacon"], 0, ["Encornet"], 0, 0, ["Cabillaud"], 0, ["Petits pois"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, ["P\u00e2t\u00e9 de campagne"], 0, ["Jambon de volaille"], 0, 0, ["Cuisses poulet r\u00f4ti"], 0, ["Bavette (boeuf)"], 0, ["Gambas"], 0, 0, ["Colin"], 0, ["Persil"], 0, 0, 0, ["Choucroute"], 0, ["Chou-fleur"], 0, 0, 0], [0, 0, 0, ["Saucisse de Toulouse"], ["Salami"], ["Rumsteck"], ["Bl\u00e9 dur"], 0, 0, ["P\u00e2t\u00e9 de foie"], 0, ["Jambon fum\u00e9"], 0, 0, ["Dinde"], 0, ["Bifteck de boeuf"], 0, ["Hareng fum\u00e9"], 0, 0, ["Coques"], 0, ["Palmier (coeur)"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Chou de Bruxelles"], 0, ["Chou"], 0, 0, 0], [0, 0, 0, ["Bouillon cube"], ["Boulgour"], ["Cannelle"], ["Chapelure"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, ["P\u00e2t\u00e9 de t\u00eate"], 0, ["Jambonneau"], 0, 0, ["\u00c9chine de porc"], 0, ["Boeuf (entrec\u00f4te)"], 0, ["Homard"], 0, 0, ["Salade compos\u00e9e"], 0, ["Oignons"], 0, 0, 0, ["Citrouille"], ["Coeur de palmier"], 0, 0, 0, 0], [0, 0, 0, ["Coriandre"], 0, 0, ["Cornichons"], 0, 0, ["Paupiettes de veau"], 0, ["Jarret"], 0, 0, ["Escalope de veau"], 0, ["Burgers"], 0, ["Hu\u00eetres"], 0, 0, ["Salade laitue"], 0, ["Navet"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, ["Petit sal\u00e9"], 0, ["Langue"], 0, 0, ["Faux-filet (boeuf)"], 0, ["Caille"], 0, ["Langoustine"], 0, 0, ["Radis noir"], 0, ["Menthe"], 0, 0, 0, ["Concombre"], ["Courge"], 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, ["Pigeon"], 0, ["Lapin"], 0, 0, ["Filet de poulet"], 0, ["Canard"], 0, ["Maquereaux"], 0, 0, ["Radis"], 0, ["Ma\u00efs"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, ["Cro\u00fbton"], 0, 0, ["Curry"], 0, 0, ["Pintade", "Poitrine de porc"], 0, ["Lard"], 0, 0, ["Filet mignon"], 0, ["Cervelas"], 0, ["Moules"], 0, 0, ["Pousses de bambou"], 0, ["M\u00e2che"], 0, 0, 0, ["Courgette"], ["Cresson"], 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, ["Poulet"], 0, ["Lard fum\u00e9"], 0, 0, ["Foie"], 0, ["Chair \u00e0 saucisse"], 0, ["Poissons eau douce"], 0, 0, ["Potimarron"], 0, ["Mac\u00e9doine"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, ["Farine"], 0, 0, ["Graine de s\u00e9same"], 0, 0, ["Rillettes"], 0, ["Lardons"], 0, 0, ["Foie de volaille"], 0, ["Chipolatas"], 0, ["Poissons mer"], 0, 0, ["Pomme de terre"], 0, ["Lentilles"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, ["Poulpe"], ["Poissons pan\u00e9s"], 0, 0, 0, 0, 0, 0, 0, 0, ["Champignons"], 0, ["C\u00e9leri"], ["Blette"], 0, ["Betterave"], 0, 0, ["Asperges"], 0, ["Artichaut"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Champignons chinois"], 0, ["Brocolis"], ["Carotte"], 0, 0, 0, ["Avocat"], ["Aubergine"], 0, ["Ail"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Sardines"], ["Saumon"], ["Saumon fum\u00e9"], ["Soupe de poissons"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
      plateau2_produit = ["Asperges", "C\u00e9leri", "Champignons", "Chou", "Chou de Bruxelles", "Chou-rouge", "Ciboulette", "Citrouille", "Coeur de palmier", "Courge", "Courgette", "Cresson", "\u00c9chalote", "Fenouil", "Germe de soja", "Gingembre", "Haricot", "Lentilles", "Mac\u00e9doine", "M\u00e2che", "Ma\u00efs", "Menthe", "Navet", "Oignons", "Pois gourmand", "Pois mangetout", "Pomme de terre", "Potimarron", "Pousses de bambou", "Salsifis", "Poissons pan\u00e9s", "Moules", "Maquereaux", "Hareng fum\u00e9", "Gambas", "Encornet", "crevisses", "Crabe", "Andouille", "Andouillette", "Bavette (boeuf)", "Canard", "Cervelas", "Chair \u00e0 saucisse", "Paprika", "Oyster sauce", "Origan", "Cro\u00fbton", "Cannelle", "Boulgour", "Bl\u00e9 dur", "Riz", "Quinoa", "Pois chiches", "Abricots secs", "Amandes", "Beurre de cacahu\u00e8te", "Dattes", "Figues s\u00e8ches", "Gingembre confit", "Brugnon", "Cassis", "Cl\u00e9mentine", "Framboise", "Groseille", "Biscuite", "Brioche", "Cacao", "Caf\u00e9 en grains", "Quenelles", "Pizzas", "Pi\u00e9montaise", "P\u00e2tes \u00e0 tarte", "Galettes", "Foie gras", "Cr\u00e8me dessert", "Fromage blanc", "Margarine", "Compote", "Gaspacho", "Haricots vert", "Ma\u00efs", "Fruits secs", "Chips", "Bi\u00e8re", "Alcools fort", "Eau min\u00e9rale", "Bougies", "Cure dents", "D\u00e9tachant", "Gants de m\u00e9nage", "Mouchoirs", "Couches b\u00e9b\u00e9", "Cr\u00e8me main", "D\u00e9maquillant", "Dentifrice", "Fil dentaire", "Gel douche", "Gel spray", "Calculatrice", "Ciseau \u00e0 papier", "Colle", "Crayons de couleur", "Encre Imprimante", "Papier \u00e0 lettre", "Foins"]
      
      coordonneProducts = findPostionsProducts(plateau2_produit, plateau2)
      
      produit_regrouper = regroupProducts(coordonneProducts)
      
      sortGroupProduct(produit_regrouper)
      
      optimizedPath = sortGroup(produit_regrouper, (1, 5), (27, 5))
      
      finalPath = makeFinalPath(plateau2, optimizedPath)

      self.view.picture.drawPath(finalPath,self.model.position_grille,self.model.case_taille,self.model.nombre_cases_x,self.model.nombre_cases_y)
   
   def show(self) -> None:
      """
      Affiche la vue.
      """
      self.view.show()
      
if __name__ == '__main__':
   
   with_Test = False
   
   app = QApplication(sys.argv)
   controller = ClientSoftwareController()
   
   if with_Test:
      # Création d’une liste de course alétoire (minimum 20 produits) pour effectuer les tests
      # (ne coche pas les éléments de la liste de produit dispo du magasin)
      import random
      test_liste_course = []
      controller.openProject(r"c:\Users\romai\Documents\MEGA\ecole\semestre_2\sae\sae_magasin\github\sae_magasin//Espace_de_travail//Test Mag 1.json")
      test_liste_course = controller.model.liste
      random.shuffle(test_liste_course)
      test_liste_course = test_liste_course[:20]
      for item in test_liste_course:
         controller.newItem(item)
   
   
   controller.show()
   sys.exit(app.exec())