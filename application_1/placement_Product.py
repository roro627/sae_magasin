from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys, os

# -----------------------------------------------------------------------------
# --- classe placement_Product
# -----------------------------------------------------------------------------

# TODO restant:
# - Connecter le fichier avec le model pour charger toute la liste des produits
# - Mettre en place la fonctionnalité de recherche
# - Mettre en place la fonctionnalité de placement des produits dans la grille (FAIT)
# - Mettre en place la fonctionnalité de suppression des produits de la grille
# - Mettre en place la fonctionnalité de grisage des produits non disponibles (FAIT)


class placement_Product(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Placement Product")
        
        
        layout = QVBoxLayout()

        self.list_widget = QListWidget()        
        
        self.list_items = []  
        self.list_checked_items = []       

        self.list_widget.itemChanged.connect(self.Box_Change)

        layout.addWidget(self.list_widget)
        self.setLayout(layout)

    def Box_Change(self, item):
        """
        Cette méthode est appelée lorsque l'état d'un élément de la liste change.
        Elle permet d'ajouter ou de supprimer les éléments sélectionnés dans la liste des produits.
        Paramètres : item -> QListWidgetItem
        Return : None
        """
        if item.checkState() == Qt.CheckState.Checked:
            self.list_checked_items.append(item)
        elif (item.checkState() == Qt.CheckState.Unchecked) and (item in self.list_checked_items):
            self.list_checked_items.remove(item)
            
    def set_Unchecked_Items(self):
        """
        Cette méthode permet d'initialiser les cases à cocher en non coché
        Elle vérifie chaque élément de la liste et désactive les éléments qui sont déjà cochés.
        Paramètres : self
        Return : None
        """
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            if item in self.list_checked_items:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
    
    def clear_Checked_Items(self):
        """
        Cette méthode permet de vider la liste des produits qui ont été cochés.
        Paramètres : self
        Return : None
        """
        self.list_checked_items = []     

    def update_Product(self, products, placed_products = []):
        """
        Cette méthode permet d'initialiser les cases à cocher en non coché et de mettre à jour la liste des produits.
        Paramètres : self , products -> une liste[String] , placed_products -> liste des produits déjà utilisés qui est une liste[String]
        """
        self.list_items = products
        self.update_Product_List(placed_products)
    
    def update_Product_List(self, placed_products = []):
        """
        Cette méthode permet de mettre à jour la liste des produits en effaçant la liste des produits existants et de les ajouter à nouveau.
        Elle permet également de griser les produits déjà utilisés.
        Paramètres : self, placed_products -> liste des produits déjà utilisés qui est une liste[String]
        Return : None
        """
        self.list_widget.clear()
        self.list_widget.addItems(self.list_items)
        
        # mettre les checkbox pour chaque item et griser les items utilisés
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            
            item.setCheckState(Qt.CheckState.Unchecked)

            if item.text() in placed_products:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = placement_Product()
    window.update_Product(["Product 1", "Product 2", "Product 3", "Product 4"])
    window.show()
    sys.exit(app.exec())