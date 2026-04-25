import pygame
import random

class Snake:
   
    def __init__(self, width, height, cell_size):
        
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.length = 1
        self.positions = [(width // 2, height // 2)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = (0, 255, 0)

    def get_head_position(self):
        
        return self.positions[0]

    def update(self):
        
        cur = self.get_head_position()
        x, y = cur
        if self.direction == pygame.K_UP:
            y -= self.cell_size
        elif self.direction == pygame.K_DOWN:
            y += self.cell_size
        elif self.direction == pygame.K_LEFT:
            x -= self.cell_size
        elif self.direction == pygame.K_RIGHT:
            x += self.cell_size

        new = (x, y)
        
        
        if new in self.positions[2:] or x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        
        
        self.positions.insert(0, new)
        
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def draw(self, surface):
       
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (self.cell_size, self.cell_size))
            pygame.draw.rect(surface, self.color, rect)

class Food:
  
    def __init__(self, width, height, cell_size):
        
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.position = (0, 0)
        self.color = (213, 50, 80)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size,
                         random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (self.cell_size, self.cell_size))
        pygame.draw.rect(surface, self.color, rect)