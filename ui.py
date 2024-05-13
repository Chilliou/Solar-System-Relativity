# Example file showing a circle moving on screen
import pygame
import random
import math
import tkinter as tk
import json
from Planet import Planet



def star_sky():
    for _ in range(1000):
        random_pos = pygame.Vector2(random.randrange(screen.get_width()), random.randrange(screen.get_height()))
        pygame.draw.circle(screen, "white", random_pos, random.randrange(3))

def circle_planet():
    radius = 10
    angle = 10
    # Calculate new coordinates based on angle and radius
    center_x = screen.get_width() #// 2  # Center X using floor division
    center_y = screen.get_height() #// 2  # Center Y using floor division
    x_offset = radius * math.cos(math.radians(angle))
    y_offset = radius * math.sin(math.radians(angle))

    # Calculate relative coordinates from center
    rel_x = center_x + x_offset - radius
    rel_y = center_y + y_offset - radius

    pygame.draw.circle(screen, "green", pygame.Vector2(rel_x, rel_y), 10)

    # Update the angle for the next rotation
    angle += 1 # Adjust rotation speed (degrees per update)

    # Wrap the angle around 360 degrees to keep rotation continuous
    angle %= 360

def update_pos():
    try:
        if(screen.get_width()<float(text_pos_x.get()) or screen.get_width()<float(text_pos_y.get())):
            raise ValueError("Out of range")
        sun_pos.x = float(text_pos_x.get())
        sun_pos.y = float(text_pos_y.get())
        print(f"pos x : {sun_pos.x} /n pos x : {sun_pos.y}")
        
    except ValueError:
        print("Error : enter valid pos")

    app.destroy()
    

def open_pop_up():
    global text_pos_x, text_pos_y, app
    
    app = tk.Tk()
    pos_x = tk.Label(app, text="Position x")
    pos_x.grid(column=0, row=0)

    text_pos_x = tk.Entry(app)
    text_pos_x.grid(column=1, row=0, columnspan=2)
    text_pos_x.insert(0,sun_pos.x)

    pos_y = tk.Label(app, text="Position Y")
    pos_y.grid(column=0, row=1)

    text_pos_y = tk.Entry(app)
    text_pos_y.grid(column=1, row=1, columnspan=2)
    text_pos_y.insert(0,sun_pos.y)

    button = tk.Button(app, text="Update", command=update_pos)
    button.grid(column=1, row=2)

    sun_pos.x = float(text_pos_x.get())
    sun_pos.y = float(text_pos_y.get())

    app.mainloop()

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

    max_rayon = max(list_rayon)
    scale_factor = 100  # Ajustez cette valeur selon vos préférences

    list_planet = []
    for planet in data:
        d = data[planet]
        dt_soleil = float(d['distance_soleil']) / min(list_distance) * 10 + screen.get_width() / 2
        planet_actuel = Planet(planet, d["masse"], d["rayon"], d["vitesse"], dt_soleil, d["rgb"], pos_y=screen.get_height() / 2)
        list_planet.append(planet_actuel)

    for p in list_planet:
        pos = pygame.Vector2(p.pos_x, p.pos_y)
        r_rayon = (p.rayon / max_rayon) * scale_factor
        pygame.draw.circle(screen, get_color(p.rgb), pos, int(r_rayon))

    return list_planet


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

global angle, radius
global list_planet

radius = 10
angle = 10

sun_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
earth_pos = pygame.Vector2(screen.get_width() / 2+100, screen.get_height() / 2+100)

bg = pygame.image.load("sky1.jpg")
list_planet = load_planet()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(bg, (0,0))


    load_planet()

    keys = pygame.key.get_pressed()
    ev = pygame.event.get()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        print(f"Voici les cord x: {mouse_x} et y: {mouse_y}")
        planet_selected = False
        for planet in list_planet:
            # Calculer la position réelle de la planète sur l'écran
            planet_x = planet.pos_x
            planet_y = planet.pos_y

            # Calculer la distance entre le clic de la souris et le centre de la planète
            distance = math.sqrt((mouse_x - planet_x) ** 2 + (mouse_y - planet_y) ** 2)

            print(f"la distance est : {distance}")
            print(f"la planet_x est : {planet_x}")
            print(f"la planet_y est : {planet_y}")
            print(f"la planet.rayon est : {planet.rayon}")

            # Vérifier si la distance est inférieure ou égale au rayon de la planète
            if distance <= planet.rayon:
                print(f"Planète sélectionnée : {planet.nom}")
                planet_selected = True
                break  # Sortir de la boucle si une planète a été sélectionnée

        if not planet_selected:
            print("Aucune planète sélectionnée")

    if keys[pygame.K_k]:
        open_pop_up()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
app.destroy()


