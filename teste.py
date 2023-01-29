import pygame as pyg 
from sys import exit

pyg.init()

tela = pyg.display.set_mode((800,800))

while True:

    for evento in pyg.event.get():

        if evento.type == pyg.QUIT:
            pyg.quit()
            exit()

    pyg.draw.rect(tela,(255,255,255),(250,250,250,250),2)
    pyg.display.update()
    tela.fill((0,0,0))