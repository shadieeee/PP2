import pygame

class Tool:
  
    def draw(self, surface, color, start_pos, end_pos, radius):
        pass

class Brush(Tool):
    def draw(self, surface, color, start_pos, end_pos, radius):
        if start_pos:
            pygame.draw.line(surface, color, start_pos, end_pos, radius * 2)

class RectTool(Tool):
    def draw(self, surface, color, start_pos, end_pos, radius):
        x = min(start_pos[0], end_pos[0])
        y = min(start_pos[1], end_pos[1])
        w = abs(start_pos[0] - end_pos[0])
        h = abs(start_pos[1] - end_pos[1])
        pygame.draw.rect(surface, color, (x, y, w, h), radius)

class CircleTool(Tool):
    def draw(self, surface, color, start_pos, end_pos, radius):
        r = int(((start_pos[0] - end_pos[0])**2 + (start_pos[1] - end_pos[1])**2)**0.5)
        pygame.draw.circle(surface, color, start_pos, r, radius)