from ursina import *
from ursina import time
import random
boxes = []
a = 0.5
app = Ursina()
aa = random.randint(-5, 5)
yy = random.randint(-5, 5)
camera.orthographic = True
camera.fov = 10

player = Entity(model='cube', color=color.black, scale=(a), position=(0,-4), collider='box')



def new_box(position):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.1,
            color=color.green,
            scale=1,
            position=position
        )
    )


background = Entity(
    model='quad',
    texture='sky.jpg',
    scale=(20, 12),
    z=1
    )


new_box(position=(aa, yy))


def update():
    global aa, yy
    if held_keys['a']:
        player.x -= 15 * time.dt
    if held_keys['d']:
        player.x += 15 * time.dt
    if held_keys['s']:
        player.y -= 15 * time.dt
    if held_keys['w']:
        player.y += 15 * time.dt
    for box in boxes:
        if player.intersects(box).hit:               
            destroy(box)
            boxes.remove(box)
            if player.scale != 9:
                player.scale *= 1.1
                aa = random.randint(-5, 5)
                yy = random.randint(-5, 5)
                new_box(position=(aa, yy))
            break


app.run()
