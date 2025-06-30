from ursina import Ursina
from ursina import camera
from ursina import Entity

app = Ursina()

camera.orthographic = True
camera.fov = 10

background = Entity(
    model='quad',
    texture='Block-Games-30-6-2025.gif',
    scale=(20, 12),
    z=1
    )

def update():
    pass


app.run()
