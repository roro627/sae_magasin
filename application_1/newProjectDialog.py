import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class newProjectDialog(QDialog):

    # Constructor
    def __init__(self) -> None:
        """
        This constructor is use for create widgets and layouts. 
        Params : self
        Return : None
        """
        super().__init__()
        self.setWindowTitle("Nouveau projet")

        # Layouts
        mainLayout = QVBoxLayout()

        horizontalLayoutName = QHBoxLayout()
        horizontalLayoutAutor = QHBoxLayout()
        horizontalLayoutDate = QHBoxLayout()
        horizontalLayoutShopName = QHBoxLayout()
        horizontalLayoutShopAdd = QHBoxLayout()
        horizontalLayoutShopPlan = QHBoxLayout()

        verticalLayout = QVBoxLayout()

        # Widgets
        projectNameText = QLabel("Nom du projet")
        projectNameLine = QLineEdit()

        autorNameText = QLabel("Auteur(s)")
        autorNameLine = QLineEdit()

        projectDateText = QLabel("Date de création")
        projectDateCreate = QDateEdit()
        projectDateCreate.setDateTime(QtCore.QDateTime.currentDateTime())

        shopNameText = QLabel("Nom du magasin")
        shopNameLine = QLineEdit()

        shopAddText = QLabel("Addresse du magasin")
        shopAddLine = QLineEdit()

        shopPlanButton = QPushButton("Choisir un plan")
        self.shopPlanText = QLabel("Pas de plan sélectionné")

        projectFinishButton = QPushButton("Créer mon projet")

        shopPlanButton.clicked.connect(self.openPlan)
        projectFinishButton.clicked.connect(self.finishProject)

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

        horizontalLayoutShopPlan.addWidget(shopPlanButton)
        horizontalLayoutShopPlan.addWidget(self.shopPlanText)
        verticalLayout.addLayout(horizontalLayoutShopPlan)

        verticalLayout.addWidget(projectFinishButton)

        mainLayout.addLayout(verticalLayout)

        self.setLayout(mainLayout)
    
    # Signals
    planButtonClicked = pyqtSignal(str)
    finishButtonClicked = pyqtSignal(dict)

    # Methods
    def getAllInfo(self) -> dict:
        dictionary = {}
        dictionary["nom_projet"] = self.projectNameLine.text()
        # TO BE CONTINUED
        return dictionary

    def openPlan(self) -> None:
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.',"*.png *.jpg *.gif *.jpeg")[0]
        self.planButtonClicked.emit(fname)
    
    def finishProject(self) -> None:
        if self.projectNameLine.text() == "" or self.autorNameLine.text() == "" or self.shopNameLine.text() == "" or self.shopAddLine.text() == "":
            invalid_box = QMessageBox(QMessageBox.Icon.Critical,"Erreur","Erreur, au moins l'un des champs n'est pas complété ou aucun plan n'est sélectionné.")
            invalid_box.exec()
        else :
            self.finishButtonClicked.emit(self.getAllInfo())