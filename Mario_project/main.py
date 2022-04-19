# on rajoute random
from re import X
import pyxel, random

TRANSPARENT_COLOR = 7
WALL_TILE_X = 4
TILE_FLOOR = (8, 8)
scroll_x = 0


def get_tile(tile_x, tile_y):
    return pyxel.tilemap(0).pget(tile_x, tile_y)

def detect_collision(x, y, dy):
    x1 = x // 8
    y1 = y // 8
    x2 = (x + 8 - 1) // 8
    y2 = (y + 8 - 1) // 8
    for yi in range(y1, y2 + 1):
        for xi in range(x1, x2 + 1):
            if get_tile(xi, yi)[0] >= WALL_TILE_X:
                return True
    if dy > 0 and y % 8 == 1:
        for xi in range(x1, x2 + 1):
            if get_tile(xi, y1 + 1) == TILE_FLOOR:
                return True
    return False

class Jeu:
    def __init__(self):
        global scroll_x

        pyxel.init(128, 128, title="Nuit du c0de")



        self.vies = 4

        self.player = player(0,0)
        
        pyxel.load("skin.pyxres")

        pyxel.run(self.update, self.draw)


    def deplacement(self):
        """déplacement avec les touches de directions"""

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += 1
            print(get_tile(self.player_x, self.player_y))
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x += -1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player_y += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.player_y += -1



    def explosions_animation(self):
        """animation des explosions"""
        for explosion in self.explosions_liste:
            explosion[2] +=1
            if explosion[2] == 12:
                self.explosions_liste.remove(explosion)


    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        self.player.update()


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(6)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, (scroll_x // 4) % 128, 128, 128, 128)
        pyxel.bltm(0, 0, 0, scroll_x, 0, 128, 128, TRANSPARENT_COLOR)


        # si le vaisseau possede des vies le jeu continue 
        if self.vies > 0:
         
            pyxel.text(5,5, 'VIES:'+ str(self.vies), 7)
            
            pyxel.camera(scroll_x, 0)
            
            self.player.draw()

        else:
            pyxel.text(50,64, 'GAME OVER', 7)

class player:
    def __init__(self, x,y)-> None:
        self.x = x
        self.y = y
        
        self.img = (0,16)
        self.imglist = [(0,16),(8,16),(16,16),(24,16)]
        
        self.running = False
        
    def deplacement(self):
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
            self.running = True
        else:
            self.running = False
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x += -1
            self.running = True
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.y += -1
            
        if self.running:
            self.run()
        else:
            self.idle()
    
    def update(self):
        self.deplacement()

    def run(self):
        if pyxel.frame_count%5 == 1:
            self.img = self.imglist[2]
        elif pyxel.frame_count%5 == 4:
            self.img = self.imglist[3]
            
    def idle(self):
        if pyxel.frame_count%20 == 1:
            self.img = self.imglist[0]
        elif pyxel.frame_count%20 == 19:
            self.img = self.imglist[1]

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.img[0], self.img[1], 8, 16 )
        

Jeu()