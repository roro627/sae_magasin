import sys
import os
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QWidget
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choix du Magasin")
        self.resize(800, 200)  # Ajuster la taille pour laisser de l'espace à l'image

        # Chargement des magasins depuis le fichier JSON
        with open(sys.path[0] + "/magasins.json", "r") as f:
            self.magasins_disponibles = json.load(f)

        # Interface utilisateur
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout()  # Utiliser un layout horizontal pour placer les éléments côte à côte
        main_widget.setLayout(main_layout)

        magasin_layout = QVBoxLayout()
        self.label_magasin = QLabel("Sélectionnez un magasin:")
        magasin_layout.addWidget(self.label_magasin)

        self.combo_magasin = QComboBox()
        for magasin in self.magasins_disponibles:
            self.combo_magasin.addItem(magasin["nom"])
        magasin_layout.addWidget(self.combo_magasin)

        self.btn_selectionner = QPushButton("Sélectionner")
        self.btn_selectionner.clicked.connect(self.selectionner_magasin)
        magasin_layout.addWidget(self.btn_selectionner)

        self.label_adresse = QLabel("")
        magasin_layout.addWidget(self.label_adresse)

        main_layout.addLayout(magasin_layout)

        # Ajout d'une image à droite
        image_layout = QVBoxLayout()
        self.label_image = QLabel()
        
        
        current_dir = os.path.abspath(os.path.dirname(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))


        pixmap = QPixmap(parent_dir + "./Exemples de plans" + "/plan1.jpg")  
        self.label_image.setPixmap(pixmap)
        image_layout.addWidget(self.label_image)

        main_layout.addLayout(image_layout)
        main_widget.setLayout(main_layout)
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

            message = f"Vous avez sélectionné le magasin {nom_magasin} situé à l'adresse suivante :\n{adresse_magasin}"
            self.label_adresse.setText(message)

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
