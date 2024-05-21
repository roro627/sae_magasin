import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import pyqtSignal

class GridViewWidget(QGraphicsView):
    def __init__(self):
        super().__init__()
        file_path = "/Users/Alexis/Desktop/Mes fichiers SAE/sae_magasin/Exemples de plans/plan3.png"
        self.setMouseTracking(True)
        #self.view.setEnabled(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene = QGraphicsScene()

        # Load and display the image
        self.pixmap = QPixmap(file_path)
        self.pixmap_height = self.pixmap.height()
        self.pixmap_width = self.pixmap.width()
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)

        #self.scene.setBackgroundBrush(QBrush(pixmap))
        #self.scene.setForegroundBrush()

        self.setScene(self.scene)
        #self.setFixedSize(QSize(600,hauteur))
        self.setWindowTitle("QGraphicsView")

    def mousePressEvent(self, event):
        print(f"Mouse pressed at position: {event.position().toPoint()}")
        super().mousePressEvent(event)

    def createGrid(self):
        group = QGraphicsItemGroup()
        group.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable, True)

        nb_square1 = int(self.pixmap_height/40)+1
        nb_square2 = int(self.pixmap_width/40)+1

        for i in range(nb_square1):
            for j in range(nb_square2):
                square = QGraphicsRectItem(0+j*40,0+i*40,40,40) 
                square.setPen(QColor("black"))
                group.addToGroup(square)
            self.scene.addItem(group)

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = GridViewWidget("Users/Alexis/Desktop/Mes fichiers SAE/sae_magasin/Exemples de plans/plan3.png") 
    window.show()
    sys.exit(app.exec())