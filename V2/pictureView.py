from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class pictureView(QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self.fpath = ""
        
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene = QGraphicsScene()
        self.scene.addText("Aucun projet n'est actuellement ouvert.")

        self.setScene(self.scene)
        self.setWindowTitle("QGraphicsView")

    def setPixmap(self,fname):
        self.scene.clear()
        self.fpath = fname
        
        self.pixmap = QPixmap(self.fpath)
        self.pixmap = self.pixmap.scaled(int(self.width()), int(self.height()), Qt.AspectRatioMode.KeepAspectRatio)
        self.pixmap_height = self.pixmap.height()
        self.pixmap_width = self.pixmap.width()
        
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)
        