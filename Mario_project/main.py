# on rajoute random
from re import X
import pyxel, random

TRANSPARENT_COLOR = 7
WALL_TILE_X = 4
TILE_FLOOR = (8, 8)

scroll_x = 0




class Jeu:
    def __init__(self):
        global scroll_x

        pyxel.init(128, 128, title="Nuit du c0de")



        self.vies = 4

        self.player = player(0,0)
        
        self.scroll_x = self.player.x
        self.scroll_y = self.player.y
        
        pyxel.load("skin.pyxres")

        pyxel.run(self.update, self.draw)

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
        self.scroll_x = (self.player.x - 64) 
        self.scroll_y = (self.player.y - 64) 


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(6)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, self.scroll_x, self.scroll_y, 128, 128)

        # si le vaisseau possede des vies le jeu continue 
        if self.vies > 0:
         
            pyxel.text(5,5, 'VIES:'+ str(self.vies), 7)
            
            pyxel.camera(self.scroll_x,self.scroll_y)
            
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
        self.LIST_GROUND = [(1,0),(1,1),(2,0)]
        self.LIST_GROUND_USABLE = [(1,0),(1,1)]
    
    def get_tile(self,tile_x, tile_y):
        return pyxel.tilemap(0).pget(tile_x//8, tile_y//8)
    
    def deplacement(self):
        print(self.get_tile(self.x, self.y))
        
        if pyxel.btn(pyxel.KEY_RIGHT) and self.get_tile(self.x+8, self.y-13) not in self.LIST_GROUND :
            self.x += 1
            self.running = True
        else:
            self.running = False
        if pyxel.btn(pyxel.KEY_LEFT) and self.get_tile(self.x, self.y-16) not in self.LIST_GROUND:
            self.x += -1
            self.running = True
        if pyxel.btn(pyxel.KEY_DOWN) and self.get_tile(self.x, self.y+16) not in self.LIST_GROUND: #on peut plus descendre
            self.y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.get_tile(self.x+4, self.y) not in self.LIST_GROUND:
            self.y += -1
        elif  self.get_tile(self.x+8, self.y+16) not in self.LIST_GROUND:
            self.y += 1
            
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
        pyxel.blt(self.x, self.y, 0, self.img[0], self.img[1], 8, 16 , 6)
        

Jeu()