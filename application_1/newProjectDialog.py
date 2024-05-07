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
        horizontalLayoutDate = QHBoxLayout()
        horizontalLayoutShopName = QHBoxLayout()
        horizontalLayoutShopAdd = QHBoxLayout()

        verticalLayout = QVBoxLayout()

        # Widgets
        projectNameText = QLabel("Nom du projet")
        projectNameLine = QLineEdit()

        autorNameText = QLabel("Auteur(s)")
        autorNameLine = QLineEdit()

        projectDateText = QLabel("Date de création")
        projectDateCreate = QDateEdit()

        shopNameText = QLabel("Nom du magasin")
        shopNameLine = QLineEdit()

        shopAddText = QLabel("Addresse du magasin")
        shopAddLine = QLineEdit()

        # Add the widgets and layouts
        horizontalLayoutName.addWidget(projectNameText)
        horizontalLayoutName.addWidget(projectNameLine)
        verticalLayout.addLayout(horizontalLayoutName)

        horizontalLayoutAutor.addWidget(autorNameText)
        horizontalLayoutAutor.addWidget(autorNameLine)
        verticalLayout.addLayout(horizontalLayoutAutor)

        horizontalLayoutDate.addWidget(projectDateText)
        horizontalLayoutDate.addWidget(projectDateCreate)
        verticalLayout.addLayout(horizontalLayoutDate)

        horizontalLayoutShopName.addWidget(shopNameText)
        horizontalLayoutShopName.addWidget(shopNameLine)
        verticalLayout.addLayout(horizontalLayoutShopName)

        horizontalLayoutShopAdd.addWidget(shopAddText)
        horizontalLayoutShopAdd.addWidget(shopAddLine)
        verticalLayout.addLayout(horizontalLayoutShopAdd)

        mainLayout.addLayout(verticalLayout)

        self.setLayout(mainLayout)

