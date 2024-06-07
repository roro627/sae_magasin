import sys
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, pyqtSignal

from productListWidget import productListWidget
from shoppingList import shoppingList
from pictureView import pictureView
from openProject import openProject

class ClientSoftwareView(QMainWindow):
    def __init__(self) -> None:
        """
        Initialise la vue du logiciel client.
        """
        super().__init__()
        self.stratPoint = None
        self.endPoint = None
        
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
        layout_getPoint = QGridLayout()

        # Widgets
        self.picture = pictureView()
        self.productList = productListWidget()
        self.productList.leaveEvent = self.productListUnfocus
        self.listShopping = shoppingList()
        self.openProjectDialog = openProject()

        self.button_start = QPushButton("Pointer le départ")
        self.label_show_start = QLabel("Aucun départ défini",alignment=Qt.AlignmentFlag.AlignCenter)
        self.button_start.clicked.connect(self.getStartPoint)
        self.start_point = False
        
        self.button_end = QPushButton("Pointer l'arrivée")
        self.label_show_end = QLabel("Aucune arrivée définie",alignment=Qt.AlignmentFlag.AlignCenter)
        self.button_end.clicked.connect(self.getEndPoint)
        self.end_point = False

        self.button_path = QPushButton("Afficher le plus court chemin")
        self.button_path.clicked.connect(self.path)

        # Add widgets in the layouts
        layout_left.addWidget(self.picture)
        layout_right.addWidget(self.productList,alignment=Qt.AlignmentFlag.AlignRight)
        layout_right.addWidget(self.listShopping,alignment=Qt.AlignmentFlag.AlignRight)
        
        layout_getPoint.addWidget(self.button_start,0,0)
        layout_getPoint.addWidget(self.label_show_start,1,0)
        layout_getPoint.addWidget(self.button_end,0,1)
        layout_getPoint.addWidget(self.label_show_end,1,1)
        layout_right.addLayout(layout_getPoint)
        
        layout_right.addWidget(self.button_path)

        # Add layouts in the mainlayout 
        mainlayout.addLayout(layout_left)
        mainlayout.addLayout(layout_right)

        # Show the software in full screen
        self.showMaximized()

    openClicked = pyqtSignal(str)
    pathClicked = pyqtSignal()
    unfocus = pyqtSignal()

    def openProject(self):
        """
        Ouvre le projet.
        """
        self.openProjectDialog.exec()
    
    def path(self) -> None:
        """
        Affiche le chemin le plus court.
        """
        startPoint = self.label_show_start.text()
        endPoint = self.label_show_end.text()
        
        # si le texte est "Aucun(e) départ/arrivée défini(e)" ou "Sélectionnez un point sur la carte ", on affiche une fenêtre d'information
        if startPoint[0] == 'A' or startPoint[0] == 'S' or endPoint[0] == 'A' or endPoint[0] == 'S':  
            self.noPointsSet()
        elif len(self.listShopping.list_items) < 2:
            self.emptyShoppingList()
        else:
            self.pathClicked.emit()
        
    def getStartPoint(self):
        """
        Obtient le point de départ.
        """
        self.label_show_start.setText("Sélectionnez un point sur la carte")
        self.start_point = True
        # au prochain clic sur la carte, on récupère les coordonnées du point
        
    def getEndPoint(self):
        """
        Obtient le point d'arrivée.
        """
        self.label_show_end.setText("Sélectionnez un point sur la carte")
        self.end_point = True
    
    def resetPoint(self):
        if self.start_point : 
            self.start_point = False
        elif self.end_point : 
            self.end_point = False
    
    def setStartPoint(self, point: str):
        """
        Définit le point de départ.
        Args:
            point (str): Le point de départ.
        """
        self.label_show_start.setText(point)
    
    def setEndPoint(self, point: str):
        """
        Définit le point d'arrivée.
        Args:
            point (str): Le point d'arrivée.
        """
        self.label_show_end.setText(point)
        
    def productListUnfocus(self,_):
        """
        Envoie un signal pour indiquer que la souris n'est plus dans le widget productList.

        Args:
            _ : Paramètre inutile.
        """
        self.unfocus.emit()
        
    def noPointsSet(self):
        """
        Affiche une fenètre d'information demandant de sélectionner les points de départ et d'arrivée.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation))
        msg.setText("Veuillez sélectionner un point de départ et un point d'arrivée.")
        msg.exec()

    def emptyShoppingList(self):
        """
        Affiche une fenètre d'information demandant de sélectionner au moins 2 produits.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation))
        msg.setText("Veuillez sélectionner au moins 2 produits dans votre liste de course.")
        msg.exec()

if __name__ == "__main__":  
    print(' ----- Execution du logiciel ----- ')
    app = QApplication(sys.argv)
    fenetre = ClientSoftwareView()
    sys.exit(app.exec())