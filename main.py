from tupy import *
from tela import TelaInicial 
from itens import Item
from monstro import Monstro
from recorde import Recorde
from player import Personagem
import random
import pygame

global pontos
pontos = Recorde()

menu1 = TelaInicial()
global monstro
monstro = Monstro()
monstro._hide()

isok = False
itens_ruins = []
itens_bons = []

pygame.init()
musica = pygame.mixer.music.load('Pokemon_HeartGold_SoulSilver_-_Champion_Red_Battle_Music_HQ.mp3')
pygame.mixer.music.play(-1)

fim = pygame.mixer.Sound('sadtrombone.wav')

def criaritens() -> Item:
    global itens_bons 
    global itens_ruins 
    itemx = random.randint(0, 800)
    #considerando 1 para itens bons e 0 para itens ruins
    isgood = random.randint(0, 1)
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
            personagem.y = 450
            personagem.x = 30
            monstro.x = 300


 
    if (menu1._file == 'gameimg.png') and isok:
        if (update_count % 60) == 0:
            print(pontos.recorde)
            if menu1._facil:
                criaritens()
        if (update_count % 40) == 0:
            if menu1._medio:
                criaritens()

        if (update_count % 20) == 0:
            if menu1._dificil:
                criaritens()

        for item in itens_ruins:
            if personagem.collides_with(item):
                pontos.diminui(5)
                itens_ruins.remove(item)
                item.y = 800
        for item in itens_bons:
            if personagem.collides_with(item):
                pontos.aumenta(5)
                itens_bons.remove(item)
                item.y = 800
    
        if personagem.collides_with(monstro):
            if personagem.proximacolisao == 0:
                pontos.diminui(10)
            personagem.proximacolisao += 1
            if personagem.proximacolisao == 15:
                personagem.proximacolisao = 0

        if pontos.recorde < 0:
            menu1._file = 'gameover.png'
            fim.play()
            isok = False
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

