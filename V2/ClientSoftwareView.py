import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal

from productListWidget import *
from placementProducts import *
from pictureView import *
from openProject import openProject

class ClientSoftwareView(QMainWindow):
    
    # Constructor
    def __init__(self) -> None:
        super().__init__()
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
  
        # Layout vertical --> principal layout
        mainlayout = QHBoxLayout()
        central_widget.setLayout(mainlayout)

        # Menu bar
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu('&Fichier')
        menu_file.addAction('Ouvrir',self.openProject)

        # Layouts
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()

        # Widgets
        self.picture = pictureView()
        self.productList = productListWidget()
        self.productPlacement = placementProducts()
        self.openProjectDialog = openProject()

        self.button_path = QPushButton("Afficher le plus court chemin")
        self.button_path.clicked.connect(self.path)

        # Add widgets in the layouts
        layout_left.addWidget(self.picture)
        layout_right.addWidget(self.productList,alignment=Qt.AlignmentFlag.AlignRight)
        layout_right.addWidget(self.productPlacement,alignment=Qt.AlignmentFlag.AlignRight)
        layout_right.addWidget(self.button_path)

        # Add layouts in the mainlayout 
        mainlayout.addLayout(layout_left)
        mainlayout.addLayout(layout_right)

        # Show the software in full screen
        self.showMaximized()
    
    # Signals
    openClicked = pyqtSignal(str)
    dijkstraClicked = pyqtSignal()

    # Methods
    def openProject(self):
        self.openProjectDialog.exec()
    
    def path(self) -> None:
        self.dijkstraClicked.emit()

# Main
if __name__ == "__main__":  
    print(' ----- Execution du logiciel ----- ')
    app = QApplication(sys.argv)
    fenetre = ClientSoftwareView()
    sys.exit(app.exec())