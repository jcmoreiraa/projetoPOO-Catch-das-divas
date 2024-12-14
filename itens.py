from tupy import *

class Item(Image):
    def __init__(self, x: float, y: float, file: str, velocidade: float, angle: int) -> None:
        self.x = x
        self.y = y
        self._file = str
        self.__velocidade = velocidade
        self._angle = angle
        self._hide()
    #Método inicial que armazena a posição e velocidade dos itens que caem no jogo.

    @property
    def velocidade(self) -> float:
        return self.__velocidade
    #Método de leitura da velocidade.
    
    @velocidade.setter
    def velocidade(self, valor: float) -> None:
        self.__velocidade = valor
    #Método de definição da velocidade.

    def update(self) -> None:
        if self.y > 520:
            return False
        self.y += self.velocidade
    #Método que atualiza a taxa de pixels dos itens.





