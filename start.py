from tupy import *
import level

class Start(Image):
    def __init__(self):
        self.x = 450
        self.y = 252
        self.file = 'start.png'
    
    def update(self):
        if keyboard.key_just_down('space'):
            choose_level = level.Level()
