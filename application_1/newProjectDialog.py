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
        self.projectNameText = QLabel("Nom du projet")
        self.projectNameLine = QLineEdit()

        self.autorNameText = QLabel("Auteur(s)")
        self.autorNameLine = QLineEdit()

        self.projectDateText = QLabel("Date de création")
        self.projectDateCreate = QDateEdit()
        self.projectDateCreate.setDateTime(QtCore.QDateTime.currentDateTime())

        self.shopNameText = QLabel("Nom du magasin")
        self.shopNameLine = QLineEdit()

        self.shopAddText = QLabel("Addresse du magasin")
        self.shopAddLine = QLineEdit()

        self.shopPlanButton = QPushButton("Choisir un plan")
        self.shopPlanText = QLabel("Pas de plan sélectionné")

        self.projectFinishButton = QPushButton("Créer mon projet")

        self.shopPlanButton.clicked.connect(self.openPlan)
        self.projectFinishButton.clicked.connect(self.finishProject)

        # Add the widgets and layouts
        horizontalLayoutName.addWidget(self.projectNameText)
        horizontalLayoutName.addWidget(self.projectNameLine)
        verticalLayout.addLayout(horizontalLayoutName)

        horizontalLayoutAutor.addWidget(self.autorNameText)
        horizontalLayoutAutor.addWidget(self.autorNameLine)
        verticalLayout.addLayout(horizontalLayoutAutor)

        horizontalLayoutDate.addWidget(self.projectDateText)
        horizontalLayoutDate.addWidget(self.projectDateCreate)
        verticalLayout.addLayout(horizontalLayoutDate)

        horizontalLayoutShopName.addWidget(self.shopNameText)
        horizontalLayoutShopName.addWidget(self.shopNameLine)
        verticalLayout.addLayout(horizontalLayoutShopName)

        horizontalLayoutShopAdd.addWidget(self.shopAddText)
        horizontalLayoutShopAdd.addWidget(self.shopAddLine)
        verticalLayout.addLayout(horizontalLayoutShopAdd)

        horizontalLayoutShopPlan.addWidget(self.shopPlanButton)
        horizontalLayoutShopPlan.addWidget(self.shopPlanText)
        verticalLayout.addLayout(horizontalLayoutShopPlan)

        verticalLayout.addWidget(self.projectFinishButton)

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