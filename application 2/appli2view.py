import sys
import os
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QWidget
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choix du Magasin")
        
        # Chargement des magasins depuis le fichier JSON
        with open(sys.path[0] + "/magasins.json", "r") as f:
            self.magasins_disponibles = json.load(f)

        # Interface utilisateur
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()  # Utiliser un layout vertical pour placer les éléments en haut
        main_widget.setLayout(main_layout)

        # Layout pour les éléments de magasin
        magasin_layout = QHBoxLayout()
        self.label_magasin = QLabel("Sélectionnez un magasin:")
        magasin_layout.addWidget(self.label_magasin)

        self.combo_magasin = QComboBox()
        for magasin in self.magasins_disponibles:
            self.combo_magasin.addItem(magasin["nom"])
        magasin_layout.addWidget(self.combo_magasin)

        self.btn_selectionner = QPushButton("Sélectionner")
        self.btn_selectionner.clicked.connect(self.selectionner_magasin)
        magasin_layout.addWidget(self.btn_selectionner)

        main_layout.addLayout(magasin_layout)

        # Label pour afficher l'adresse
        self.label_adresse = QLabel("")
        main_layout.addWidget(self.label_adresse)

        # Layout pour afficher l'image
        self.label_image = QLabel()
        main_layout.addWidget(self.label_image)

        # Montrer la fenêtre maximisée
        self.showMaximized()

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
            plan_magasin = magasin_selectionne["image"]

            message = f"Vous avez sélectionné le magasin {nom_magasin} situé à l'adresse suivante :\n{adresse_magasin}"
            self.label_adresse.setText(message)
        
            current_dir = sys.path[0]
            parent_dir = os.path.dirname(current_dir)

            # Chargement de l'image
            image_path = os.path.join(parent_dir, "Exemples de plans", plan_magasin)
            pixmap = QPixmap(image_path)

            # Redimensionnement de l'image à 300x300
            pixmap = pixmap.scaled(1000, 700)

            self.label_image.setPixmap(pixmap)

    def confirmation_button_clicked(self, button):
        if button.text() == "OK":
            print("L'utilisateur a confirmé la sélection.")
        elif button.text() == "Cancel":
            print("L'utilisateur a annulé la sélection.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
