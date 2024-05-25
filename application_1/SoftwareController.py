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
        
        self.view.dial.finishButtonClicked.connect(self.nouveauProjet)
        self.view.openProjectDialog.openClicked.connect(self.ouvrirProjet)
        self.view.deletProjectDialog.deletClicked.connect(self.supprimerProjet)
        self.view.saveClicked.connect(self.enregistrerProjet)
        
        self.view.sliderMoved.connect(self.updateGrid)
        self.view.grid.mouseClicked.connect(self.mouseItemGrid)
        
        self.view.pr.itemAdded.connect(self.newItem)
        self.view.pr.itemDelet.connect(self.itemRemove)
        
        self.view.dial.planButtonClicked.connect(self.nouveauPlanProjet)
                

    def newItem(self, item):
        self.model.addProduct(item)
        self.updateProductList()

    def itemRemove(self, item):
        self.model.removeProduct(item)
        self.updateProductList()

    def nouveauPlanProjet(self,fname):
        self.model.setFilePathPlan(fname)
    
    def mouseItemGrid(self,pos):
        self.grid_model.addItems(self.view.product.list_checked_items,pos)
        self.view.product.set_Unchecked_Items()
        self.view.product.clear_Checked_Items()

    def nouveauProjet(self):
        # Gérer l'action nouveau projet
        info = self.view.dial.getAllInfo()
        self.model.update(info)
        self.view.grid.setPixmap(self.model.getFullPathImage())
        self.grid_model.updateGrid(self.view.grid.pixmap_height,self.view.grid.pixmap_width)
        self.view.grid.createGrid(50)
        self.enregistrerProjet()

    def ouvrirProjet(self, fname):
        # Gérer l'action ouvrir projet
        self.model.setFilePath(fname)
        self.model.ouvrirProjet()
        self.view.grid.setPixmap(self.model.getFullPathImage())
        self.grid_model.updateGrid(self.view.grid.pixmap_height,self.view.grid.pixmap_width)
        self.view.grid.createGrid(50)
        products = self.model.getProducts()
        self.view.product.update_Product(products)
        self.view.pr.updateCheckbox(products)

    def supprimerProjet(self, fname):
        # Gérer l'action supprimer projet
        self.model.setFilePath(fname)
        self.model.supprimerProjet()
        self.updateProductList()

    def enregistrerProjet(self):
        # Gérer l'action enregistrer projet
        self.model.enregistrerProjet()

    def updateProductList(self):
        products = self.model.getProducts()
        self.view.product.update_Product(products)
    
    def updateGrid(self,size):
        if self.model.filePathPlan != "":
            self.grid_model.updateSquareSize(size)
            self.view.grid.createGrid(size)

    def show(self):
        # Afficher la vue
        self.view.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    controller = SoftwareController()
    controller.show()

    sys.exit(app.exec())
