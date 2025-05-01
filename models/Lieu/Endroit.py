from typing import List

from models.Utilitaire.Util import Util


class Endroit:
    id = 0
    liaison = []
    distance = 0
    canvas_id = None

    def __init__(self, id, liens, distance):
        self.id = id
        self.liaison = liens
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_deplacement(self, endroits):
        deplacement_final = []
        deplacement = []

        # print(len(self.liaison))
        for i in range(len(self.liaison)):
            if self.liaison[i] > 0:
                deplacement.append({
                    'value': self.liaison[i],
                    'endroit': endroits[i]
                })

        deplacement_final = [obj["endroit"] for obj in sorted(deplacement, key=lambda x: x["value"], reverse=True)]

        return deplacement_final

    def get_deplacement_libre(self, game):
        deplacements = self.get_deplacement(game.endroits)
        # print("Ce sont:")
        
        libres = []
        for deplacement in deplacements:
            if deplacement not in game.get_occupe():
                libres.append(deplacement)
                
        # for deplacement in libres:
        #     print("", deplacement.id)
            
        return libres
    
    # def best_chemin(self,occuped: List['Endroit'],but):
    #     chemin = []
    #     break_test = False
    #
    #     visited = [False, ] * 21
    #
    #     for lieu_occupe in occuped:
    #         visited[lieu_occupe.id] = True
    #
    #     visited[self.id] = True
    #     # print(visited)
    #     file = []
    #     self.enfiler(self.id+1, file)
    #     # self.enfiler(visited, self.id+1, file, chemin)
    #     while len(file) > 0 and not break_test:
    #         current = self.defiler(file)
    #         cur = int(current)
    #
    #         for u in Util.get_deplacement(current):
    #             if not visited[u-1]:
    #                 visited[u-1] = True
    #
    #                 Endroit.enfiler(u, file)
    #                 # Endroit.enfiler(visited, u, file, chemin)
    #                 if not Util.is_among(chemin, u):
    #                     chemin.append(u)
    #                     if u == but:
    #                         break_test = True
    #
    #     return chemin

    # def best_chemin_simple(self):
    #     chemin = []
    #     break_test = False
    #
    #     visited = [False, ] * 21
    #     visited[self.id] = True
    #     print(visited)
    #     file = []
    #     self.enfiler(self.id+1, file)
    #     # self.enfiler(visited, self.id+1, file, chemin)
    #     while len(file) > 0 and not break_test:
    #         current = self.defiler(file)
    #         cur = int(current)
    #
    #         for u in Util.get_deplacement(current):
    #             if not visited[u-1]:
    #                 visited[u-1] = True
    #                 # print(visited)
    #                 Endroit.enfiler(u, file)
    #                 # Endroit.enfiler(visited, u, file, chemin)
    #                 if not Util.is_among(chemin, u):
    #                     chemin.append(u)
    #                     if u == 11:
    #                         break_test = True
    #
    #     # print(chemin)
    #     return self.to_lalana(chemin)

    # def to_lalana(self,lalanas,but):
    #     val = []
    #     alefa = True
    #     cur_lalanas = lalanas
    #     retour = [self.id+1]
    #     index_limit = len(cur_lalanas)
    #     while Endroit.do_i_continue(self.id+1,cur_lalanas) and len(val)<4 and len(cur_lalanas)>0:
    #         while alefa:
    #             if len(cur_lalanas)==0: alefa=False
    #             for i in range(0, index_limit):
    #                 string = ""
    #                 temp = retour.pop(len(retour) - 1)
    #                 zeze = cur_lalanas[i]
    #                 dep = Util.get_deplacement(temp)
    #                 if Util.is_inserable(retour, cur_lalanas[i]) and cur_lalanas[i] in Util.get_deplacement(temp):
    #                     actual_value = Endroit.mbola_misy_aoriana(cur_lalanas,i,temp)
    #                     string += str(actual_value)
    #                     retour.append(temp)
    #                     retour.append(actual_value)
    #                     cur_lalanas.remove(actual_value)
    #                     index_limit -= 1
    #                     break
    #                 else:
    #                     retour.append(temp)
    #                 if i == index_limit - 1:
    #                     alefa = False
    #             if but in retour:
    #                 alefa = False
    #                 cur_lalanas.append(but)
    #                 index_limit += 1
    #                 continue
    #         val.append(retour)
    #         retour = [self.id+1]
    #         alefa = True
    #
    #     return val

    # def get_chemins(self, unautorized):
    #     chemins = []
    #     departs = Util. get_deplacement(self.id+1)
    #
    #     for depart in departs:
    #         chemin = [depart]
    #         while chemin[len(chemin)-1] != 11:
    #             chemin.append(Endroit.get_best_next(chemin[len(chemin)-1],unautorized))
    #         chemins.append(chemin)
    #
    #     return chemins
    #
    # @staticmethod
    # def chemins(position, unautorized):
    #     chemins = []
    #     departs = Util.get_deplacement(position[3])
    #
    #     for depart in departs:
    #         chemin = [depart]
    #         while chemin[len(chemin)-1] != 11:
    #             chemin.append(Endroit.get_best_next(chemin[len(chemin)-1],unautorized))
    #         chemins.append(chemin)
    #
    #     return chemins

    # @staticmethod
    # def get_best_next(index, unautorized):
    #     voisins = Util.get_deplacement(index)
    #     # print(f"unothorized {unautorized}")
    #     for voisin in voisins:
    #         if voisin == 11:
    #             return voisin
    #         if voisin not in unautorized:
    #             return voisin
    #     return None

    @staticmethod
    def best_chemin(indice,occuped):
        chemin = []
        break_test = False

        visited = [False, ] * 21

        for lieu_occupe in occuped:
            visited[lieu_occupe] = True

        visited[indice] = True
        file = []
        Endroit.enfiler(indice, file)
        while len(file) > 0 and not break_test:
            current = Endroit.defiler(file)
            cur = int(current)

            for u in Util.get_deplacement(current):
                if not visited[u]:
                    visited[u] = True

                    Endroit.enfiler(u, file)
                    if u not in chemin:
                        chemin.append(u)
                        # if u == but:
                        #     break_test = True

        return chemin

    @staticmethod
    def enfiler(index, file):
        file.append(index)

    @staticmethod
    def defiler(file):
        current = file[0]
        file.remove(current)
        return current

# print(test())
# tab = [1,2,6,3,11]
# print(Util.value_of(10,11))
# print(Endroit.mbola_misy_aoriana(tab,2,10))
# azo_aleha = Endroit.best_chemin(13,[13,2,5,16])
# print(azo_aleha)
# print(len(azo_aleha))