from PyQt6.QtCore import QObject, pyqtSlot
from SoftwareModel import SoftwareModel
from SoftwareView import SoftwareView
from GridModel import GridModel
from PyQt6.QtWidgets import QApplication
import sys


class SoftwareController():
    def __init__(self):

        # Initialiser la vue et le modèle
        self.view = SoftwareView()
        self.model = SoftwareModel()
        self.grid_model = GridModel()

        # Connecter les signaux de la vue aux slots du contrôleur

        # -------------- Signaux de View -------------- #
        self.view.sliderMoved.connect(self.updateGrid)
        self.view.confGridClicked.connect(self.confGridBegin)
        self.view.confGridFinishClicked.connect(self.confGridEnd)
        self.view.placementClicked.connect(self.productListEnabled)

        # -------------- Signaux de View.pr -------------- #
        self.view.pr.itemAdded.connect(self.newItem)
        self.view.pr.itemDelet.connect(self.itemRemove)
        
        # -------------- Signaux de View.dial -------------- #
        self.view.dial.finishButtonClicked.connect(self.nouveauProjet)
        self.view.dial.planButtonClicked.connect(self.nouveauPlanProjet)

        # -------------- Signaux de View.openProjectDialog -------------- #
        self.view.openProjectDialog.openClicked.connect(self.ouvrirProjet)

        # -------------- Signaux de View.saveClicked -------------- #
        self.view.saveClicked.connect(self.enregistrerProjet)

        # -------------- Signaux de View.deletProjectDialog -------------- #
        self.view.deletProjectDialog.deletClicked.connect(self.supprimerProjet)

        # -------------- Signaux de View.grid -------------- #
        self.view.grid.mouseClicked.connect(self.mouseItemGrid)

    # --- Méthodes pour View --- #
    def updateGrid(self,size):
        if self.model.filePathPlan != "":
            self.grid_model.updateSquareSize(size)
            self.grid_model.updateGrid(self.view.grid.pixmap_height,self.view.grid.pixmap_width)
            self.view.grid.createGrid(size,self.model.gridConfigured,self.grid_model.gridStart)
            
    def confGridBegin(self):
        self.view.slider.setEnabled(True)
        self.view.btn2.setEnabled(True)
        self.view.btn3.setEnabled(False)
        self.view.btn1.setEnabled(False)
        self.model.gridConfigured = True
        self.view.grid.gridIsMovable()
    
    def confGridEnd(self):
        self.view.btn1.setEnabled(False)
        self.view.btn2.setEnabled(False)
        self.view.btn3.setEnabled(True)
        self.view.slider.setEnabled(False)
        self.model.gridConfiguredFinish = True
        self.view.grid.gridIsNotMovable()
    
    def productListEnabled(self):
        self.model.itemsPlaced = True
        self.view.btn1.setEnabled(False)
        self.view.pr.setEnabled(True)

    # --- Méthodes pour View.pr --- #
    def newItem(self, item):
        self.model.addProduct(item)
        self.updateProductList()

    def itemRemove(self, item):
        self.model.removeProduct(item)
        self.updateProductList()
    
    def updateProductList(self):
        products = self.model.getProducts()
        self.view.product.update_Product(products)

    # --- Méthodes pour View.dial --- #
    def nouveauProjet(self):
        # Gérer l'action nouveau projet
        info = self.view.dial.getAllInfo()
        self.model.update(info)

        self.view.grid.setPixmap(self.model.getFullPathImage())
        self.grid_model.updateGrid(self.view.grid.pixmap_height,self.view.grid.pixmap_width)
        self.view.grid.createGrid(self.view.slider.value()*10,self.grid_model.gridMoved,self.grid_model.gridStart)
        self.view.btn1.setEnabled(True)
        self.view.btn3.setEnabled(True)
        self.enregistrerProjet()

    def nouveauPlanProjet(self,fname):
        self.model.setFilePathPlan(fname)
    
    # --- Méthodes pour View.openProjectDialog --- #
    def ouvrirProjet(self, fname):
        # Gérer l'action ouvrir projet
        self.model.setFilePath(fname)
        self.model.ouvrirProjet()
        self.view.grid.setPixmap(self.model.getFullPathImage())

        self.grid_model.grid_position = self.model.position_produit
        self.grid_model.gridStart = self.model.position_grille
        self.grid_model.square_size = self.model.case_taille

        self.grid_model.updateGrid(self.view.grid.pixmap_height,self.view.grid.pixmap_width)
        self.view.grid.createGrid(self.grid_model.square_size,self.grid_model.gridMoved,self.model.position_grille)

        # Configuration des bouttons en fonction de l'état d'avancement du projet.
        if self.model.itemsPlaced : self.productListEnabled()
        elif self.model.gridConfiguredFinish : self.confGridEnd()
        elif self.model.gridConfigured : self.confGridBegin()
        else : self.view.btn1.setEnabled(True), self.view.btn3.setEnabled(True)

        products = self.model.getProducts()
        self.view.product.update_Product(products,self.model.getPlacedProducts())
        self.grid_model.grid_position = self.model.position_produit
        self.view.pr.updateCheckbox(products)

    # --- Méthodes pour View.deletProjectDialog --- #
    def enregistrerProjet(self):
        # Gérer l'action enregistrer projet

        self.model.position_produit = self.grid_model.grid_position
        self.model.position_grille = self.grid_model.gridStart
        self.model.case_taille = self.grid_model.square_size

        self.model.enregistrerProjet()
    
    # --- Méthodes pour View.deletProjectDialog --- #
    def supprimerProjet(self, fname):
        # Gérer l'action supprimer projet
        self.model.setFilePath(fname)
        self.model.supprimerProjet()
        self.updateProductList()
    
    # --- Méthodes pour View.grid --- #
    def mouseItemGrid(self,pos):
        if self.model.gridConfigured and not self.model.gridConfiguredFinish:
            print("Bougement de la grille")
            self.grid_model.gridMoved = True
            self.grid_model.gridStart = (self.view.grid.group.pos().x(),self.view.grid.group.pos().y())
        self.grid_model.addItems(self.view.product.list_checked_items,pos)
        self.model.position_produit = self.grid_model.grid_position
        self.view.product.set_Unchecked_Items()
        self.view.product.clear_Checked_Items()
    
    def show(self):
        # Afficher la vue
        self.view.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    controller = SoftwareController()
    controller.show()

    sys.exit(app.exec())
