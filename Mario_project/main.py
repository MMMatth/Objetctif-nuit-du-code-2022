# on rajoute random
from re import X
import pyxel, random

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
        self.LIST_GROUND = [(1,0),(1,1),(2,0),(3,1),(0,1)]
        self.player = player(64,64,4,self.LIST_GROUND)
        
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



    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        self.player.update()
        
        self.scroll_x = (self.player.x - 64) 
        self.scroll_y = (self.player.y - 64) 



    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(6)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, self.scroll_x, self.scroll_y, 128, 128)

        # si le vaisseau possede des vies le jeu continue 
        if self.player.vie > 0:
         
            pyxel.text(5,5, 'VIES:'+ str(self.player.vie), 7)
            
            pyxel.camera(self.scroll_x,self.scroll_y)
            
            self.player.draw()
            
        else:
            pyxel.text(50,64, 'GAME OVER', 7)
            
        if self.player.x > 416:    
            pyxel.text(self.player.x,self.player.y-50, 'WIN', 7)
        

class player:
    def __init__(self, x,y,life,list_ground)-> None:
        self.x = x
        self.y = y
        self.sens = 1
        self.vie = life
        
        self.img = (0,16)
        self.allimg = [(0,16),(8,16),(16,16),(24,16)]
        
        self.running = False
        self.LIST_GROUND = list_ground
        
        self.left = False
        self.right = False
        self.jump = False
        self.fall = True
        
        self.objet = {}
    

    
    def dead(self):
        self.vie -= 1
        self.x , self.y = 0, 0
    
    def collision(self):
        print(self.x,self.y)
        if pyxel.btn(pyxel.KEY_RIGHT) and get_tile(self.x+6, self.y+12) not in self.LIST_GROUND : # colission left block
            self.right = True
        else : 
            self.right = False
        
        if pyxel.btn(pyxel.KEY_LEFT) and get_tile(self.x+1, self.y+12) not in self.LIST_GROUND: # colission right block
            self.left = True
        else : 
            self.left = False
 
        if pyxel.btn(pyxel.KEY_UP) and get_tile(self.x, self.y) not in self.LIST_GROUND and self.jump == False and not get_tile(self.x, self.y+16) not in self.LIST_GROUND: # colission up block
            self.compteur = 0
            self.jump = True
        
        if pyxel.btn(pyxel.KEY_DOWN) and get_tile(self.x, self.y+16) == (3,1):
            self.x = 320
            self.y = 40
            
        if get_tile(self.x, self.y+16) == (4,1):
            self.dead()      

        if get_tile(self.x, self.y) == (0,1) or get_tile(self.x+8, self.y) == (0,1):
            self.objet = {
                "champignon": objet(183, 16, self.LIST_GROUND)
            }   
             
        
        if not get_tile(self.x, self.y) not in self.LIST_GROUND or not get_tile(self.x+8, self.y) not in self.LIST_GROUND:
            self.jump = False
            
        
        if get_tile(self.x, self.y+16) not in self.LIST_GROUND and get_tile(self.x+8, self.y+16) not in self.LIST_GROUND: # colission down block
            self.fall = True
        else:
            self.fall = False
            
        
            
    def deplacement(self):
        if self.right :
            self.x += 1
            self.sens = 1
        if self.left:
            self.x += -1
            self.sens = -1
        if self.jump:
            self.compteur += 1
            if self.compteur % 15 != 14:
                self.fall = False
                self.y += -1
            else:
                self.jump = False
                self.fall = True    
        if self.fall:
            self.y += 1
                
    def animation(self):
        if self.jump or self.fall:
            self.anim_jump()
        elif self.right or self.left:
            self.anim_run()
        
        else:
            self.anim_idle()
            
    def update(self):
        self.deplacement()
        self.animation()
        self.collision()
        for nom in self.objet:
            self.objet[nom].update()
        if self.y > 100:
            self.dead()

    def anim_run(self):
        if pyxel.frame_count%5 == 1:
            self.img = self.allimg[2]
        elif pyxel.frame_count%5 == 4:
            self.img = self.allimg[3]
            
    def anim_idle(self):
        if pyxel.frame_count%20 == 1:
            self.img = self.allimg[0]
        elif pyxel.frame_count%20 == 19:
            self.img = self.allimg[1]
    
    def anim_jump(self):
        self.img = self.allimg[2]

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.img[0], self.img[1], 8 * self.sens, 16 , 6)
        for nom in self.objet:
            self.objet[nom].draw()

class objet:
    def __init__(self, x,y,list_ground)-> None:
        self.x = x
        self.y = y
        self.img = (32,0)
        self.LIST_GROUND = list_ground
    
    def update(self):
        self.x += 0.5
        if get_tile(self.x, self.y+8) not in self.LIST_GROUND:
            self.y += 0.5
        if get_tile(self.x, self.y+16) == (4,1):
                self.x = 10000
                self.y = 10000 
                
    def draw(self):
        pyxel.blt(self.x,self.y,0,self.img[0],self.img[1],8,8,0)
        
if __name__ == "__main__":
    Jeu()
