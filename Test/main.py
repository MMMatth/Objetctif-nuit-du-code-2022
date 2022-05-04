import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")
#on charge le fichier pyxel edit
pyxel.load("seize_par-seize.pyxres")
# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 60
TILE_GROUND = [(2,2),(3,2)]
TILE_WALL = [(2,0), (3,0),(2,1)]
SCROLL_BORDER_X = 40
SCROLL_BORDER_Y = 20
scroll_x = 0
scroll_y = 0
dx = 1 #sens de déplcaement
def get_tile(x, y):
    return pyxel.tilemap(0).pget(x//8, y//8)

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    global scroll_x,dx
    print(get_tile(x,y))
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
        dx = 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 40) :
            x = x - 1
            dx = -1
    if pyxel.btn(pyxel.KEY_DOWN) or (get_tile(x+4,y+12) not in TILE_GROUND and get_tile(x+4,y+12) not in TILE_WALL):
        if (y < 120) :
            y = y + 0.5
    if pyxel.btn(pyxel.KEY_SPACE):
        if (y > 0) :
            y = y - 2
    #scroll    
    if x>40 :
        scroll_x = min(x - SCROLL_BORDER_X,240*8)
        return x, y


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global dx
    # vide la fenetre
    pyxel.cls(0)

    # map
    pyxel.camera()
    pyxel.bltm(0,0,0,scroll_x,scroll_y,128,128,colkey=2)
    #vaisseau qui commence en (0,8) dans fichier pyxres
    pyxel.camera(scroll_x,scroll_y)
    pyxel.blt(vaisseau_x, vaisseau_y,0,0,16,16*dx,16,colkey=6)

pyxel.run(update, draw)