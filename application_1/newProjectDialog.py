import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class newProjectDialog(QDialog):

    # Constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nouveau projet")

        # Layouts
        mainLayout = QVBoxLayout()

        horizontalLayoutName = QHBoxLayout()
        horizontalLayoutAutor = QHBoxLayout()
        horizontalLayoutShopName = QHBoxLayout()
        horizontalLayoutShopAdd = QHBoxLayout()

        verticalLayout = QVBoxLayout()

        # Widgets
        ProjectNameText = QLabel("Nom du projet")
        ProjectNameLine = QLineEdit()

        AutorNameText = QLabel("Auteur(s)")
        AutorNameLine = QLineEdit()

        ShopNameText = QLabel("Nom du magasin")
        ShopNameLine = QLineEdit()

        ShopAddText = QLabel("Addresse du magasin")
        ShopAddLine = QLineEdit()

        # Add the widgets and layouts
        horizontalLayoutName.addWidget(ProjectNameText)
        horizontalLayoutName.addWidget(ProjectNameLine)
        verticalLayout.addLayout(horizontalLayoutName)

        horizontalLayoutAutor.addWidget(AutorNameText)
        horizontalLayoutAutor.addWidget(AutorNameLine)
        verticalLayout.addLayout(horizontalLayoutAutor)

        horizontalLayoutShopName.addWidget(ShopNameText)
        horizontalLayoutShopName.addWidget(ShopNameLine)
        verticalLayout.addLayout(horizontalLayoutShopName)

        horizontalLayoutShopAdd.addWidget(ShopAddText)
        horizontalLayoutShopAdd.addWidget(ShopAddLine)
        verticalLayout.addLayout(horizontalLayoutShopAdd)

        mainLayout.addLayout(verticalLayout)

        self.setLayout(mainLayout)

