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
    
    # Signal
    planButtonClicked = pyqtSignal()

    # Methods
    def openPlan(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.',"*.png *.jpg *.gif *.jpeg")[0]
        self.planButtonClicked.emit()
        # A mettre dans un autre fichier pour respecter modèle MVC
        self.shopPlanText.setText(os.path.basename(fname))
    
    def finishProject(self):
        pass