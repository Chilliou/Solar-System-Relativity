# Example file showing a circle moving on screen
import pygame
import random
import math
import tkinter as tk
import json
import cv2
from Planet import Planet



def star_sky():
    for _ in range(1000):
        random_pos = pygame.Vector2(random.randrange(screen.get_width()), random.randrange(screen.get_height()))
        pygame.draw.circle(screen, "white", random_pos, random.randrange(3))

def update_pos():
    try:
        if(screen.get_width()<float(text_pos_x.get()) or screen.get_width()<float(text_pos_y.get())):
            raise ValueError("Out of range")
        planet_selected.pos_x = float(text_pos_x.get())
        planet_selected.pos_y = float(text_pos_y.get())
        planet_selected.masse = float(text_masse.get())
            
            
    except ValueError:
        print("Error : enter valid pos")

    app.destroy()
    app = None
    

def open_pop_up():
    global text_pos_x, text_pos_y,text_masse, app
    
    if app is None:
        app = tk.Tk()
        pos_x = tk.Label(app, text="Position x")
        pos_x.grid(column=0, row=0)

        text_pos_x = tk.Entry(app)
        text_pos_x.grid(column=1, row=0, columnspan=2)
        text_pos_x.insert(0, planet_selected.pos_x)

        pos_y = tk.Label(app, text="Position Y")
        pos_y.grid(column=0, row=1)

        text_pos_y = tk.Entry(app)
        text_pos_y.grid(column=1, row=1, columnspan=2)
        text_pos_y.insert(0, planet_selected.pos_y)

        masse = tk.Label(app, text="Masse")
        masse.grid(column=0, row=2)

        text_masse = tk.Entry(app)
        text_masse.grid(column=1, row=2, columnspan=2)
        text_masse.insert(0, planet_selected.masse)

        button = tk.Button(app, text="Update", command=update_pos)
        button.grid(column=1, row=3)
        
        planet_selected.pos_x = float(text_pos_x.get())
        planet_selected.pos_y = float(text_pos_y.get())

    else:
        print("Reset x et y")
        text_pos_x.delete(0, tk.END)
        text_pos_x.insert(0, planet_selected.pos_x)
        
        text_pos_y.delete(0, tk.END)
        text_pos_y.insert(0, planet_selected.pos_y)

        text_masse.delete(0, tk.END)
        text_masse.insert(0, planet_selected.masse)

        app.lift()  # Amener la fenêtre au premier plan

    
    #app.mainloop()

def get_color(s_rgb) -> pygame.Color :
    rgb = s_rgb.split(',')
    return pygame.Color(int(rgb[0]), int(rgb[1]), int(rgb[2]), 255)


def load_planet():
    f = open('planetes.json')
    data = json.load(f)
    f.close()

    list_distance = []
    list_rayon = []
    for planet in data:
        list_rayon.append(data[planet]["rayon"])
        if planet != "Soleil":
            list_distance.append(data[planet]["distance_soleil"])

    list_planet = []
    for planet in data:
        d = data[planet]
        dt_soleil = float(d['distance_soleil']) / min(list_distance) * 10 + screen.get_width() / 2
        planet_actuel = Planet(planet, d["masse"], d["rayon"], 0,d["vitesse"], dt_soleil, d["rgb"], pos_y=screen.get_height() / 2)
        list_planet.append(planet_actuel)

    return list_planet
    
    
    
def call_drawn_planet():

    for p in list_planet:
        drawn_planet(p, p.pos_x, p.pos_y, "./ressource/"+p.nom+".png")
    
    
def drawn_planet(planet, pos_x, pos_y, file_name):
  SCALE = 0.10

  # Chargez l'image en couleur
  try:
    image = cv2.imread(file_name, cv2.IMREAD_COLOR)

    # Obtenir les dimensions de l'image
    (h, w) = image.shape[:2]
  except Exception:
    print('Erreur pour'+file_name)

  # Calculez les coordonnées du centre
  center_x = int(w / 2 * SCALE)
  center_y = int(h / 2 * SCALE)
  
  planet.rayon = center_x
  
  pos_x_rel = pos_x-center_x
  pos_y_rel = pos_y-center_y

  sun = pygame.image.load(file_name)
  sun1 = pygame.transform.scale_by(sun,SCALE)
  
  screen.blit(sun1,(pos_x_rel,pos_y_rel))
  
  if planet_selected != None and planet_selected == planet:
    draw_selected_planet(pos_x_rel, pos_y_rel, h, w)

