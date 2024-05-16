import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal

class productListWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.tree  = QTreeWidget()
        current_directory = sys.path[0]
        parent_directory = os.path.dirname(current_directory)

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
        parent_item = QTreeWidgetItem(self.tree, [parent_name])
        for child_name in children_names:
            child_item = QTreeWidgetItem(parent_item, [child_name])

            child_item.setCheckState(0, Qt.CheckState.Unchecked)

            parent_item.addChild(child_item)

    def checkboxChanged(self, item, column):
        # le bouton est checké
        if item.checkState(column) == Qt.CheckState.Checked:
            self.itemAdded.emit(item.text(column))
        else:
            self.itemDelet.emit(item.text(column))

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = productListWidget()  
    window.show()
    sys.exit(app.exec())