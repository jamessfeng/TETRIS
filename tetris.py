#!/usr/bin/python3

#Tetris

import pygame
import os
from abc import ABC, abstractmethod

os.environ['SDL_AUDIODRIVER'] = 'dummy'
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (169,169,169)

bSide =30
bMargin = bSide/10 
global counter 
counter = 0

# TYPES OF PIECES 
# Line , T , Cube, Z , Z flip, L flip
# 1    , 2 , 3   , 4 ,   5   ,  6 

class main(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ITS TITSRIS")
        self.width = 700
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.screen.fill(GREY)
        self.fps = 30
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)
        self.grid = self.init_grid()
        self.floor = [19 for x in range(10)]
        # print("ground"+self.ground)
        #self.draw_grid()
        #self.print_grid()
        #Line(self.grid)
        #self.draw_grid()
        #self.print_grid()
        #print(self.grid)
    def run(self):
        # fb = Line(self.grid)
        #print(fb.block_id)
        # block = Block()
        # print(block)
        # #self.gravity(1)

        # Cell([2,0], self.grid)
        n = 0
        currPiece = Piece(1, self.grid)
        #print(currPiece.blocks)
        self.print_grid()
        self.gravity(currPiece)
        print("asdfasdfasd")
        self.print_grid()
        #cPiece = Piece(8, self.grid)
        #print(self.floor_check(currPiece))
        time_elapsed_since_last_action = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000

            if (n == 0): self.gravity(currPiece)
            n += 1
            if (n > 10): n = 0
            self.gravity(currPiece)
            #pygame.time.delay(50)

            # dt = self.clock.tick() 
            # time_elapsed_since_last_action += dt
            # if time_elapsed_since_last_action > 250:
            #     self.gravity(currPiece)
            #     time_elapsed_since_last_action = 0
            #pygame.display.flip()
            # self.draw_text(("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                           # self.clock.get_fps(), " "*5, self.playtime)), 1)
            #pygame.display.flip()
            #self.screen.blit(self.background, (0, 0))

            self.draw_grid()
            #Line(self.grid)

        pygame.quit()


    def init_grid(self):
        w, h = 10, 20
        grid = [[0 for x in range(w)] for y in range(h)] 
        return grid

    def draw_text(self, text, type):
        if type == 1:
            surface = self.font.render(text, True, (0, 255, 0))
            # // makes integer division in python3
            self.screen.blit(surface, (0, 0))
            pygame.display.flip()
    def draw_grid(self):
        #width = 100
        pygame.draw.rect(self.screen, RED, (0, 0, 10*(bSide+bMargin)+bMargin, bMargin))
        pygame.draw.rect(self.screen, RED, (0, 0, bMargin, 20*(bSide+bMargin)+bMargin))
        height = bMargin
        width = bMargin
        for dList in self.grid:    
            for cell in dList:
                if cell is 0:
                    self.draw_cell(WHITE, height, width)
                else:
                    self.draw_cell(BLACK, height, width)
                width += bSide
                pygame.draw.rect(self.screen, RED, (width, height, bMargin, bSide))
                width += bMargin
            height += bSide
            width = bMargin
            pygame.draw.rect(self.screen, RED, (0, height, 10*(bSide+bMargin), bMargin))                
            height += bMargin

        pygame.display.flip()

    def gravity(self, piece):
        if self.floor_check(piece) == True:
            for block in piece.blocks:
                #print(str(block))
                block.y += 1
                self.sync_pieceboard(piece)
                # print(block.x, block.y)
        else:
            pass
    def next_block(self):
        pass
    def sync_pieceboard(self, piece):
        for block in piece.blocks:
            self.grid[block.y-1][block.x] = 0
            self.grid[block.y][block.x] = 1

    def floor_check(self, piece):
        for block in piece.blocks:
            if block.y >= self.floor[block.x]:
                #print(block.y + self.floor[block.x])
                return False
        return True

    def print_grid(self):
        for array in self.grid:
            print(array)
    def draw_cell(self, Colour, height, width):
        pygame.draw.rect(self.screen, Colour, (width, height, bSide, bSide))