def draw_selected_planet(pos_x_rel, pos_y_rel, h, w):
    SCALE = 0.10
    THICKNESS = 3
    LENGTH_LINE = 25

    pygame.draw.line(screen,"white",(pos_x_rel,pos_y_rel),(pos_x_rel+LENGTH_LINE,pos_y_rel), THICKNESS)
    pygame.draw.line(screen,"white",(pos_x_rel,pos_y_rel),(pos_x_rel,pos_y_rel+LENGTH_LINE), THICKNESS)
    
    pygame.draw.line(screen,"white",(pos_x_rel+w*SCALE-LENGTH_LINE,pos_y_rel),(pos_x_rel+w*SCALE,pos_y_rel), THICKNESS)
    pygame.draw.line(screen,"white",(pos_x_rel+w*SCALE,pos_y_rel),(pos_x_rel+w*SCALE,pos_y_rel+LENGTH_LINE), THICKNESS)
    
    pygame.draw.line(screen,"white",(pos_x_rel+w*SCALE-LENGTH_LINE,pos_y_rel+h*SCALE),(pos_x_rel+w*SCALE,pos_y_rel+h*SCALE), THICKNESS)
    pygame.draw.line(screen,"white",(pos_x_rel+w*SCALE,pos_y_rel+h*SCALE-LENGTH_LINE),(pos_x_rel+w*SCALE,pos_y_rel+h*SCALE), THICKNESS)
    
    pygame.draw.line(screen,"white",(pos_x_rel,pos_y_rel+h*SCALE-LENGTH_LINE),(pos_x_rel,pos_y_rel+h*SCALE), THICKNESS)
    pygame.draw.line(screen,"white",(pos_x_rel,pos_y_rel+h*SCALE),(pos_x_rel+LENGTH_LINE,pos_y_rel+h*SCALE), THICKNESS)


def drawn_cross(pos_x, pos_y):
    THICKNESS = 3
    CROSS_SIZE = 20
    pygame.draw.line(screen,"white",(pos_x-CROSS_SIZE,pos_y),(pos_x+CROSS_SIZE,pos_y), THICKNESS)
    pygame.draw.line(screen,"white",(pos_x,pos_y-CROSS_SIZE),(pos_x,pos_y+CROSS_SIZE), THICKNESS)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1820, 1000))
clock = pygame.time.Clock()
running = True
dt = 0

global angle, radius
global list_planet
global planet_selected

app = None
planet_selected = None
radius = 10
angle = 10
cross = None


bg = pygame.image.load("sky1.jpg")
list_planet = load_planet()

while running:

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("black")
    screen.blit(bg, (0,0))

    call_drawn_planet()

    if cross is not None:
        drawn_cross(cross[0], cross[1])
    
    if app:
        app.update_idletasks()
        app.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for planet in list_planet:
                # Calculer la position réelle de la planète sur l'écran
                planet_x = planet.pos_x
                planet_y = planet.pos_y

                # Calculer la distance entre le clic de la souris et le centre de la planète
                distance = math.sqrt((mouse_x - planet_x) ** 2 + (mouse_y - planet_y) ** 2)

                # Vérifier si la distance est inférieure ou égale au rayon de la planète
                if distance <= planet.rayon:
                    planet_selected = planet
                    cross = None
                    open_pop_up()
                    break  # Sortir de la boucle si une planète a été sélectionnée
            if planet_selected is None:
                cross = mouse_x, mouse_y
                drawn_cross(mouse_x, mouse_y)

        if event.type == pygame.QUIT:
            running = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
app.destroy()


