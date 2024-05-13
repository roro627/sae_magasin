import sys
import json
import os
from PyQt6.QtWidgets import *

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choix du Magasin")
        self.resize(400, 200)

        # Chargement des magasins depuis le fichier JSON
        with open(sys.path[0] + "/magasins.json", "r") as f:
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

        self.label_adresse = QLabel("")
        layout.addWidget(self.label_adresse)

        self.setLayout(layout)

    def selectionner_magasin(self):
        confirmation_box = QMessageBox(self)
        confirmation_box.setText('Etes-vous sûr de prendre ce magasin ?')
        confirmation_box.setWindowTitle("Confirmation")
        confirmation_box.setIcon(QMessageBox.Icon.Information)
        confirmation_box.addButton(QMessageBox.StandardButton.Cancel)
        confirmation_box.addButton(QMessageBox.StandardButton.Ok)
        confirmation_box.setDefaultButton(QMessageBox.StandardButton.Cancel)
        confirmation_box.buttonClicked.connect(self.confirmation_button_clicked)
        confirmation_result = confirmation_box.exec()

        if confirmation_result == QMessageBox.StandardButton.Ok:
            index = self.combo_magasin.currentIndex()
            magasin_selectionne = self.magasins_disponibles[index]
            nom_magasin = magasin_selectionne["nom"]
            adresse_magasin = magasin_selectionne["adresse"]
            image_nom = magasin_selectionne["image"]  # Obtient le nom de l'image du JSON
            ##(sys.path[1] + "/Exemples de plan/", image_nom)
            ##mettre le programme pour afficher l'image
            message = f"Vous avez sélectionné le magasin {nom_magasin} situé à l'adresse suivante :\n{adresse_magasin}"
            self.label_adresse.setText(message)

    def confirmation_button_clicked(self, button):
        if button.text() == "OK":
            print("L'utilisateur a confirmé la sélection.")
        elif button.text() == "Cancel":
            print("L'utilisateur a annulé la sélection.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
