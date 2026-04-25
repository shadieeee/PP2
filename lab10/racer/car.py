import pygame

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path):
        super().__init__()
        loaded_img = pygame.image.load("images/car.png").convert_alpha()
        w, h = loaded_img.get_size()
        
        SCALE_FACTOR = 0.1
        self.original_img = pygame.transform.scale(loaded_img, (w * SCALE_FACTOR, h * SCALE_FACTOR))
        
        self.image = self.original_img.copy()
        self.rect = self.image.get_rect()
        
        self.position = pygame.math.Vector2(x, y)
        self.angle = 90
        self.speed = 0
        self.rotation_speed = 3

    def rotate_car(self, direction):
        self.angle += direction * self.rotation_speed
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.original_img, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate_car(1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate_car(-1)
        
        self.speed = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed = 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed = -3
        
        direction_vector = pygame.math.Vector2(1, 0).rotate(-self.angle)
        self.position += direction_vector * self.speed
        self.rect.center = (round(self.position.x), round(self.position.y))