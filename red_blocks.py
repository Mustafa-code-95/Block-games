from ursina import *
import time
import threading
from random import randint
import os

ooo = 10
app = Ursina()
Sky()
rt = 6
e = 1
game_over = False
score = 0
score_thread_started = False
game_over_text = Text('', origin=(0,5), scale=1.2)
score_text = Text('', origin=(0,10), scale=1.2)

def ft():
    global score, score_text, game_over
    while not game_over:
        time.sleep(1)
        score += 1
        score_text.text = f'Score: {score-1}'


player = Entity(model='cube', texture='tnt.jpg', color=color.white, scale=(1,1,1), position=(0,1,0), collider='box')
ground = Entity(model='plane', scale=(10,1,10), texture='white_cube', texture_scale=(1,1), color=color.gray, collider='box')

camera.position = (0, 10, -20)
camera.rotation_x = 30
camera.bg_color = color.rgb(135, 206, 235)

obstacles = []


def spawn_obstacle():
    x = randint(-4, 4)
    z = randint(5, 20)
    obstacle = Entity(model='cube', color=color.red, position=(x,0.5,z), scale=(1,1,1), collider='box')
    obstacles.append(obstacle)


for i in range(5):
    spawn_obstacle()


def update_score():
    if not game_over:
        global score
        score += 1
        score_text.text = f'Score: {score}'
        invoke(update_score, delay=1)


def reset_game():
    global game_over, score, rt, ooo, score_updating
    game_over = False
    score = 0
    rt = 6
    ooo = 10
    score_text.text = 'Score: 0'
    game_over_text.text = ''
    player.position = (0, 1, 0)

    for obstacle in obstacles:
        obstacle.x = randint(-4, 4)
        obstacle.z = randint(10, 20)

    if not score_updating:
        score_updating = True
        update_score()


def update():
    global game_over, score_thread_started, rt, ooo, score, score_text

    if not score_thread_started:
        threading.Thread(target=ft, daemon=True).start()
        score_thread_started = True

    if not game_over:
        if held_keys['a']:
            player.x -= 15 * time.dt
        if held_keys['d']:
            player.x += 15 * time.dt
        if held_keys['s']:
            player.z -= 15 * time.dt
        if held_keys['w']:
            player.z += 15 * time.dt
        if score == ooo:
            ooo += 10
            rt += 5
        for obstacle in obstacles:
            obstacle.z -= rt * time.dt
            if obstacle.z < -10:
                obstacle.z = randint(10, 20)
                obstacle.x = randint(-4, 4)

            if player.intersects(obstacle).hit:
                obstacle.z = randint(10, 20)
                obstacle.x = randint(-4, 4)
                game_over = True
                game_over_text.text = 'Game Over\nClick r to restart'
                d = open("red_blocks_records.txt", "a+")
                d.write(f"Score: {score}\n")

    else:
        if held_keys['r']:
            reset_game()


app.run()
