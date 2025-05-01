import copy
from math import inf
from typing import List

from models.Lieu.Endroit import Endroit
from models.Utilitaire import bof
from models.Utilitaire.Util import Util
from models.Vivant.Police import Police
from models.Vivant.Voleur import Voleur


class Etat:
    positions = []



    def __init__(self,game):
        for police in game.polices:
            self.positions.append(police.emplacement.id)
        self.positions.append(game.voleur.emplacement.id)

    # @staticmethod
    # def descendre(positions,profondeur, game):
    #
    #     if profondeur == 1:
    #         return Etat.valeur(positions)
    #     else:
    #         retour = []
    #         for etat_p in Etat.getEtat(positions):
    #             cur_etat = Etat.descendre(etat_p,profondeur + 1, game)
    #             for etat in cur_etat:
    #                 print(f"etat : {etat} {profondeur}")
    #                 retour.append(max(etat))
    #         return retour

    #
    #
    # @staticmethod
    # def etat_from(game):
    #     return Etat(game.polices,game.voleur)

    @staticmethod
    def valeur(positions):
        obstacle = []
        distance = 0
        for i in range(1,4):
            obstacle.append(positions[i])
            distance += len(bof.parcours_largeur(Util.liens,positions[i],positions[0],obstacle))

        return len(Endroit.best_chemin(positions[0],positions)) - len(bof.parcours_largeur(Util.liens,positions[0],10,obstacle)) + distance

    @staticmethod
    def getActions(positions) -> []:
        rep = []
        for i in range(1,4):
            # line = []
            for endroit in Util.get_deplacement(positions[i]):
                if endroit not in positions:
                    copie = positions[:]
                    copie[i] = endroit
                    rep.append(copie[:])
        return rep

    @staticmethod
    def getActions_voleur(positions) -> []:
        rep = []
        for i in range(0, 1):
            # line = []
            for endroit in Util.get_deplacement(positions[i]):
                if endroit not in positions:
                    copie = positions[:]
                    copie[i] = endroit
                    rep.append(copie[:])
        return rep

    # @staticmethod
    # def minimax(etat, profondeur, estMax):
    #     if profondeur == 1:
    #         return Etat.valeur(etat)
    #     if estMax:
    #         v = -inf
    #         if Etat.est_une_liste_d_entiers(etat):
    #             for mouvement in Etat.getActions(etat):
    #                 v = max(v,Etat.minimax(mouvement,profondeur-1,False))
    #         else:
    #             for move in etat:
    #                 for mouvement in Etat.getActions(move):
    #                     v = max(v, Etat.minimax(mouvement, profondeur - 1, False))
    #         return v
    #     else:
    #         v = +inf
    #         if Etat.est_une_liste_d_entiers(etat):
    #             for mouvement in Etat.getActions_voleur(etat):
    #                 v = min(v,Etat.minimax(mouvement,profondeur-1,True))
    #         else:
    #             for move in etat:
    #                 for mouvement in Etat.getActions(move):
    #                     v = min(v, Etat.minimax(mouvement, profondeur - 1, True))
    #
    #         return v
    #
    # @staticmethod
    # def est_une_liste_d_entiers(liste):
    #     return all(isinstance(element, int) for element in liste)

    @staticmethod
    def minimax(etat, profondeur, estMax):
        if profondeur == 0:
            return Etat.valeur(etat)
        if estMax:
            v = -inf
            best_move = []
            for mouvement in Etat.getActions_voleur(etat):
                value = Etat.minimax(mouvement, profondeur - 1, False)
                if v < value:
                    best_move = mouvement
                v = max(v, value)
            if profondeur == 4:
                return best_move
            else:
                return v
        else:
            v = +inf
            best_move = []
            for mouvement in Etat.getActions(etat):
                value = Etat.minimax(mouvement, profondeur - 1, True)
                if v > value:
                    best_move = mouvement
                v = min(v, value)
            if profondeur == 4:
                return best_move
            else:
                return v

    # @staticmethod
    # def minimax(etat, profondeur, estMax):
    #     if profondeur == 0:
    #         return Etat.valeur(etat)
    #     if estMax:
    #         v = -inf
    #         best_move = []
    #         for mouvement in Etat.getActions(etat):
    #             if v < Etat.minimax(mouvement, profondeur - 1, True):
    #                 best_move = mouvement
    #             v = max(v, Etat.minimax(mouvement, profondeur - 1, False))
    #         if profondeur == 3:
    #             return best_move
    #         else:
    #             return v
    #     else:
    #         v = +inf
    #         best_move = []
    #         for mouvement in Etat.getActions_voleur(etat):
    #             if v > Etat.minimax(mouvement, profondeur - 1, True):
    #                 best_move = mouvement
    #             v = min(v, Etat.minimax(mouvement, profondeur - 1, True))
    #         if profondeur == 3:
    #             return best_move
    #         else:
    #             return v

    # def getEtat(self) -> []:
    #     rep = []
    #     for i in range(0,3):
    #         line = []
    #         for endroit in Util.get_deplacement(self.positions[i]):
    #             copie = self.positions[:]
    #             copie[i] = endroit
    #             line.append(copie[:])
    #         rep.append(line)
    #     return rep

    # def __str__(self):
        # string = ""
        # for police in self.polices:
        #     string += "police: " + str(police.emplacement.id)
        # string += "voleur: " + str(self.voleur.emplacement.id)
        # string += "\n"
        #
        #
        # return string


# print(f"val :  {Etat.minimax([6,3,10,15],4,False)}")
# print(f"val :  {Etat.minimax([11,5,9,15],3,False)}")
# print(Util.get_deplacement(1))