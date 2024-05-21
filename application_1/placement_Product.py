from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys, os


# TODO restant:
# - Connecter le fichier avec le model pour charger toute la liste des produits
# - Mettre en place la fonctionnalité de recherche
# - Mettre en place la fonctionnalité de placement des produits dans la grille
# - Mettre en place la fonctionnalité de suppression des produits de la grille
# - Mettre en place la fonctionnalité de grisage des produits non disponibles (déjà placés dans une autre case de la grille)


class placement_Product(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Placement Product")
        
        layout = QVBoxLayout()

        list_widget = QListWidget()
        list_items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]
        list_widget.addItems(list_items)

        for index in range(list_widget.count()):
            item = list_widget.item(index)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            if index == 2:
                item.setCheckState(Qt.CheckState.Unchecked)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
            else:
                item.setCheckState(Qt.CheckState.Unchecked)

        list_widget.itemChanged.connect(self.handleItemChanged)

        layout.addWidget(list_widget)
        self.setLayout(layout)

    def handleItemChanged(self, item):
        if item.checkState() == Qt.CheckState.Checked:
            print(f"Item {item.text()} is checked")
        else:
            print(f"Item {item.text()} is unchecked")
    
    def update_product(self, product):
        pass
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = placement_Product()
    window.show()
    sys.exit(app.exec())