from models.Lieu.Endroit import Endroit
from models.Utilitaire.Util import Util
from models.Vivant.Acteur import Acteur


class Police(Acteur):
    def __init__(self, noeud: Endroit):
        super().__init__(noeud)

    def my_best_action(self, liste_path):
        autorised = []
        for path in liste_path:
            if path.pop() == 11:
                autorised.append(path)
        if len(autorised) == 1:
            return autorised[0]
        else:
            taille = []
            for path in autorised:
                taille.append(len(path))
            index = Util.index_min(taille)
            return autorised[index]

    def win_label(self):
        return "Les policiers ont gagné"