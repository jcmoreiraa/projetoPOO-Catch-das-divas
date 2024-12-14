from tupy import *

class Recorde(Label):

    def __init__(self) -> None:
        super().__init__('Recorde: 0', 180, 28, font='Arial 20', color='yellow')
        self.recorde = 0
        self.__maiorrecorde = 0

        #Método inicial, herdando funções da classe Label do Tupy, que imprime a pontuação atualizada na tela
    
    def aumenta(self, pontos: int) -> None:

        self.recorde += pontos
        self.text = f'Pontuação: {self.recorde}'

        if self.recorde > self.__maiorrecorde:
            self.__maiorrecorde = self.recorde
        
        #Método que atualiza a pontuação aumentando.

    def diminui(self, pontos: int) -> None:
        self.recorde -= pontos
        self.text = f'Pontuação: {self.recorde}'

        #Método que atualiza a pontuação diminuindo.
