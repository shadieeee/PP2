import pygame
import math
import random
class Coin(pygame.sprite.Sprite):
    def __init__(self, screen_width,screen_hight):
        super().__init__()

        self.original_img = pygame.image.load("images/coin.png").convert_alpha()
        self.screen_width = screen_width
        self.screen_hight = screen_hight
        self.original_img = pygame.transform.scale(self.original_img,(30,30))

        self.width = self.original_img.get_width()
        self.hight = self.original_img.get_height()

        self.image = self.original_img.copy()

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(50,screen_width - 50)
        self.rect.y = random.randint(50,screen_hight - 50)

        self.visible = True         
        self.last_switch = pygame.time.get_ticks()
        self.switch_interval = 5000  

        self.timer = 0.0
    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_switch >= self.switch_interval:
            self.visible = not self.visible
            self.last_switch = current_time
            
            if self.visible:
                self.rect.x = random.randint(50, self.screen_width - 50)
                self.rect.y = random.randint(50, self.screen_hight - 50)

    
        if not self.visible:
            self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        else:
            self.timer += 0.1
            scale_factor = abs(math.sin(self.timer)) 

            
            new_w = max(1, int(self.width * scale_factor))
         
            self.image = pygame.transform.scale(self.original_img, (new_w, self.hight))

            
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center