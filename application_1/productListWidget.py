import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal

# -----------------------------------------------------------------------------
# --- classe productListWidget
# -----------------------------------------------------------------------------

class productListWidget(QWidget):
    # Constructeur
    def __init__(self) -> None:
        super().__init__()
        self.tree  = QTreeWidget()
        
        current_directory = sys.path[0]
        parent_directory = os.path.dirname(current_directory)
        self.upadateWorking = False


        with open(f"{parent_directory}//Liste_de_produits//liste_produits.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for key in data.keys():
                self.add_tree_item(key, data[key])

        self.tree.setHeaderLabels(["Liste des produits"])

        # Connecter le signal itemChanged à la méthode checkboxChanged
        self.tree.itemChanged.connect(self.checkboxChanged)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.tree)
        self.setLayout(mainlayout)

    itemAdded = pyqtSignal(str)
    itemDelet = pyqtSignal(str)

    def add_tree_item(self, parent_name, children_names):
        """
        Cette méthode permet d'ajouter dans le QTreeWidgetItem une catégorie de produit avec les produits liés à cette catégorie.
        
        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    parent_name (String) : Le nom de la catégorie de produit.
                    children_names (list[String]) : Une liste des noms des produits liés à la catégorie.
        Return :None
        """
        parent_item = QTreeWidgetItem(self.tree, [parent_name])
        for child_name in children_names:
            child_item = QTreeWidgetItem(parent_item, [child_name])
            
            child_item.setCheckState(0, Qt.CheckState.Unchecked)
            
            parent_item.addChild(child_item)

    def checkboxChanged(self, item, column):
        """
        Cette méthode permet de gérer l'événement lorsqu'un bouton de case à cocher (checkbox) est cliqué.

        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    item (QTreeWidgetItem) : L'élément dont la case à cocher a été modifiée.
                    column (int) : La colonne de la case à cocher.
        Return :None
        """
        # le bouton est checké
        if self.upadateWorking:
            return
        if item.checkState(column) == Qt.CheckState.Checked:
            self.itemAdded.emit(item.text(column))
        else:
            self.itemDelet.emit(item.text(column))

    def updateCheckbox(self, products):
        """
        Cette méthode permet de mettre à jour les cases à cocher (checkbox) dans l'arbre en fonction de la liste des produits.

        Paramètres :self (PlacementProduct) : L'instance de la classe.
                    products (list[String]) : Une liste des noms des produits à cocher.

        Return :None
        """
        # parcourir les items de l'arbre pour trouver et checker les items de la liste products
        self.upadateWorking = True

        for i in range(self.tree.topLevelItemCount()):
            parent = self.tree.topLevelItem(i)
            for j in range(parent.childCount()):
                child = parent.child(j)
                if child.text(0) in products:
                    child.setCheckState(0, Qt.CheckState.Checked)

        self.upadateWorking = False


if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = productListWidget()  
    window.show()
    sys.exit(app.exec())