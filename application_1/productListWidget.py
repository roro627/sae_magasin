import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class productListWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.tree  = QTreeWidget()
        current_directory = sys.path[0]
        parent_directory = os.path.dirname(current_directory)

        with open(f"{parent_directory}//Liste_de_produits//liste_produits.json", "r") as f:
            data = json.load(f)
            print(data)

        self.add_tree_item("Fruit", ["Pomme", "Banane", "Orange"])
        self.add_tree_item("Légume", ["Carotte", "Pomme de terre", "Tomate"])
        self.tree.setHeaderLabels(["Liste des produits"])

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.tree)
        self.setLayout(mainlayout)

    def add_tree_item(self, parent_name, children_names):
        parent_item = QTreeWidgetItem(self.tree, [parent_name])
        for child_name in children_names:
            child_item = QTreeWidgetItem(parent_item, [child_name])

            child_item.setCheckState(0, Qt.CheckState.Unchecked)

            parent_item.addChild(child_item)

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = productListWidget()  
    window.show()
    sys.exit(app.exec())