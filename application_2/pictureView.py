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

    def setPixmap(self, fname, case_taille, nombre_cases_x, nombre_cases_y):
        self.scene.clear()
        self.fpath = fname
        
        self.pixmap = QPixmap(self.fpath)
        self.pixmap = self.pixmap.scaled(int(case_taille * nombre_cases_x), int(case_taille * nombre_cases_y), Qt.AspectRatioMode.KeepAspectRatio)
        self.pixmap_height = self.pixmap.height()
        self.pixmap_width = self.pixmap.width()
        
        image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(image_item)
    


    def drawPath(self, line_tab, position_debut_grille, case_taille, nombre_cases_x, nombre_cases_y):
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

    
    def drawProduct(self, positionProduct,position_debut_grille, case_taille, nombre_cases_x, nombre_cases_y):
        group = QGraphicsItemGroup()

        square_size = case_taille

        # affiche chaque case de la grille seulement si elle est dans le chemin
        for i in range(nombre_cases_y):
            for j in range(nombre_cases_x):
                if (i + position_debut_grille[0], j + position_debut_grille[1]) == positionProduct:
                    point = QGraphicsRectItem(j*square_size, i*square_size, square_size, square_size)
                    point.setPen(QColor("red"))
                    group.addToGroup(point)
                
        self.scene.addItem(group) 