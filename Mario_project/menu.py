# on rajoute random
from re import X
import pyxel, random
import main
import os

TRANSPARENT_COLOR = 7
WALL_TILE_X = 4
TILE_FLOOR = (8, 8)

scroll_x = 0



def get_tile(tile_x, tile_y):
    return pyxel.tilemap(0).pget(tile_x//8, tile_y//8)
class Jeu:
    def __init__(self):
        global scroll_x

        pyxel.init(128, 128, title="Mario")
        pyxel.mouse(True)

        pyxel.load("menu.pyxres")

        pyxel.run(self.update, self.draw)


    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        self.click()
        # print(pyxel.mouse_x,pyxel.mouse_y)

    def click(self):
        if 32 < pyxel.mouse_x < 94 and 40 < pyxel.mouse_y < 62 and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            quit()

            
            
        if 32 < pyxel.mouse_x < 94 and 53 < pyxel.mouse_y < 94 and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            quit()

    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(6)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)

        # si le vaisseau possede des vies le jeu continue 
            
            
        pyxel.text(56,49, 'PLAY', 7)
        pyxel.text(56,81, 'QUIT', 7)
        pyxel.text(53,20, 'MARIO', 7)
            
        

if __name__ == "__main__":
    Jeu()
