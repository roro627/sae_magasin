from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class pictureView(QGraphicsView):
    def __init__(self):
        """
        Initialise la vue de l'image.
        """
        super().__init__()
        
        self.fpath = ""
        
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene = QGraphicsScene()
        self.scene.addText("Aucun projet n'est actuellement ouvert.")

        self.setScene(self.scene)
        self.setWindowTitle("QGraphicsView")
    
    mouseClicked = pyqtSignal(tuple)
    
    def mousePressEvent(self, event):
        items = self.items(event.pos())
        for item in items:
            if type(item) is QGraphicsPixmapItem:
                pos = item.mapFromScene(self.mapToScene(event.pos()))
                pos = (int(pos.x()),int(pos.y()))
                self.mouseClicked.emit(pos)
        super().mousePressEvent(event)

    def setPixmap(self, fname: str, case_taille: int, nombre_cases_x: int, nombre_cases_y: int):
        """
        Définit le pixmap pour l'image.
        Args:
            fname (str): Le nom du fichier de l'image.
            case_taille (int): La taille de la case.
            nombre_cases_x (int): Le nombre de cases en x.
            nombre_cases_y (int): Le nombre de cases en y.
        """
        self.scene.clear()
        self.fpath = fname
        
        self.pixmap = QPixmap(self.fpath)
        self.pixmap = self.pixmap.scaled(int(case_taille * nombre_cases_x), int(case_taille * nombre_cases_y), Qt.AspectRatioMode.KeepAspectRatio)
        self.pixmap_height = self.pixmap.height()
        self.pixmap_width = self.pixmap.width()
        
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)
    


    def drawPath(self, line_tab: list, position_debut_grille: tuple, case_taille: int, nombre_cases_x: int, nombre_cases_y: int) -> QGraphicsItemGroup:
        """
        Dessine le chemin sur l'image.
        Args:
            line_tab (list): Une liste de tuples représentant le chemin.
            position_debut_grille (tuple): Un tuple représentant la position de début de la grille.
            case_taille (int): La taille de la case.
            nombre_cases_x (int): Le nombre de cases en x.
            nombre_cases_y (int): Le nombre de cases en y.
        """
        group = QGraphicsItemGroup()

        square_size = case_taille

        # affiche chaque case de la grille seulement si elle est dans le chemin
        for i in range(nombre_cases_y):
            for j in range(nombre_cases_x):
                if (i + position_debut_grille[0], j + position_debut_grille[1]) in line_tab:
                    point = QGraphicsRectItem(j*square_size, i*square_size, square_size, square_size)
                    point.setPen(QColor("black"))
                    group.addToGroup(point)
                
        self.scene.addItem(group)
        
        return group

    
    def drawProduct(self, positionProduct: tuple, position_debut_grille: tuple, case_taille: int, nombre_cases_x: int, nombre_cases_y: int):
        """
        Dessine le produit sur l'image.
        Args:
            positionProduct (tuple): Un tuple représentant la position du produit.
            position_debut_grille (tuple): Un tuple représentant la position de début de la grille.
            case_taille (int): La taille de la case.
            nombre_cases_x (int): Le nombre de cases en x.
            nombre_cases_y (int): Le nombre de cases en y.
        """
        group = QGraphicsItemGroup()

        square_size = case_taille

        # affiche chaque case de la grille seulement si elle est dans le chemin
        for i in range(nombre_cases_y):
            for j in range(nombre_cases_x):
                if (i + position_debut_grille[0], j + position_debut_grille[1]) == positionProduct:
                    point = QGraphicsRectItem(j*square_size, i*square_size, square_size, square_size)
                    pen = QPen(QColor("red"))
                    pen.setWidth(2) #change la largeur du contour
                    point.setPen(pen)
                    group.addToGroup(point)
                
        self.scene.addItem(group) 
        return group
        
    def clearProduct(self, graphic_item):
        self.scene.removeItem(graphic_item)