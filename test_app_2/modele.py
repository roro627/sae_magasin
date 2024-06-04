import json
import sys

class MagasinModel:
    def __init__(self):
        self.charger_magasins()

    def charger_magasins(self):
        with open(sys.path[0] + "/magasins.json", "r") as f:
            self.magasins_disponibles = json.load(f)

    def get_magasins(self):
        return self.magasins_disponibles
