import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from models.Lieu.Endroit import Endroit
import time
import tkinter
from tkinter import *
from typing import List

from models.Utilitaire.Etat2 import Etat
from models.Utilitaire.Point import Point
from models.Game import Game
from models.Utilitaire.Util import Util


class Frame(Tk):
    points = [
        Point(50, 300),  # 0
        Point(75, 181),  # 1
        Point(75, 418.2),  # 2
        Point(171, 300),  # 3
        Point(231, 25.1),  # 4
        Point(231, 300),  # 5
        Point(231, 574),  # 6
        Point(350, 0),  # 7
        Point(350, 121),  # 8
        Point(350, 181),  # 9
        Point(350, 300),  # 10
        Point(350, 418),  # 11
        Point(350, 478),  # 12
        Point(350, 600),  # 13
        Point(471, 25.5),  # 14
        Point(471, 300),  # 15
        Point(471, 574),  # 16
        Point(531, 300),  # 17
        Point(618, 186),  # 18
        Point(618, 418),  # 19
        Point(650, 300),  # 20
    ]
    game = Game()
    move_input = None
    submit = None

    cercles = []

    def __init__(self):
        super().__init__()
        self.title("Police & voleurs")
        self.geometry("1400x1000")
        canvas = Canvas(self, width=1400, height=800, bg="white")
        self.canvas = canvas
        canvas.pack(padx=5, pady=5)
        # from left,from top deb,from left
        canvas.create_line(110, 10, 110, 200)
        canvas.create_line(10, 110, 210, 110, fill="green")

        depart = [300, 100]
        centre_x = 350
        centre_y = 300
        rayon = 300
        canvas.create_oval(centre_x - rayon + depart[0], centre_y - rayon + depart[1], centre_x + rayon + depart[0],
                           centre_y + rayon + depart[1], outline="black")

        rayon_petit = 20
        # background des cercles
        # idx = 0
        for point in self.points:
            cercle = canvas.create_oval(point.x - rayon_petit + depart[0], point.y - rayon_petit + depart[1],
                                                   point.x + rayon_petit + depart[0], point.y + rayon_petit + depart[1],
                                                   outline="red",
                                                   fill="white")
            # canvas.create_text(point.x, point.y, text=str(idx))
            # idx += 1
            self.cercles.append(cercle)

        def valider():
            valeur = int(self.move_input.get())
            self.move_input.delete(0, tkinter.END)
            self.game.voleur.emplacement = self.game.endroits[valeur]
            self.update()
            self.my_turn()
            self.update()
            self.game.evaluer()
            if self.game.gagnant is not None:
                self.game.aGagner()

        def rejouer():
            self.game.init_acteur()
            self.update()

        self.move_input = tkinter.Entry(self)
        self.move_input.pack()
        self.submit = tkinter.Button(self, text="Valider", command=valider)
        self.submit.pack()

        self.rejouer = tkinter.Button(self, text="Rejouer", command=rejouer)
        self.rejouer.pack()
    
    def je_joue(self, lieu: Endroit):
        self.game.voleur.deplacer(lieu, self)
        
        # valeur = int(self.move_input.get())
        # self.move_input.delete(0, tkinter.END)
        # self.game.voleur.emplacement = self.game.endroits[valeur]
        # self.update()
        self.my_turn()
        self.update()
        self.game.evaluer()
        if self.game.gagnant is not None:
            self.game.aGagner()

    def update(self):
        rayon_petit = 20
        index = 0
        depart = [300, 100]
        canvas = self.canvas
        
        for cercle in self.cercles:
           canvas.tag_unbind(cercle, '<Button-1>')        

        # background des afaka andehanana
        for endroit in self.game.endroits:
            if endroit in self.game.voleur.get_moves(self.game):
                print("", endroit.id)
                canvas.itemconfig(self.cercles[endroit.id], fill="yellow")
                
                canvas.tag_bind(self.cercles[endroit.id], '<Button-1>', lambda event, lieu=endroit: self.je_joue(lieu))
            else:
                canvas.itemconfig(self.cercles[endroit.id], fill="white")



        # chiffres
        for point in self.points:
            canvas.create_text(point.x + depart[0], point.y + depart[1], text=index, font=("Arial", 16), fill="blue")
            index += 1

        # couleur police
        for police in self.game.polices:
            canvas.itemconfig(self.cercles[police.emplacement.id], fill="black")

        # voleur
        canvas.itemconfig(self.cercles[self.game.voleur.emplacement.id], fill="green")

        # self.game.polices[0].emplacement = self.game.endroits[self.game.polices[0].emplacement.id+1]

        # print(f"Vos choix sont {Util.get_deplacement(self.game.voleur.emplacement.id + 1)}")
        # action = int(input("Ou voulez vous aller : "))
        # self.game.voleur.deplacer(self.game.endroits[action-1])
        # self.after(1000, self.update)

    def move_police(self):
        liste = []
        taille = []
        m_voleur = Util.the_best_action(self.game.voleur.emplacement.best_chemin(self.game.get_occupe(), 11), 11)
        for police in self.game.polices:
            chemin = Util.the_best_action(police.emplacement.best_chemin(self.game.get_occupe(), m_voleur[1]),
                                          m_voleur[1])
            liste.append(chemin)
            taille.append(len(chemin))

        policier = Util.index_min(taille)
        print(policier)
        print(f"lasa -> {liste[policier][1]}")
        self.game.polices[policier].deplacer(self.game.endroits[liste[policier][1] - 1], self)


    def my_turn(self):
        positions = []
        positions.append(self.game.voleur.emplacement.id)
        for police in self.game.polices:
            positions.append(police.emplacement.id)

        action = Etat.minimax(positions,4,False)
        self.game.polices[0].deplacer(self.game.endroits[action[1]], self)
        self.game.polices[1].deplacer(self.game.endroits[action[2]], self)
        self.game.polices[2].deplacer(self.game.endroits[action[3]], self)



window = Frame()
window.update()
window.mainloop()
