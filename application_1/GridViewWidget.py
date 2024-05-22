import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import pyqtSignal

class GridViewWidget(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        #self.view.setEnabled(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene = QGraphicsScene()
        self.scene.addText("Aucun projet n'est actuellement ouvert.")

        #self.scene.setBackgroundBrush(QBrush(pixmap))
        #self.scene.setForegroundBrush()

        self.setScene(self.scene)
        #self.setFixedSize(QSize(600,hauteur))
        self.setWindowTitle("QGraphicsView")

    def mousePressEvent(self, event):
        print(f"Mouse pressed at position: {event.position().toPoint()}")
        super().mousePressEvent(event)
    
    def setPixmap(self,fname):
        self.pixmap = QPixmap(fname)
        self.pixmap_height = self.pixmap.height()
        self.pixmap_width = self.pixmap.width()
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)

    def createGrid(self,square_size : int):
        self.scene.clear()
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)
        group = QGraphicsItemGroup()
        group.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable, True)

        nb_square1 = int(self.pixmap_height/square_size)+1
        nb_square2 = int(self.pixmap_width/square_size)+1

        for i in range(nb_square1):
            for j in range(nb_square2):
                square = QGraphicsRectItem(0+j*square_size,0+i*square_size,square_size,square_size) 
                square.setPen(QColor("black"))
                group.addToGroup(square)
            self.scene.addItem(group)