from tupy import *


class Monster(Image):
    def __init__(self, x: int, velocidade: int) -> None:
        super().__init__('monster.png')
        self.x = x
        self.y = 0
        self.velocidade = velocidade
    
    def update(self):
    self.x = self.x - self.velocidade
    if self.x < -20:
      self.x = 820
    elif self.x > 820:
      self.x = -20
    if self._collides_with(bolha):
            