import sys
from PyQt6.QtWidgets import *

class SoftwareView(QMainWindow):
    
    # Constructor
    def __init__(self):
        super().__init__()

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
  
        # Layout vertical --> principal layout
        mainlayout = QVBoxLayout()
        central_widget.setLayout(mainlayout)

        mainlayout.addWidget(QLabel("Texte de test"))

        # Menu bar
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu('&Fichier')
        menu_file.addAction('Nouveau',self.newProject)
        menu_file.addAction('Ouvrir',self.openProject)
        menu_file.addSeparator()
        menu_file.addAction('Enregistrer',self.saveProject)

        self.show()
    
    # Methods
    def newProject(self):
        pass

    def openProject(self):
        pass

    def saveProject(self):
        pass

# Main
if __name__ == "__main__":  
    print(' ----- Execution du logiciel ----- ')
    app = QApplication(sys.argv)
    fenetre = SoftwareView()
    sys.exit(app.exec())