class Cell():
    """docstring for Block"""
    def __init__(self, cords, grid):
        self.x = cords[0]
        self.y = cords[1]
        grid[self.y][self.x] = 1

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

# TYPES OF PIECES 
# Line , T , Cube, Z , Z flip, L , L flip
#   1  , 2 ,  3  , 4 ,   5   , 6 ,   7

class Piece():
    """docstring for Piece"""
    def __init__(self, p_type, grid):
        if (p_type == 1):
            self.b1 = Cell([3,0], grid)
            self.b2 = Cell([4,0], grid)
            self.b3 = Cell([5,0], grid)
            self.b4 = Cell([6,0], grid) 
        elif (p_type == 2):
            self.b1 = Cell([4,0], grid)        
            self.b2 = Cell([5,0], grid)
            self.b3 = Cell([6,0], grid)
            self.b4 = Cell([5,1], grid)
        elif (p_type == 3):
            self.b1 = Cell([4,0], grid)        
            self.b2 = Cell([5,0], grid)
            self.b3 = Cell([4,1], grid)
            self.b4 = Cell([5,1], grid)
        elif (p_type == 4):
            self.b1 = Cell([4,0], grid)        
            self.b2 = Cell([5,0], grid)
            self.b3 = Cell([5,1], grid)
            self.b4 = Cell([6,2], grid)
        elif (p_type == 5):
            self.b1 = Cell([5,0], grid)        
            self.b2 = Cell([6,0], grid)
            self.b3 = Cell([4,1], grid)
            self.b4 = Cell([5,1], grid)
        elif (p_type == 6):
            self.b1 = Cell([4,0], grid)        
            self.b2 = Cell([5,0], grid)
            self.b3 = Cell([6,0], grid)
            self.b4 = Cell([4,1], grid)
        elif (p_type == 7):
            self.b1 = Cell([4,0], grid)        
            self.b2 = Cell([5,0], grid)
            self.b3 = Cell([6,0], grid)
            self.b4 = Cell([6,1], grid)
        #TEST BLOCK
        elif (p_type == 8):  
            self.b1 = Cell([4,5], grid)        
            self.b2 = Cell([5,5], grid)
            self.b3 = Cell([6,5], grid)
            self.b4 = Cell([6,19], grid)
        self.pivot = self.b1
        self.blocks = [self.b1, self.b2, self.b3, self.b4]
        #print(self.blocks)
        #print(self.blocks)

# class Block():
#     """docstring for Block"""
#     def __init__(self):
#         self.block_id = 1
#         #print(selblock_id)
#         #counter += 1
#     def rotate():
#         pass
#     def __str__(self):
#         return str(self.block_id)

# class Line(Block):
#     """docstring for line"""
#     def __init__(self, grid):
#         Block(Line, self).__init__()
#         for x in range (3,7):
#             grid[0][x] = 1
#         print(self.block_id)

# class Cube(Block):
#     """docstring for Cube"""
#     def __init__(self, arg):
#         super(Cube, self).__init__()

# class Z(Block):
#     """docstring for Z"""
#     def __init__(self, arg):
#         super(Z, self).__init__()
#         self.arg = arg
        
# class ZO(Block):
#     """docstring for oZ"""
#     def __init__(self, arg):
#         super(oZ, self).__init__()
#         self.arg = arg
                        
# class L(Block):
#     """docstring for L"""
#     def __init__(self, arg):
#         super(L, self).__init__()
#         self.arg = arg

# class LO(Block):
#     """docstring for oL"""
#     def __init__(self, arg):
#         super(oL, self).__init__()
#         self.arg = arg
               
if __name__=="__main__":
    # call the main function
    main().run()