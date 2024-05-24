import sys,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSignal, Qt

class deletProject(QDialog):
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
        self.tree.clear()
        
        search_text = self.search.text()
        for file in os.listdir(f"{self.parent_directory}//Espace_de_travail"):
            if file.endswith(".json") and search_text.lower() in file.lower():
                item = QTreeWidgetItem(self.tree, [file])
                self.tree.addTopLevelItem(item)
                

    def delet_selected_file(self):
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