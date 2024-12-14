from tupy import *

class TelaInicial(BaseImage):

    def __init__(self) -> None:
        super().__init__(file = 'telainicial.png', x = 450, y= 250)
        self._facil = False
        self._medio = False
        self._dificil = False
        self._fim = False

class Personagem(Image):
    def __init__(self, x: float, y: float, angle: int, file = str) -> None:
        self.x = x
        self.y = y
        self.angle = angle
        self.file = file

    def anda(self) -> None:
        if keyboard.is_key_down('left') or keyboard.is_key_just_down('left'):
            self.file = 'esquerda.png'
        elif keyboard.is_key_down('right') or keyboard.is_key_just_down('right'):
            self.file = 'direita.png'
        else:
            self.file = 'frente.png' 





