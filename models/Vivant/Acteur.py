from models.Lieu.Endroit import Endroit
from abc import ABCMeta, abstractmethod


class Acteur(metaclass=ABCMeta):
    emplacement: Endroit = None

    def __init__(self, emplacement: Endroit):
        self.emplacement = emplacement

    def get_moves(self, game):
        empty = []
        for voisin in self.emplacement.get_deplacement(game.endroits):
            empty.append(voisin)
        return empty

    def deplacer(self, lieu: Endroit, frame):
        self.emplacement = lieu
        frame.update()
        # print("kk")

    @abstractmethod
    def win_label(self):
        pass
