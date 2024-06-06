from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys, os

class shoppingList(QWidget):
    def __init__(self) -> None:
        """
        Initialise l'objet shoppingList avec une liste vide et configure l'interface utilisateur.
        """
        super().__init__()
        
        layout = QVBoxLayout()

        self.title = QLabel("Liste de course")
        self.list_widget = QListWidget()        
        
        self.list_items = []    
        
        self.updateWorking = False    


        layout.addWidget(self.title)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

            
    def update_Product(self, products: list[str]) -> None:
        """
        Met à jour la liste des produits et rafraîchit l'affichage.

        Paramètres :
        products (list) : La nouvelle liste de produits.
        """
        self.list_items = products
        self.update_Product_List()
        
    def update_Product_List(self) -> None:
        """
        Rafraîchit l'affichage de la liste de produits.
        """
        self.list_widget.clear()
        self.list_widget.addItems(self.list_items)
        
        # mettre les checkbox pour chaque item et griser les items utilisés
        for index in range(self.list_widget.count()):
            self.list_widget.item(index)


    def add_product(self, product: str) -> None:
        """
        Ajoute un produit à la liste et rafraîchit l'affichage.

        Paramètres :
        product (str) : Le produit à ajouter.
        """
        self.list_items.append(product)
        self.update_Product_List()
        
    def remove_product(self, product: str) -> None:
        """
        Supprime un produit de la liste et rafraîchit l'affichage.

        Paramètres :
        product (str) : Le produit à supprimer.
        """
        self.list_items.remove(product)
        self.update_Product_List()

    def get_products(self) -> list[str]:
        """
        Renvoie la liste des produits.

        Returns :
        list : La liste des produits.
        """
        return self.list_items

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = shoppingList()
    window.update_Product(["item1","item2","item3"])
    window.show()
    sys.exit(app.exec())