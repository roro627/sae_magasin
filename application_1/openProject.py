import sys,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSignal

# -----------------------------------------------------------------------------
# --- classe openProject
# -----------------------------------------------------------------------------

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
        """
        Cette méthode permet de chercher le fichier json que l'on veut.
        Paramètres : self
        Return : None
        """
        self.tree.clear()
        
        search_text = self.search.text()
        for file in os.listdir(f"{self.parent_directory}//Espace_de_travail"):
            if file.endswith(".json") and search_text.lower() in file.lower():
                item = QTreeWidgetItem(self.tree, [file])
                self.tree.addTopLevelItem(item)
                

    def open_selected_file(self):
        """
        Cette méthode permet d'ouvrir le fichier json qu'on a selectionné précédement.
        Paramètres : self
        Return : None
        """
        selected_item = self.tree.selectedItems()
        if selected_item:
            selected_file = f"{self.parent_directory}//Espace_de_travail//{selected_item[0].text(0)}"
            self.openClicked.emit(selected_file) 
            self.close()
            
            
    def showEvent(self, event):
        """
        Cette méthode permet de lancer la fonction search_files() dès que la fenêtre est affichée, vient de QDialog.
        Paramètres : self , event -> QShowEvent
        Return : None
        """
        self.search_files()


if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = openProject()  
    window.show()
    sys.exit(app.exec())