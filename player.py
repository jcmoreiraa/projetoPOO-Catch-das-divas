from tupy import *

class Player(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "humandown.png"
        self.x = x
        self.y = y
        self.direction = ""
    def update(self):
        match self.direction:
            case "left":
                self.file = "humanleft.png"
            case "right":
                self.file = "humanright.png"
                
        if keyboard.is_key_down('Left'):
            self.direction = "left"
            self.x -= 15
        if keyboard.is_key_down('Right'):
            self.direction = "right"
            self.x += 15