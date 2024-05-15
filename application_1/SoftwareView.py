import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from newProjectDialog import newProjectDialog
from productListWidget import productListWidget

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

        # Menu bar
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu('&Fichier')
        menu_file.addAction('Nouveau',self.newProject)
        menu_file.addAction('Ouvrir',self.openProject)
        menu_file.addSeparator()
        menu_file.addAction('Enregistrer',self.saveProject)

        # Dock
        self.pr = productListWidget()
        

        self.dial = newProjectDialog()
        mainlayout.addWidget(self.pr,alignment=Qt.AlignmentFlag.AlignRight)


        # affiche en plein écran
        self.showMaximized()
    
    # Signals
    newClicked = pyqtSignal()
    openClicked = pyqtSignal()
    saveClicked = pyqtSignal()
    
    # Methods
    def newProject(self):
        self.dial.exec() 

    def openProject(self):
        self.openClicked.emit()

    def saveProject(self):
        self.saveClicked.emit()

# Main
if __name__ == "__main__":  
    print(' ----- Execution du logiciel ----- ')
    app = QApplication(sys.argv)
    fenetre = SoftwareView()
    sys.exit(app.exec())