import pyxel
from collections import deque
from random import randint


class App():

    def __init__(self) -> None:

        pyxel.init(100,100, title="jeu de la vie")

        self.plateau = [[0 for _ in range(pyxel.height)] for _ in range(pyxel.width)]

        self.run = False
        self.speed_tour = 40
        self.decalage = 0

        print("-------------------\n jeux de la vie \n clique droit pour poser cellule \n P pour lancer ou mettre sur pause la simulation \n ------------------")

        pyxel.run(self.update,self.draw)

    def update(self):

        self.test_input()

        self.test_run()

    def test_run(self):

        if self.run:

            if (pyxel.frame_count + self.decalage) % self.speed_tour == 0:

                self.check_tour()

    def test_input(self):

        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):

            self.plateau[pyxel.mouse_y][pyxel.mouse_x] = 1

        if pyxel.btnp(pyxel.KEY_P):

            if self.run:
                self.run = False
            else:
                self.run = True
                self.decalage = -(pyxel.frame_count % self.speed_tour - 1)

    def draw(self):

        pyxel.cls(7)

        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 1, 1, 8)

        self.draw_plateau()

    def draw_plateau(self):

        for r in range(len(self.plateau)):

            for c in range(len(self.plateau[0])):

                if self.plateau[r][c] == 1:
                    pyxel.rect(c, r, 1, 1, 0)

    def check_tour(self):

        liste_with_voisin = []

        for r in range(len(self.plateau)):

            liste = []

            for c in range(len(self.plateau[0])):

                liste.append(self.get_nb_voisin(r,c))

            liste_with_voisin.append(liste)


        for r in range(len(self.plateau)):


            for c in range(len(self.plateau[0])):

                nb_voisin = liste_with_voisin[r][c]

                if self.plateau[r][c] == 1:

                    if nb_voisin < 2 or nb_voisin > 3:

                        self.plateau[r][c] = 0

                else:

                    if nb_voisin == 3:

                        self.plateau[r][c] = 1
        

    def get_nb_voisin(self, r, c) -> int:

        cmpt = 0
        
        if r < len(self.plateau)-1:
            if self.plateau[r+1][c] == 1:
                cmpt += 1

        if r > 0:
            if self.plateau[r-1][c] == 1:
                cmpt += 1

        if c < len(self.plateau[0])-1:
            if self.plateau[r][c+1] == 1:
                cmpt += 1

        if c > 0:
            if self.plateau[r][c-1] == 1:
                cmpt += 1

        if r < len(self.plateau)-1 and c < len(self.plateau[0])-1:
            if self.plateau[r+1][c+1] == 1:
                cmpt += 1

        if r < len(self.plateau) -1 and c > 0:
            if self.plateau[r+1][c-1] == 1:
                cmpt += 1

        if r > 0 and c > 0:
            if self.plateau[r-1][c-1] == 1:
                cmpt += 1

        if r > 0 and c < len(self.plateau[0])-1:
            if self.plateau[r-1][c+1] == 1:
                cmpt += 1

        return cmpt

App()