from random import randint
import pygame as pyg
from sys import exit

pyg.init()
BASE = 800
ALTURA = 600
tela = pyg.display.set_mode((BASE,ALTURA))

class Jogo_da_vida:

    def __init__(self):
        self.size_block = 10
        self.block_life = pyg.Surface((self.size_block - 1,self.size_block - 1))
        self.block_life.fill("#ffd700")
        self.fps = pyg.time.Clock()
        self.height_block = int(ALTURA/self.size_block)
        self.widght_block = int(BASE/self.size_block)
        self.load_board()
    

    def load_board(self):
        self.board = []
        for line in range(self.height_block):
            line = []
            for col in range(self.widght_block):
                if randint(1,100) < 10:
                    line.append(1)
                else:
                    line.append(0)
            self.board.append(line)
    
    def check_event(self):

        for evento in pyg.event.get():
            
            if evento.type == pyg.QUIT:
                pyg.quit()
                exit()
                
    
    def run(self):
        while True:
            self.fps.tick(5)
            self.check_event()
            self.draw_grid()
            self.update_game()
            self.draw_blocks_life()
            pyg.display.update()
            tela.fill((255,255,255))

    
    def draw_grid(self):

        for line in range(self.height_block):
            for col in range(self.widght_block):
                pyg.draw.rect(tela,(0,0,0),(col * self.size_block, line * self.size_block,self.size_block - 1,self.size_block - 1))
    
    def update_game(self):

        for line in range(self.height_block):
            for col in range(self.widght_block):
                peca = self.board[line][col]
                vizinhos = self.get_vizinho(line,col)

                if peca == 1:

                    if vizinhos.count(1) <= 1:
                        self.board[line][col] = 0
                    
                    elif vizinhos.count(1) > 3:
                        self.board[line][col] = 0
                    
                    elif vizinhos.count(1) >= 2 and vizinhos.count(1) <= 3:
                        pass

                if peca == 0:

                    if vizinhos.count(1) == 3:
                        self.board[line][col] = 1


    def get_vizinho(self,line,col):
        vizinhos = []
        for linha in range(line - 1, line + 2):
            for coluna in range(col - 1,col + 2):

                limites = linha < 0 or linha >= self.height_block or coluna < 0 or coluna >= self.widght_block

                if linha == line and coluna == col or limites:
                    continue
             
                peca = self.board[linha][coluna]
                vizinhos.append(peca)
        
        return vizinhos
    
    def draw_blocks_life(self):

        for line in range(self.height_block):
            for col in range(self.widght_block):

                if self.board[line][col] == 1:
                    calc_pos = (col * self.size_block,line * self.size_block)
                    tela.blit(self.block_life,calc_pos)


if __name__ == "__main__":
    game_obj = Jogo_da_vida()
    game_obj.run()