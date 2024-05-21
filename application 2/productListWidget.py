import sys
import os
import json
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, pyqtSignal

class productListWidget(QWidget):
    itemAdded = pyqtSignal(str)
    itemDeleted = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.loadData()

    def initUI(self):
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Liste des produits"])
        self.tree.itemChanged.connect(self.checkboxChanged)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tree)
        self.setLayout(main_layout)

    def loadData(self):
        current_directory = sys.path[0]
        parent_directory = os.path.dirname(current_directory)
        json_path = os.path.join(parent_directory, "Liste_de_produits", "liste_produits.json")

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    self.add_tree_item(key, value)
        except FileNotFoundError:
            QMessageBox.critical(self, "Erreur", "Le fichier liste_produits.json est introuvable.")
            sys.exit(1)
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Erreur", "Erreur de lecture du fichier JSON.")
            sys.exit(1)

    def add_tree_item(self, parent_name, children_names):
        parent_item = QTreeWidgetItem(self.tree, [parent_name])
        for child_name in children_names:
            child_item = QTreeWidgetItem(parent_item, [child_name])
            child_item.setCheckState(0, Qt.CheckState.Unchecked)
            parent_item.addChild(child_item)

    def checkboxChanged(self, item, column):
        if item.checkState(column) == Qt.CheckState.Checked:
            self.itemAdded.emit(item.text(column))
        else:
            self.itemDeleted.emit(item.text(column))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = productListWidget()
    window.show()
    sys.exit(app.exec())
