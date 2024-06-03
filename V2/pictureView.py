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
    
    def drawPath(self,line_tab,square_size):
        self.group = QGraphicsItemGroup()
        for elt in line_tab:
            line = QGraphicsRectItem(elt[1]*square_size+20,elt[0]*square_size+20,square_size,square_size)
            line.setPen(QColor("red"))
            self.group.addToGroup(line)
        #self.group.setRotation(180)
        self.scene.addItem(self.group)
