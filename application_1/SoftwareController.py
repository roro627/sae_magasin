from SoftwareModel import SoftwareModel
from SoftwareView import SoftwareView
from GridModel import GridModel
from loginDialog import loginDialog
from PyQt6.QtWidgets import QApplication
import sys

# -----------------------------------------------------------------------------
# --- classe Controller
# -----------------------------------------------------------------------------

class SoftwareController():
    def __init__(self):

        # Initialiser la vue et le modèle
        self.login = loginDialog()
        self.view = SoftwareView()
        self.model = SoftwareModel()
        self.grid_model = GridModel()

        # Connecter les signaux de la vue aux slots du contrôleur

        # -------------- Signaux de Login -------------- #
        self.login.loginClicked.connect(self.loginToSoftware)

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
    
    # --- Méthodes pour Login --- #

    def loginToSoftware(self,info):
        if info["username"] == "admin" and info["password"] == "motdepasse":
            self.show()
            self.login.close()
        else :
            self.view.loginError()

    # --- Méthodes pour View --- #
    def updateGrid(self,size):
        """
        Cette méthode permet de mettre à jour la taille de la grille.
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    size (int) : La nouvelle taille de la grille.
        Return :None
        """
        if self.model.filePathPlan != "":
            self.grid_model.updateSquareSize(size)
            self.grid_model.updateGrid(self.view.grid.pixmap_height,self.view.grid.pixmap_width)
            self.view.grid.createGrid(size,self.model.gridConfigured,self.grid_model.gridStart)

    def confGridBegin(self):
        """
        Cette méthode permet de passer en mode "configuration de la grille".
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        """
        self.view.slider.setEnabled(True)
        self.view.btn2.setEnabled(True)
        self.view.btn3.setEnabled(False)
        self.view.btn1.setEnabled(False)
        self.model.gridConfigured = True
        self.view.grid.gridIsMovable()

    def confGridEnd(self):
        """
        Cette méthode permet d'enlever le mode "configuration de la grille".
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        """
        self.view.btn1.setEnabled(False)
        self.view.btn2.setEnabled(False)
        self.view.btn3.setEnabled(True)
        self.view.slider.setEnabled(False)
        self.model.gridConfiguredFinish = True
        self.view.grid.gridIsNotMovable()

    def productListEnabled(self):
        """
        Cette méthode permet d'activer la liste des produits et de désactiver le bouton "placement".
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        """
        self.model.itemsPlaced = True
        self.view.btn1.setEnabled(False)
        self.view.pr.setEnabled(True)

    # --- Méthodes pour View.pr --- #
    def newItem(self, item):
        """
        Cette méthode permet d'ajouter un nouvel élément à la liste des produits.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    item (String) : Le nom du nouvel élément à ajouter.
        Return :None
        """
        self.model.addProduct(item)
        self.updateProductList()

    def itemRemove(self, item):
        """
        Cette méthode permet de supprimer un élément de la liste des produits.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    item (String) : Le nom de l'élément à supprimer.
        Return :None
        """
        self.model.removeProduct(item)
        self.updateProductList()

    # --- Méthodes pour View.dial --- #
    def nouveauProjet(self):
        """
        Cette méthode permet de créer un nouveau projet.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        """
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
        """
        Cette méthode permet d'avoir un nouveau plan pour le projet.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    fname (String) : Le nom du fichier du nouveau plan.
        Return :None
        """
        self.model.setFilePathPlan(fname)
    
    # --- Méthodes pour View.openProjectDialog --- #
    def ouvrirProjet(self, fname):
        """
        Cette méthode permet de charger les informations du projet en cours depuis un fichier JSON.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    fname (String) : Le nom du fichier contenant les informations du projet.
        Return :None
        """
        
        # Gérer l'action ouvrir projet
        self.model.setFilePath(fname)
        self.model.ouvrirProjet()
        self.view.grid.setPixmap(self.model.getFullPathImage())
        self.grid_model.grid_position = self.model.position_produit
        self.grid_model.gridStart = self.model.position_grille
        self.grid_model.square_size = self.model.case_taille

        self.grid_model.updateGrid(self.view.grid.pixmap_height,self.view.grid.pixmap_width)
        self.view.grid.createGrid(self.grid_model.square_size,self.grid_model.gridMoved,self.model.position_grille)

        # Configuration des boutons en fonction de l'état d'avancement du projet.
        if self.model.itemsPlaced : self.productListEnabled()
        elif self.model.gridConfiguredFinish : self.confGridEnd()
        elif self.model.gridConfigured : self.confGridBegin()
        else : self.view.btn1.setEnabled(True), self.view.btn3.setEnabled(True)

        products = self.model.getProducts()
        self.view.product.update_Product(products,self.model.getPlacedProducts())
        self.grid_model.grid_position = self.model.position_produit
        self.view.pr.updateCheckbox(products)

    def mouseItemGrid(self,pos):
        """
        Cette méthode permet de gérer l'événement lorsque l'utilisateur fait un clic sur la grille.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    pos (tuple[int, int]) : La position (x, y) du clic dans la grille.
        Return :None
        """
        if self.model.gridConfigured and not self.model.gridConfiguredFinish:
            print("Bougement de la grille")
            self.grid_model.gridMoved = True
            self.grid_model.gridStart = (self.view.grid.group.pos().x(),self.view.grid.group.pos().y())
        self.grid_model.addItems(self.view.product.list_checked_items,pos)
        self.model.position_produit = self.grid_model.grid_position
        self.view.product.set_Unchecked_Items()
        self.view.product.clear_Checked_Items()


    def supprimerProjet(self, fname):
        """
        Cette méthode permet de supprimer le fichier JSON du projet en cours en vérifiant s'il existe.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    fname (String) : Le nom du fichier du projet à supprimer.
        Return :None
        """
        # Gérer l'action supprimer projet
        self.model.setFilePath(fname)
        self.model.supprimerProjet()
        self.updateProductList()

    def enregistrerProjet(self):
        """
        Cette méthode permet d'enregistrer les informations du projet en cours dans un fichier écrit en JSON.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        """
        
        # Gérer l'action enregistrer projet

        self.model.position_produit = self.grid_model.grid_position
        self.model.position_grille = self.grid_model.gridStart
        self.model.case_taille = self.grid_model.square_size

        self.model.enregistrerProjet()

    def updateProductList(self):
        """
        Cette méthode permet de mettre à jour la liste des produits dans la vue en utilisant les données du modèle.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        """
        products = self.model.getProducts()
        self.view.product.update_Product(products)

    def show(self):
        """
        Cette méthode permet d'afficher la vue.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
        Return :None
        """
        self.view.showMaximized()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    controller = SoftwareController()
    controller.login.show()

    sys.exit(app.exec())
