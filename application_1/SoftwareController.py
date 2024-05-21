from PyQt6.QtCore import QObject, pyqtSlot
from SoftwareModel import SoftwareModel
from SoftwareView import SoftwareView
from PyQt6.QtWidgets import QApplication
import sys


class SoftwareController(QObject):
    def __init__(self):
        super().__init__()

        # Initialiser la vue et le modèle
        self.view = SoftwareView()
        self.model = SoftwareModel()

        # Connecter les signaux de la vue aux slots du contrôleur
        self.view.dial.planButtonClicked.connect(self.nouveauPlanProjet)
        self.view.dial.finishButtonClicked.connect(self.nouveauProjet)
        self.view.pr.itemAdded.connect(self.newItem)
        self.view.pr.itemDelet.connect(self.itemRemove)

        self.view.openProjectDialog.openClicked.connect(self.ouvrirProjet)

        self.view.saveClicked.connect(self.enregistrerProjet)

    def newItem(self, item):
        self.model.addProduct(item)

    def itemRemove(self, item):
        self.model.removeProduct(item)

    def nouveauPlanProjet(self,fname):
        self.model.setFilePathPlan(fname)

    def nouveauProjet(self):
        # Gérer l'action nouveau projet
        info = self.view.dial.getAllInfo()
        self.model.update(info)
        self.view.grid.setPixmap(self.model.filePathPlan)
        self.enregistrerProjet()

    def ouvrirProjet(self, fname):
        # Gérer l'action ouvrir projet
        self.model.setFilePath(fname)
        self.model.ouvrirProjet()
        self.view.grid.setPixmap(self.model.filePathPlan)

    def enregistrerProjet(self):
        # Gérer l'action enregistrer projet
        self.model.enregistrerProjet()

    def show(self):
        # Afficher la vue
        self.view.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    controller = SoftwareController()
    controller.show()

    sys.exit(app.exec())
