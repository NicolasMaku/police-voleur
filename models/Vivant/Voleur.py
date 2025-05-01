from typing import List

from models.Lieu.Endroit import Endroit
from models.Vivant.Acteur import Acteur


class Voleur(Acteur):
    def __init__(self, lieu: Endroit):
        super().__init__(lieu)

    # def get_best_move(self,endroits: List[Endroit]):
    #     arbre = List[Endroit]
    #     arbre = self.emplacement.get_deplacement(endroits)
    #
    #     for i in range(len(arbre)):
    #         print("# " + str(arbre[i].id) + " #")
    #         arbre[i] = arbre[i].get_deplacement(endroits)
    #         for arb in arbre[i]:
    #             print(arb.id)
    #
    #     return arbre

    def win_label(self):
        return "le voleur a gagné"