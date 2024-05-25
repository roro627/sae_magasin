import sys,json,os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import pyqtSignal

class GridModel:
    def __init__(self):
        self.gride_Moved = False
        self.square_size = 50
    
    # Methods
    def getIndex(self, pos : tuple) -> tuple :
        return (int(pos[1]//self.square_size),int(pos[0]//self.square_size))

    def getCase(self, pos : tuple):
        (x,y) = self.getIndex(pos)
        return self.grid_position[y][x]

    def addItems(self,items_list,pos):
        (x,y) = self.getIndex(pos)
        if type(self.grid_position[y][x]) == list:
            for item in items_list:
                self.grid_position[y][x].append(item.text())
        else :
            items = []
            for item in items_list:
                items.append(item.text())
            self.grid_position[y][x] = items
        print(self.grid_position)

    def updateSquareSize(self, size : int):
        self.square_size = size
    
    def updateGrid(self, pixmap_height : int, pixmap_width : int):
        self.pixmap_height = pixmap_height
        self.pixmap_width = pixmap_width

        self.nb_square_height = self.pixmap_height // self.square_size
        self.nb_square_width = self.pixmap_width // self.square_size

        self.grid_position = [[0 for _ in range(self.nb_square_width)] for _ in range(self.nb_square_height)]

if __name__ == "__main__":
    test = GridModel()
    test.updateGrid(50,50)
    print(test.grid_position)
