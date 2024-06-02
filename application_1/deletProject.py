import sys,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSignal, Qt

# -----------------------------------------------------------------------------
# --- classe GridProject
# -----------------------------------------------------------------------------

class deletProject(QDialog):
    # Constructeur
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Supprimer projet")
        
        
        current_directory = sys.path[0]
        self.parent_directory = os.path.dirname(current_directory)
        
        self.setWindowIcon(QIcon(self.parent_directory+"//icons//delet_file.svg"))
        
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
        self.tree.itemDoubleClicked.connect(self.delet_selected_file)
        self.button.clicked.connect(self.delet_selected_file)
        

        
    deletClicked = pyqtSignal(str)

    def search_files(self):
        """
        Cette fonction permet de rechercher les fichiers du dossier Espace_de_travail et de les afficher dans la fenêtre de dialogue.
        
        Paramètres : self : L'instance de la classe.
        Return : None 
        """
        self.tree.clear()
        
        search_text = self.search.text()
        for file in os.listdir(f"{self.parent_directory}//Espace_de_travail"):
            if file.endswith(".json") and search_text.lower() in file.lower():
                item = QTreeWidgetItem(self.tree, [file])
                self.tree.addTopLevelItem(item)
                

    def delet_selected_file(self):
        """
        Cette méthode supprime le fichier sélectionné de la liste des fichiers disponibles.

        Paramètres :self : L'instance de la classe.
        Return :None
        """
        selected_item = self.tree.selectedItems()
        if selected_item:
            # faire une confirmation avant de supprimer le fichier
            messageBox = QMessageBox(QMessageBox.Icon.Question,
                        "Confirmation de suppression",
                        "Voulez-vous vraiment supprimer ce fichier ?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                        self)
            messageBox.button(QMessageBox.StandardButton.Yes).setText("Oui")
            messageBox.button(QMessageBox.StandardButton.No).setText("Non")
            messageBox.exec()
            
            if messageBox.clickedButton() == messageBox.button(QMessageBox.StandardButton.Yes):
                selected_file = f"{self.parent_directory}//Espace_de_travail//{selected_item[0].text(0)}"
                self.deletClicked.emit(selected_file)
                self.close()                
            
            
            
    # fonction de Qdialog qui permet de gérer les événements de la fenêtre lorsqu'elle est affichée
    def showEvent(self, event):
        """
        Cette méthode est appelée lorsque la fenêtre est affichée.
        Elle appelle la fonction search_files() pour rechercher les fichiers dans le dossier Espace_de_travail et les afficher dans la fenêtre de dialogue.
    
        Paramètres :self : L'instance de la classe.
                    event : L'événement de QShowEvent.
        Return : None
        """
        self.search_files()

    # fonction de Qdialog qui permet de gérer les événements clavier
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Delete:
            self.delet_selected_file()

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = deletProject()  
    window.show()
    sys.exit(app.exec())