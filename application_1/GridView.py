import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import pyqtSignal

# -----------------------------------------------------------------------------
# --- classe GridView
# -----------------------------------------------------------------------------

class GridView(QGraphicsView):
    # Constructeur
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene = QGraphicsScene()
        self.scene.addText("Aucun projet n'est actuellement ouvert.")
        self.setScene(self.scene)
        self.setWindowTitle("QGraphicsView")
    
    mouseClicked = pyqtSignal(tuple)

    def mouseReleaseEvent(self, event):
        """
        Cette méthode est appelée lorsque le bouton de la souris est relâché.
        Elle parcourt les éléments visuels à la position de l'événement et émet un signal si un élément de type QGraphicsPixmapItem est trouvé.
        
        Paramètres :self (GridView) : L'instance de la classe GridView.
                    event (QMouseEvent) : L'événement de souris qui s'est produit.
        Return :None
        """
        items = self.items(event.pos())
        for item in items:
            if type(item) is QGraphicsPixmapItem:
                # Convertion de la postion pour correspondre à la postion du plan.
                pos = item.mapFromScene(self.mapToScene(event.pos()))
                pos = (int(pos.x()),int(pos.y()))
                self.mouseClicked.emit(pos)
        super().mouseReleaseEvent(event)

    def setPixmap(self,fname):
        """
        Définit l'image pour la vue.
        
        Paramètres : fname (str) : Le nom du fichier de l'image à définir comme image de la vue.
        Return : None
        """
        self.pixmap = QPixmap(fname)
        self.pixmap = self.pixmap.scaled(int(self.width()), int(self.height()), Qt.AspectRatioMode.KeepAspectRatio)
        self.pixmap_height = self.pixmap.height()
        self.pixmap_width = self.pixmap.width()
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)

    def gridIsMovable(self):
        """
        Cette méthode permet de rendre le groupe d'éléments de la grille déplaçable.
        
        Paramètre : self (GridView) : L'instance de la classe GridView.
        Return : None
        """
        self.group.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable, True)
    
    def gridIsNotMovable(self):
        """
        Cette méthode permet de rendre le groupe d'éléments de la grille non déplaçable.
        
        Paramètre : self (GridView) : L'instance de la classe GridView.
        Return : None
        """
        self.group.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable, False)

    def createGrid(self,square_size : int, gridIsMovable : bool, gridBegin : tuple):
        """
        Crée une grille dans la vue de graphique.
        Elle efface la scène actuelle, ajoute une image à la scène, crée un groupe d'éléments pour la grille,
        et ajoute des rectangles à ce groupe pour former la grille.
    
        Paramètres :self (GridView) : L'instance de la classe GridView.
                    square_size (int) : La taille des carrés de la grille.
                    gridIsMovable (bool) : Si True, le groupe d'éléments de la grille est déplaçable.
                    gridBegin (tuple) : La position de départ de la grille dans la vue de graphique.
        Return :None
        """
        self.scene.clear()
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)
        self.group = QGraphicsItemGroup()
        if gridIsMovable :
            self.gridIsMovable()

        nb_square1 = int(self.pixmap_height/square_size)+1
        nb_square2 = int(self.pixmap_width/square_size)+1

        for i in range(nb_square1):
            for j in range(nb_square2):
                square = QGraphicsRectItem(gridBegin[0]+j*square_size,gridBegin[1]+i*square_size,square_size,square_size) 
                square.setPen(QColor("black"))
                self.group.addToGroup(square)
        self.scene.addItem(self.group)



