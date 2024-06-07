from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys, os

# -----------------------------------------------------------------------------
# --- classe placement_Product
# -----------------------------------------------------------------------------


class placement_Product(QWidget):
    # Constructeur
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

        Paramètres :self (placement_Product): L'instance de la classe.
                    item (QListWidgetItem): L'élément de la liste qui a été modifié.
        Return :None
        """
        if item.checkState() == Qt.CheckState.Checked:
            self.list_checked_items.append(item)
        elif (item.checkState() == Qt.CheckState.Unchecked) and (item in self.list_checked_items):
            self.list_checked_items.remove(item)
            
    def set_Unchecked_Items(self):
        """
        Cette méthode permet d'initialiser les cases à cocher en non coché
        Elle vérifie chaque élément de la liste et désactive les éléments qui sont déjà cochés.
        
        Paramètres : self (placement_Product): L'instance de la classe.
        Return : None
        """
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            if item in self.list_checked_items:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
    
    def clear_Checked_Items(self):
        """
        Cette méthode permet de vider la liste des produits qui ont été cochés.
        Paramètres : self (placement_Product): L'instance de la classe.
        Return : None
        """
        self.list_checked_items = []     

    def update_Product(self, products, placed_products=[]):
        """
        Cette méthode permet d'initialiser les cases à cocher en non coché et de mettre à jour la liste des produits.

        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    products (list[String]) : Une liste des produits.
                    placed_products (list[String], optionnel) : Une liste des produits déjà utilisés.
        Return :None
        """
        self.list_items = products
        self.update_Product_List(placed_products)

    def update_Product_List(self, placed_products=[]):
        """
        Cette méthode permet de mettre à jour la liste des produits en effaçant la liste existante et en ajoutant les nouveaux produits.
        Elle permet également de griser les produits déjà utilisés et d'initialiser les cases à cocher en non coché.

        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    placed_products (list[String], optionnel) : Une liste des produits déjà utilisés.

        Return :None
        """
        self.list_widget.clear()
        self.list_widget.addItems(self.list_items)
        
        # Mettre les checkbox pour chaque item et griser les items utilisés
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