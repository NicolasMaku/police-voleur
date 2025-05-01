class Util(object):
    liens = [
       # 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5 -- enlevé
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 7
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 8
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 9
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 10
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # 11
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # 12
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # 13
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 14
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 15 -- enlevé
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],  # 16
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],  # 17
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],  # 18
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],  # 19
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],  # 20
    ]
    @staticmethod
    def is_among(tab,element):
        for member in tab:
            if member == element: return True
        return False
    @staticmethod
    def get_deplacement(index):
        deplacement = list()
        number = len(Util.liens[index])
        for i in range(len(Util.liens[index])):
            if Util.liens[index][i] > 0:
                deplacement.append({
                    'value': Util.liens[index][i],
                    'endroit': i
                })
        retour = [obj["endroit"] for obj in sorted(deplacement, key=lambda x: x["value"], reverse=True)]
        return retour

    @staticmethod
    def get_deplacement_possible(index,obstacle):
        deplacement = list()
        number = len(Util.liens[index])
        for i in range(len(Util.liens[index])):
            if Util.liens[index][i] > 0 and i not in obstacle:
                deplacement.append(i)

        return deplacement

    # @staticmethod
    # def is_inserable(chemin,element):
    #     for member in chemin:
    #         if Util.is_among(Util.get_deplacement(member), element):
    #             return False
    #     return True

    # @staticmethod
    # def f_count(index,retour):
    #     deplacement = Util.get_deplacement(index)
    #     number = 0
    #     for dep in deplacement:
    #         if dep in retour:
    #             number += 1
    #     return number

    @staticmethod
    def value_of(ligne,col):
        return Util.liens[ligne][col-1]

    @staticmethod
    def index_max(tableau):
        if not tableau:
            return None
        max_value = max(tableau)
        return tableau.index(max_value)

    @staticmethod
    def index_min(tableau):
        if not tableau:
            return None
        max_value = min(tableau)
        return tableau.index(max_value)

    @staticmethod
    def the_best_action(liste_path, but):
        autorised = []
        for path in liste_path:
            if path[len(path)-1] == but:
                autorised.append(path)
        if len(autorised) == 1:
            return autorised[0]
        else:
            taille = []
            for path in autorised:
                taille.append(len(path))
            index = Util.index_min(taille)
            if index is None:
                return liste_path[0]
                # return "Random"
            return autorised[index]


print(Util.get_deplacement(13))
