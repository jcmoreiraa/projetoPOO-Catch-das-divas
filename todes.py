from tupy import *
import random
import os
import random 
import pygame

global itens_ruins 
global itens_bons 

global isok
isok = False



itens_ruins = []
itens_bons = []
class TelaInicial(BaseImage):

    def __init__(self) -> None:
        super().__init__(file = 'telainicial.png', x = 450, y= 250)
        self._facil = False
        self._medio = False
        self._dificil = False
        self._fim = False



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

        andar_esquerda = True
        andar_direita = False
        if keyboard.is_key_down('Left'):
           self.file = 'humanleft1.png'
           self.x -= 30
           if self.x < 40:
                self.x = 40
           

        elif keyboard.is_key_down('Right'):
           self.file = 'humanright1.png'
           self.x += 30
           if self.x>840:
               self.x=840
        
                

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



global pontos
pontos = Recorde()

menu1 = TelaInicial()
global monstro
monstro = Monstro()
monstro._hide()

pygame.init()
musica = pygame.mixer.music.load('novembrochuvoso.mp3')
pygame.mixer.music.play()


def criaritens() -> Item:
    global itens_bons 
    global itens_ruins 
    itemx = random.randint(0, 800)
    #considerando 1 para itens bons e 0 para itens ruins
    if menu1._dificil:
        isgood = random.randint(0, 3)
    if menu1._facil or menu1._medio:
        isgood = random.randint(0,1)
    if isgood == 1:
        itens_bons.append(Item(itemx,'trofeu.png', isgood))
    else:
        itens_ruins.append(Item(itemx,'tomate.png', isgood))            


global update_count 
update_count = 1

def update_itens():
    global itens_ruins
    global itens_bons
    for item in itens_bons:
        item.update()
    for item in itens_ruins:
        item.update()

def update_monstro():
    global monstro
    monstro.update()

def update_personagem():
    global personagem
    personagem.update()

global personagem
personagem = Personagem(180, 470)
personagem._hide()

global mostrar_pontos
mostrar_pontos = Label('', 180, 28, font = 'Arial 20',
                color = 'white', anchor = 'nw')

def update():
    global itens_ruins 
    global itens_bons 
    global update_count
    global monstro 
    global personagem
    global isok
    global pontos
    global mostrar_pontos
    mostrar_pontos._hide()
    if keyboard.is_key_just_down('space') and (isok is False):
        menu1._file = 'level.png'

# precisa arrumar a parte de definir o nivel pq da pra mudar de nivel durante a partida
# o que nao deveria poder acontecer ai eh so botar um if se o isok eh true entao nao muda
    if isok is False:
        if (keyboard.is_key_just_down('1')):
            menu1._facil = True
            menu1._file = 'tudopronto.png'
            isok = True

        elif (keyboard.is_key_just_down('2')):
            menu1._medio = True
            menu1._file = 'tudopronto.png'
            isok = True


        elif (keyboard.is_key_just_down('3')):
            menu1._dificil = True
            menu1._file = 'tudopronto.png'
            isok = True
            


    if (keyboard.is_key_just_down('space')):
        if menu1._file == 'tudopronto.png':
            isok = True
            menu1._file = 'gameimg.png'
            monstro._show()
            personagem._show()
            pontos.recorde = 0
            personagem.perdeu = False
            personagem.y = 470


 
    if (menu1._file == 'gameimg.png') and isok:
        if (update_count % 60) == 0:
            print(pontos.recorde)
            if menu1._facil:
                criaritens()
        if (update_count % 40) == 0:
            if menu1._medio:
                criaritens()

        if (update_count % 5) == 0:
            if menu1._dificil:
                criaritens()
               
        if pontos.recorde < 0:
            menu1._file = 'gameover.png'
            isok = False
            menu1._dificil = False

            monstro._hide()
            mostrar_pontos._hide()
            personagem.perdeu = True
            for item in itens_bons:
                item._hide()
            for item in itens_ruins:
                item._hide()





        mostrar_pontos._hide()
        mostrar_pontos = Label(pontos.recorde, 180, 28, font = 'Arial 20',
                color = 'white', anchor = 'nw')


    update_itens()
    update_monstro()
    update_personagem()
        
    update_count += 1
    


# monstro = Monstro()
# itens = []

run(globals())

