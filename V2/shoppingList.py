from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys, os

class shoppingList(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout = QVBoxLayout()

        self.title = QLabel("Liste de course")
        self.list_widget = QListWidget()        
        
        self.list_items = []    
        
        self.updateWorking = False    

        self.list_widget.itemChanged.connect(self.Box_Change)

        layout.addWidget(self.title)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

    def Box_Change(self, item):
        if item.checkState() == Qt.CheckState.Checked:
            print(f"Item {item.text()} is checked")
        else:
            print(f"Item {item.text()} is unchecked")
            
    def update_Product(self, products):
        self.list_items = products
        self.update_Product_List()
        
    def update_Product_List(self):
        self.list_widget.clear()
        self.list_widget.addItems(self.list_items)
        
        # mettre les checkbox pour chaque item et griser les items utilisés
        for index in range(self.list_widget.count()):
            self.list_widget.item(index)


    def add_product(self, product):
        self.list_items.append(product)
        self.update_Product_List()
        
    def remove_product(self, product):
        self.list_items.remove(product)
        self.update_Product_List()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = shoppingList()
    window.update_Product(["item1","item2","item3"])
    window.show()
    sys.exit(app.exec())