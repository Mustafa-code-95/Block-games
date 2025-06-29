from ursina import *
from random import randint

f = 0
list = [color.green, color.blue, color.pink]
sss = 0
d = 0
op = 7
m = 0
level = 0
o = 1.00

app = Ursina()

Sky()
h =  False
max = 9
e_e = False
game_over = False

h_text = Text('', origin=(0,3), scale=4)
e_e_text = Text('', origin=(0,0), scale=2)
game_over_text = Text('', origin=(0,1.5), scale=3)
restart_prompt = Text('', origin=(0, -0.1), scale=1.5)

player = Entity(model='cube', texture='tnt.jpg', color=color.white, scale=(1,1,1), position=(0,1,0), collider='box')

ground = Entity(model='plane', scale=(10,1,10), texture='white_cube', texture_scale=(1,1), color=color.gray, collider='box')

camera.position = (0, 10, -20)
camera.rotation_x = 30
camera.bg_color = color.rgb(135, 206, 235)

obstacles = []

def spawn_obstacle():
    x = randint(-4, 4)
    z = randint(5, 20)
    obstacle = Entity(model='cube', color=list[f], position=(x,0.5,z), scale=(1,1,1), collider='box')
    obstacles.append(obstacle)


for i in range(10):
    spawn_obstacle()


def update():
    global game_over, level, o, e_e, m, op, d, h, sss, f, list
    e_e = False
    
    if held_keys['a']:
        player.x -= 15 * time.dt
    if held_keys['d']:
        player.x += 15 * time.dt
    if held_keys['s']:
        player.z -= 15 * time.dt
    if held_keys['w']:
        player.z += 15 * time.dt


    for obstacle in obstacles:
        obstacle.z -= op * time.dt
        if obstacle.z < -10:
            obstacle.z = randint(10, 20)
            obstacle.x = randint(-4, 4)

        if player.intersects(obstacle).hit:
            
            if player.scale_x < max:
                player.scale /= 0.9
                obstacle.z = randint(10, 20)
                obstacle.x = randint(-4, 4)

            else:
                player.scale = 0.1
                level = 0
                o = 0
                d += 3
                op += d
                m += 1
                e_e = True
                e_e_text.text = f"Mission {m}"
            
            if m == 10:
                op = 7
                d = 0
                m = o
                level = 0
                sss += 1
                game_over_text.text = f"Level {level}"
                e_e_text.text = f"Mission {m}"
                h_text.text = f"Professionalist Level {sss}"
                if f != 2:
                    f += 1
                    obstacle.color = list[f]

                else:
                    f = 0

            if player.scale_x > o:
                o += 1
                level += 1
                game_over = False
                game_over_text.text = f"Level {level}"


app.run()
