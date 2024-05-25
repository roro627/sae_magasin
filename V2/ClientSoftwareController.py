from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication

import sys,os

from ClientSoftwareModel import ClientSoftwareModel
from ClientSoftwareView import ClientSoftwareView

"""
TODO Pour tout les fichier:
- ouvir un fichier json grace à openproject et update le model
   - implémenter la méthode openProject et supprimer le systeme actuel. fait
   - dans l'update mettre à jour le model.fait et les widgets. fait
- relier la liste de course à chaque sélection de produit dans la liste de produit dispo du magasin
- afficher un point sur chaque position de produit sélectionné dans la liste de course
- supprimer un point sur chaque position de produit désélectionné dans la liste de course
- implémenter dijkstra pour trouver le plus court chemin
"""

class ClientSoftwareController():
   def __init__(self):

      # Initialiser la vue et le modèle
      self.view = ClientSoftwareView()
      self.model = ClientSoftwareModel()

      # Connecter les signaux de la vue aux slots du contrôleur
      self.view.openProjectDialog.openClicked.connect(self.openProject)
      
      
      
      
      
      
   def openProject(self,fpath):
      self.model.setFilePath(fpath)
      self.model.ouvrirProjet()
      self.updateProductList()
      self.view.picture.setPixmap(self.model.getFullPathImage())
      
      
   def dijkstra():
      pass
   
   def updateProductList(self):
      self.view.productList.updateAvailableProducts(self.model.getProducts())
   
   def show(self):
      self.view.show()
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   controller = ClientSoftwareController()
   controller.show()
   sys.exit(app.exec())