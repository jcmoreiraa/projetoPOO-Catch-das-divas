from tupy import *

class Monstro(Image):
    def __init__(self) -> None:
        self.x = 30
        self.y = 460
        self._file = 'monster.png'
        self.__velocidade = 10
        self.andar_para_direita = True

    @property
    def velocidade(self) -> float:
        return self.__velocidade
    #Método de leitura da velocidade.

    @velocidade.setter
    def velocidade(self, valor: float) -> None:
        self.__velocidade = valor
    #Método de definição da velocidade.

    def update(self) -> None:
        global itens_ruins
        global itens_bons
        if self.x > 850:
            self.andar_para_direita = False
        elif self.x < 60:
            self.andar_para_direita = True
            
        if self.andar_para_direita:
            self.file = 'monstrodir.png'
            self.x += self.velocidade
        elif not self.andar_para_direita:
            self.file = 'monstroesq.png'
            self.x -= self.velocidade
        
    #         #remover valores dos pontos 
    # #Método que atualiza a taxa de pixels dos itens.

    def _collides_with(self, other: TupyObject) -> bool:
        return super()._collides_with(other)
    
    def collides_with(self, other: TupyObject) -> bool:
        return super()._collides_with(other)
            