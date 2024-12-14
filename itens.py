from tupy import *

class Item(Image):
    def __init__(self, x: float, file: str, bomouruim: int ) -> None:
        self.x = x
        self.y = 10
        self._file = file
        self.velocidade = 10
        self.isgood = bomouruim
        # self._hide()
    #Método inicial que armazena a posição e velocidade dos itens que caem no jogo.

    def update(self) -> None:
        self.y += self.velocidade 
    

    #Método que atualiza a taxa de pixels dos itens.
    def destroy(self) -> None:
        return super().destroy()





