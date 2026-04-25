import pygame
import sys
from constants import *
from tools import Brush, RectTool, CircleTool

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Paint App")
    
    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    canvas.fill(BLACK)
    
    clock = pygame.time.Clock()
    
  
    current_tool = Brush()
    current_color = BLUE
    radius = 5
    
    drawing = False
    start_pos = None
   

    last_pos = None 
    while True:
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_r: current_color = RED
                elif event.key == pygame.K_g: current_color = GREEN
                elif event.key == pygame.K_b: current_color = BLUE
                
               
                
                elif event.key == pygame.K_p: # Pen/Brush
                    current_tool = Brush()
                    if current_color == BLACK: current_color = BLUE # Возврат цвета после ластика
                elif event.key == pygame.K_s: # Square/Rect
                    current_tool = RectTool()
                elif event.key == pygame.K_c: # Circle
                    current_tool = CircleTool()
                elif event.key == pygame.K_e: # Eraser
                    current_tool = Brush()
                    current_color = BLACK
                
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                
                if drawing and not isinstance(current_tool, Brush):
                    current_tool.draw(canvas, current_color, start_pos, event.pos, radius)
                drawing = False
                start_pos = None
                last_pos = None

            if event.type == pygame.MOUSEMOTION and drawing:
             
                if isinstance(current_tool, Brush):
                    current_tool.draw(canvas, current_color, last_pos, event.pos, radius)
                    last_pos = event.pos

        """Отрисовка"""
        screen.fill(BLACK) 
        screen.blit(canvas, (0, 0))

        if drawing and not isinstance(current_tool, Brush):
            current_pos = pygame.mouse.get_pos()
            current_tool.draw(screen, current_color, start_pos, current_pos, radius)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()