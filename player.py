from tupy import *
from monstro import Monstro
from recorde import Recorde

global pontos
pontos = Recorde()
global monstro
monstro = Monstro()
itens_ruins = []
itens_bons = []

class Personagem(Image):
    def __init__(self, x: float, y: float, file = str) -> None:
        self.x = x
        self.y = y
        self.angle = 0
        self.pulando = 0
        self.pulo = False
        self.file = 'humandown.png'
        self.proximacolisao = 0
        self.perdeu = False
        self.queda = 0

    def update(self) -> None:
        global monstro
        global pontos 
        global itens_bons
        global itens_ruins


        if keyboard.is_key_down('Left'):
            self.file = 'humanleft.png'
            self.x -= 30
            if self.x < 40:
                self.x = 40

        elif keyboard.is_key_down('Right'):
            self.file = 'humanright.png'
            self.x += 30
            if self.x>860:
               self.x=860
        elif keyboard.is_key_just_down('Up'):
            self.pulo = True
        elif self.pulo:
            if self.pulando <= 2:
               self.pulando += 1
               self.y -= 30
            elif self.pulando < 8:
                self.pulando += 1
                
            elif self.pulando == 8:
                self.pulando += 1
                self.y += 30
            elif self.pulando == 9:
                self.pulando += 1
                self.y += 30
            elif self.pulando == 10:
                self.pulando = 0
                self.pulo = False
                self.y += 30           
        else:
            self.file = 'humandown.png' 

        if self.collides_with(monstro):
            if self.proximacolisao == 0:
                pontos.diminui(10)
            self.proximacolisao += 1
            if self.proximacolisao == 15:
                self.proximacolisao = 0
            
        for item in itens_ruins:
            if self.collides_with(item):
                pontos.diminui(5)
                itens_ruins.remove(item)
                item.y = 800
        for item in itens_bons:
            if self.collides_with(item):
                pontos.aumenta(5)
                itens_bons.remove(item)
                item.y = 800

        if self.perdeu:
            if self.queda < 5:
                self.y -= 30
                self.queda += 1
            else:
                self.y += 30

        
    def _collides_with(self, other: TupyObject) -> bool:
        return super()._collides_with(other)
    
    def collides_with(self, other: TupyObject) -> bool:
        return super()._collides_with(other)