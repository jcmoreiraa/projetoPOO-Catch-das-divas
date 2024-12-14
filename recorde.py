from tupy import *

class Recorde(Label):

    def __init__(self) -> None:
        super().__init__('Recorde: 0', 500, 9, font='Times New Roman 30', color='yellow')
        self.__recorde = 0
        self.__maiorrecorde = 0

        #Método inicial, herdando funções da classe Label do Tupy, que imprime a pontuação atualizada na tela
    
    def aumenta(self, pontos: int) -> None:
        self.__recorde += pontos
        self.text = f'Pontuação: {self.__score}'

        if self.__recorde > self.__maiorrecorde:
            self.__maiorrecorde = self.__recorde
        
        #Método que atualiza a pontuação aumentando.

    def diminui(self, pontos: int) -> None:
        self.__recorde -= pontos
        self.text = f'Pontuação: {self.__score}'

        #Método que atualiza a pontuação diminuindo.


