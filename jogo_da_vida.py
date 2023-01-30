import pygame as pyg
from sys import exit

ALTURA = 600
BASE = 800
janela = pyg.display.set_mode((BASE,ALTURA))
GRID_COLOR = (0,0,0)
BG_COLOR = (255,255,255)
COLOR_BLOCK_LIFE = "#ffd700"

class Jogo_da_vida:

    def __init__(self):
        self.size_block = 20
        self.block_height = int(ALTURA/self.size_block)
        self.block_width =  int(BASE/self.size_block)
        self.fps = pyg.time.Clock()
        self.fps_num =  30
        self.board = self.load_board()
        self.block_life = pyg.Surface((self.size_block - 1,self.size_block - 1))
        self.block_life.fill(COLOR_BLOCK_LIFE)
        self.editor_mode = True
    

    def load_board(self):
        board = []

        for line in range(self.block_height):
            line = []
            for col in range(self.block_width):
                line.append(0)
            board.append(line)
        
        return board

    def draw_grid(self):

        for line in range(self.block_height):
            for col in range(self.block_width):
                pos_x = col * self.size_block
                pos_y = line * self.size_block
                pyg.draw.rect(janela,GRID_COLOR,(pos_x,pos_y,self.size_block - 1,self.size_block - 1))
    
    def check_event(self):

        for evento in pyg.event.get():

            if evento.type == pyg.QUIT:
                pyg.quit()
                exit()
            
            if evento.type == pyg.KEYDOWN:
                if evento.key == pyg.K_a:
                    self.editor_mode = not self.editor_mode
                    self.fps_num = [7,60][int(self.editor_mode)]
            
            if pyg.mouse.get_pressed()[0] and self.editor_mode:
                mouse_pos = pyg.mouse.get_pos()

                pos_x = int(mouse_pos[0]/self.size_block)
                pos_y = int(mouse_pos[1]/self.size_block)

                self.board[pos_y][pos_x] = 1
            
            if pyg.mouse.get_pressed()[2] and self.editor_mode:
                mouse_pos = pyg.mouse.get_pos()

                pos_x = int(mouse_pos[0]/self.size_block)
                pos_y = int(mouse_pos[1]/self.size_block)

                self.board[pos_y][pos_x] = 0



    def run(self):

        while True:

            self.fps.tick(self.fps_num)

            self.check_event()
            self.draw_grid()
            self.update_game()
            self.draw_block_life()
            pyg.display.update()
            janela.fill(BG_COLOR)

    def get_cell(self,line,col):
        return self.board[line][col]
    
    def update_game(self):

        if self.editor_mode:
            return

        next = self.load_board()

        for line in range(self.block_height):
            for col in range(self.block_width):
                vizinhos = self.get_vizinhos(line,col)
                state = self.get_cell(line,col)

                if state == 0 and vizinhos.count(1) == 3:
                    next[line][col] = 1
                elif state == 1 and (vizinhos.count(1) < 2 or vizinhos.count(1) > 3):
                    next[line][col] = 0
                else:
                    next[line][col] = state

        self.board = next
    

    def get_vizinhos(self,line,col):
        vizinhos = []
        for linha in range(line - 1,line + 2):
            for coluna in range(col - 1,col + 2):

                limites = linha < 0 or linha >= self.block_height or coluna < 0 or coluna >= self.block_width

                if coluna == col and linha == line or limites:
                    continue

                peca = self.get_cell(linha,coluna)
                vizinhos.append(peca)
        
        return vizinhos
    

    def draw_block_life(self):

        for line in range(self.block_height):
            for col in range(self.block_width):

                if self.get_cell(line,col) == 1:
                    _x = col * self.size_block
                    _y = line * self.size_block

                    janela.blit(self.block_life,(_x,_y))

if __name__ == "__main__":
    game_object = Jogo_da_vida()
    game_object.run()