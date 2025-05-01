# from models.Acteur import Acteur
# from models.Utilitaire.Util import Util
# from models.Voleur import Voleur
import random
from typing import List
import tkinter
from tkinter import *

from models.Utilitaire.Etat2 import Etat
from models.Utilitaire.Util import Util
from models.Lieu.Endroit import Endroit
from models.Vivant.Acteur import Acteur
from models.Vivant.Police import Police
from models.Vivant.Voleur import Voleur


class Game:
    endroits: List[Endroit] = []
    voleur: Voleur = None
    polices: List[Police] = []
    tour = 0
    profondeur = 3
    liens = []
    gagnant: Acteur = None

    def __init__(self):
        self.initialiser_liens()
        self.init_acteur()

    def initialiser_liens(self):
        liens = Util.liens

                   # 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21
        distances = [3, 3, 3, 2, 3, 1, 3, 3, 2, 1, 0, 1, 2, 3, 3, 1, 3, 2, 3, 3, 3]

        self.liens = liens
        for i in range(21):
            # print(i)
            self.endroits.append(Endroit(i, self.liens[i], distances[i]))

    def get_deplacement_endroit(self, i):
        return self.endroits[i].get_deplacement(self.endroits)

    def get_all_possibilities(self):
        return self.endroits

    def get_occupe(self):
        liste = [Endroit]
        liste.append(self.voleur.emplacement)
        for police in self.polices:
            liste.append(police.emplacement)
        return liste

    def get_possibilities(self):
        occupe = self.get_occupe()
        liste = []
        for i in range(len(self.endroits)):
            if not Util.is_among(occupe, self.endroits[i]):
                liste.append(self.endroits[i])
        return liste

    def init_acteur(self):
        self.voleur = Voleur(self.endroits[10])
        # print("voleur " + str(self.voleur.emplacement.id))
        self.polices = [
            Police(self.endroits[5]),
            Police(self.endroits[9]),
            Police(self.endroits[15])
                        ]

    # def init_acteur(self):
    #     self.voleur = Voleur(self.endroits[0])
    #     # print("voleur " + str(self.voleur.emplacement.id))
    #     self.polices = [
    #         Police(self.endroits[4]),
    #         Police(self.endroits[5]),
    #         Police(self.endroits[13])
    #                     ]

    def get_coup_police(self):
        liste = []
        coup_voleur = Util.the_best_action(self.voleur.emplacement.best_chemin(self.get_occupe(), 11), 11)
        for police in self.polices:
            liste.append(Util.the_best_action(police.emplacement.best_chemin(self.get_occupe(), coup_voleur[1]), coup_voleur[1]))

        return liste

    def status(self):
        print(f"Voleur: {self.voleur.emplacement.id+1}")
        for police in self.polices:
            print(f"Police: {police.emplacement.id+1}")

    def occuped(self):
        occupe = []
        occupe.append(self.voleur.emplacement.id)
        for police in self.polices:
            occupe.append(police.emplacement.id)
        return occupe

    def evaluer(self):
        if self.voleur.emplacement.id == 10:
            self.gagnant = self.voleur

        if len(Util.get_deplacement_possible(self.voleur.emplacement.id,self.occuped())) == 0:
            self.gagnant = self.polices[0]

    def aGagner(self):
        win_f = tkinter.Tk()
        win_f.title("Someone win")
        win_f.geometry("200x200")
        texte = self.gagnant.win_label()
        win_label = tkinter.Label(win_f, text=texte)
        win_label.pack()
        win_f.mainloop()




# gome = Game()
# otat = Etat(gome)
# for etat in Etat.descendre(otat.positions,0, gome):
#     print(etat)
#
# print("Val : " + str(max(Etat.descendre(otat.positions,0, gome))))
