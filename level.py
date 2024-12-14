
from tupy import *
import random


class Level(Image):
    def __init__(self):
        self.x = 450
        self.y = 252
        self.file = 'level.png'
        self.level1 = False
        self.level2 = False
        self.level3 = False 

    def update(self):
        if keyboard.key_just_down('1'):
            self.level1 =  True            
        elif keyboard.key_just_down('2'):
            self.level2 = True
        elif keyboard.key_just_down('3'):
            self.level3 = True