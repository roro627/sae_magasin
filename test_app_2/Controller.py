import sys
import os
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QPixmap
from modele import MagasinModel
from View import MainWindow

class MagasinController:
    def __init__(self):
        self.model = MagasinModel()
        self.view = MainWindow(self)

    def selectionner_magasin(self):
        confirmation_box = QMessageBox(self.view)
        confirmation_box.setText('Etes-vous sûr de prendre ce magasin ?')
        confirmation_box.setWindowTitle("Confirmation")
        confirmation_box.setIcon(QMessageBox.Icon.Information)
        confirmation_box.addButton(QMessageBox.StandardButton.Cancel)
        confirmation_box.addButton(QMessageBox.StandardButton.Ok)
        confirmation_box.setDefaultButton(QMessageBox.StandardButton.Cancel)
        confirmation_result = confirmation_box.exec()

        if confirmation_result == QMessageBox.StandardButton.Ok:
            index = self.view.combo_magasin.currentIndex()
            magasin_selectionne = self.model.get_magasins()[index]
            nom_magasin = magasin_selectionne["nom"]
            adresse_magasin = magasin_selectionne["adresse"]
            plan_magasin = magasin_selectionne["image"]

            message = f"Vous avez sélectionné le magasin {nom_magasin} situé à l'adresse suivante :\n{adresse_magasin}"
            self.view.label_adresse.setText(message)
        
            current_dir = sys.path[0]
            parent_dir = os.path.dirname(current_dir)

            # Chargement de l'image
            image_path = os.path.join(parent_dir, "Exemples de plans", plan_magasin)
            pixmap = QPixmap(image_path)

            # Redimensionnement de l'image
            pixmap = pixmap.scaled(1000, 700)

            self.view.label_image.setPixmap(pixmap)

    def add_item(self, item_name):
        self.view.selected_items.addItem(item_name)

    def delete_item(self, item_name):
        for i in range(self.view.selected_items.count()):
            if self.view.selected_items.item(i).text() == item_name:
                self.view.selected_items.takeItem(i)
                break

def main():
    app = QApplication(sys.argv)
    controller = MagasinController()
    controller.view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
