from ursina import Ursina
from ursina import camera

app = Ursina()

camera.orthographic = True
camera.fov = 10

background = Entity(
    model='quad',
    texture='',
    scale=(20, 12),
    z=1
    )

