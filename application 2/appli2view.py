import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel

# Définition de la classe principale de l'application
class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choix du Magasin")
        self.resize(400, 200)

        # Chargement des magasins depuis le fichier JSON avec un fichier test
        with open("magasins.json", "r") as f:
            self.magasins_disponibles = json.load(f)

        # Interface utilisateur
        layout = QVBoxLayout()

        self.label_magasin = QLabel("Sélectionnez un magasin:")
        layout.addWidget(self.label_magasin)

        self.combo_magasin = QComboBox()
        for magasin in self.magasins_disponibles:
            self.combo_magasin.addItem(magasin["nom"])
        layout.addWidget(self.combo_magasin)

        self.btn_selectionner = QPushButton("Sélectionner")
        self.btn_selectionner.clicked.connect(self.selectionner_magasin)
        layout.addWidget(self.btn_selectionner)

        self.setLayout(layout)

    # Méthode pour gérer la sélection du magasin
    def selectionner_magasin(self):
        index = self.combo_magasin.currentIndex()
        magasin_selectionne = self.magasins_disponibles[index]
        print("Magasin sélectionné:", magasin_selectionne["nom"])
        print("Adresse:", magasin_selectionne["adresse"])

# Point d'entrée de l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
