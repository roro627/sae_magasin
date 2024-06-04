import sys,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSignal

class openProject(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ouvrir projet")
        
        
        current_directory = sys.path[0]
        self.parent_directory = os.path.dirname(current_directory)
        
        self.setWindowIcon(QIcon(self.parent_directory+"//icons//open_file.svg"))
        
        self.tree  = QTreeWidget()
        self.search = QLineEdit()
        self.button = QPushButton("Valider")
        
        self.search.setPlaceholderText("Rechercher un fichier")
        self.search.setClearButtonEnabled(True)
        
        self.tree.setHeaderLabels(["Liste des projet existants"])
        self.search_files()
        
                
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.search)
        mainlayout.addWidget(self.tree)
        self.setLayout(mainlayout)
        mainlayout.addWidget(self.button)
        
        self.search.textChanged.connect(self.search_files)
        self.tree.itemDoubleClicked.connect(self.open_selected_file)
        self.button.clicked.connect(self.open_selected_file)

    openClicked = pyqtSignal(str)

    def search_files(self):
        self.tree.clear()
        
        search_text = self.search.text()
        for file in os.listdir(f"{self.parent_directory}//Espace_de_travail"):
            if file.endswith(".json") and search_text.lower() in file.lower():
                item = QTreeWidgetItem(self.tree, [file])
                self.tree.addTopLevelItem(item)
                

    def open_selected_file(self):
        selected_item = self.tree.selectedItems()
        if selected_item:
            selected_file = selected_item[0].text(0)
            selected_file = f"{self.parent_directory}//Espace_de_travail//{selected_file}"
            self.openClicked.emit(selected_file)
            self.close()
            
    

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = openProject()  
    window.show()
    sys.exit(app.exec())