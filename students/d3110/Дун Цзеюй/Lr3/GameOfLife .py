import pygame
import random
import copy

class GameOfLife:
    def __init__(self, width: int=640, height: int=480, cell_size: int=10, speed: int=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self):
        # @see: http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        cells = self.cell_list(randomize = True)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_cell_list(cells)
            cells = self.update_cell_list(cells)
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=False):
        if randomize == True:
            clist = []
            for i in range(self.cell_height):
                clist.append([1 if random.randint(1, 10) % 2 == 0 else 0
                 for j in range((self.cell_width))])
            return clist
        else:
            clist = []
            for i in range(self.cell_height):
                if i == 2:
                    clist.append([1 if j == 3 else 0
                     for j in range((self.cell_width))])
                if i == 2 :
                    clist.append([1 if j == 4 else 0
                     for j in range((self.cell_width))])
                if i == 2:
                    clist.append([1 if (j == 3) or (j == 2) or (j == 4) else 0
                     for j in range((self.cell_width))])
                clist.append([0 for j in range((self.cell_width))])           
            return clist
    def draw_cell_list(self, rects):
        x, y = 0, 0 
        for i in rects:
            for j in i:
                if j == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                        (x, y, self.cell_size, self.cell_size))
                if j == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                        (x, y, self.cell_size, self.cell_size))
                x +=self.cell_size
            y += self.cell_size
            x = 0


    def get_near(self, cell):
        x, y = (cell[0], cell[1])
        near = []
        for i in range(-1, 2):
            for j in range(- 1, 2):
                if not(i == 0 and j == 0):
                    if (abs(y + i) < (self.cell_width)) and (abs (x + j) < (self.cell_height)):
                        near.append((abs(x + j),
                         abs(y+i)))                
        return list(set(near))


    def update_cell_list(self, cell_list):
        buff_list = copy.deepcopy(cell_list)
        k=0
        for i in range(len(cell_list)):
            for j in range(len(cell_list[i])):
                list = self.get_near((i, j))
                k=0
                for x, y in list:
                    if cell_list[x][y]:
                        k+=1
                if k==3 or (k==2 and cell_list[i][j]==1):
                    buff_list[i][j]=1
                else:
                    buff_list[i][j]=0                                                                               
        return buff_list                
        
if __name__ == '__main__':
    game = GameOfLife(640 , 480, 10)
    print(game.get_near((0,13)))
    game.run()