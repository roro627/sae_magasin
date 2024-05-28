import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal

from newProjectDialog import newProjectDialog
from openProject import openProject
from deletProject import deletProject

from GridView import GridView

from productListWidget import productListWidget
from placement_Product import placement_Product


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
        menu_file.addAction('Supprimer',self.deletProject)
        menu_file.addSeparator()
        menu_file.addAction('Enregistrer',self.saveProject)

        # Layouts
        layout_tools = QHBoxLayout()
        layout_menu = QHBoxLayout()

        # Widgets
        self.dial = newProjectDialog()
        self.openProjectDialog = openProject()
        self.deletProjectDialog = deletProject()
        
        self.pr = productListWidget()
        self.pr.setEnabled(False)

        self.grid = GridView()
        self.product = placement_Product()

        self.btn1 = QPushButton("Paramétrer la grille")
        self.btn1.clicked.connect(self.beginConfigGrid)

        self.btn2 = QPushButton("Terminer le paramétrage")
        self.btn2.setEnabled(False)
        self.btn2.clicked.connect(self.endConfigGrid)

        self.btn3 = QPushButton("Placer les produits")
        self.btn3.clicked.connect(self.beginPlacement)

        self.min = QLabel("1")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setEnabled(False)
        self.slider.setValue(5)
        self.slider.setMinimum(1)
        self.slider.setMaximum(5)
        self.max = QLabel("5")
        self.slider.valueChanged.connect(self.sliderValue)
        layout_tools.addWidget(self.btn1)
        layout_tools.addWidget(self.btn2)
        layout_tools.addWidget(self.btn3)
        layout_tools.addWidget(self.min)
        layout_tools.addWidget(self.slider)
        layout_tools.addWidget(self.max)
        mainlayout.addLayout(layout_tools)

        layout_menu.addWidget(self.product,alignment=Qt.AlignmentFlag.AlignLeft)
        layout_menu.addWidget(self.grid)
        layout_menu.addWidget(self.pr,alignment=Qt.AlignmentFlag.AlignRight)
        mainlayout.addLayout(layout_menu)

        
        # affiche en plein écran
        self.showMaximized()
    
    # Signals
    newClicked = pyqtSignal()
    saveClicked = pyqtSignal()
    sliderMoved = pyqtSignal(int)

    confGridClicked = pyqtSignal()
    confGridFinishClicked = pyqtSignal()
    placementClicked = pyqtSignal()

    # Methods
    def newProject(self):
        self.dial.exec() 

    def openProject(self):
        self.openProjectDialog.exec()
        
    def deletProject(self):
        self.deletProjectDialog.exec()

    def saveProject(self):
        self.saveClicked.emit()
    
    def sliderValue(self):
        val = 10*(self.slider.value())
        self.sliderMoved.emit(val)
    
    def beginConfigGrid(self):
        self.confGridClicked.emit()
    
    def endConfigGrid(self):
        self.confGridFinishClicked.emit()

    def beginPlacement(self):
        self.placementClicked.emit()

# Main
if __name__ == "__main__":  
    print(' ----- Execution du logiciel ----- ')
    app = QApplication(sys.argv)
    fenetre = SoftwareView()
    sys.exit(app.exec())