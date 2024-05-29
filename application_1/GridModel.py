import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import pyqtSignal

class GridModel:
    #Constructeur
    def __init__(self):
        self.gridMoved = False
        self.gridStart = [0,0]
        self.square_size = 50
        self.grid_position = []
    
    # Methodes
    def getIndex(self, pos : tuple) -> tuple :
        """
        Cette méthode permet de convertir un point de QGraphicsView en une position de la grille 
        self.grid_position.
        Paramètres : self, pos : tuple de forme (x : int, y : int)
        Return : tuple de forme (x : int, y : int)
        """
        print("start",self.gridStart)
        return ((int(pos[1]-self.gridStart[1])//self.square_size),(int(pos[0]-self.gridStart[0])//self.square_size))

    def getCase(self, pos : tuple) -> (int|list) :
        """
        Cette méthode permet d'obtenir le contenu d'une case de la grille self.grid_position
        Paramètres : self, pos : tuple de forme (x : int, y : int)
        Return : list ou int si la case ne contient pas de produits
        """
        (x,y) = self.getIndex(pos)
        return self.grid_position[x][y]

    def addItems(self,items_list : list ,pos : tuple) -> None :
        """
        Cette méthode permet d'ajouter le ou les élèments de items_list dans une case de la grille
        self.grid_position.
        Paramètres : self, items_list : list, pos : tuple de forme (x : int, y : int)
        Return : None
        """
        if items_list != []:
            (x,y) = self.getIndex(pos)
            if type(self.grid_position[x][y]) == list:
                for item in items_list:
                    self.grid_position[x][y].append(item.text())
            else :
                items = []
                for item in items_list:
                    items.append(item.text())
                self.grid_position[x][y] = items
        print(self.grid_position)

    def updateSquareSize(self, size : int) -> None :
        """
        Cette méthode permet de mettre à jour la taille des carrés de la grille. 
        Paramètres : self, size : int 
        Return : None
        """
        self.square_size = size
    
    def updateGrid(self, pixmap_height : int, pixmap_width : int) -> None :
        self.pixmap_height = pixmap_height
        self.pixmap_width = pixmap_width

        self.nb_square_height = self.pixmap_height // self.square_size
        self.nb_square_width = self.pixmap_width // self.square_size

        self.grid_position = [[0 for _ in range(self.nb_square_width)] for _ in range(self.nb_square_height)]

if __name__ == "__main__":
    test = GridModel()
    test.updateGrid(50,50)
    print(test.grid_position)
