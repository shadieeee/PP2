import pygame
import sys
from coin import Coin
from car import Car
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

coins_group = pygame.sprite.Group()

def main():
    pygame.init()
    font = pygame.font.SysFont("Arial", 24, bold=True)
    pygame.mixer.init()

    coin_trigger_sound = pygame.mixer.Sound("sounds/coin-trigger.mp3")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Car Race")
    clock = pygame.time.Clock()

    try:
        bg = pygame.image.load("images/Race_Track.webp").convert()
        bg = pygame.transform.scale(bg, ((SCREEN_WIDTH, SCREEN_HEIGHT)))
    except pygame.error as e:
        print(f"Не удалось загрузить фон: {e}")
        bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        bg.fill((50, 150, 50))

    running = True

    score = 0

    all_sprites = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()

    player = Car(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "images/car.png")
    all_sprites.add(player)

    def spawn_coin():
        new_coin = Coin(SCREEN_WIDTH, SCREEN_HEIGHT)
        coins_group.add(new_coin)
        all_sprites.add(new_coin)

    def draw_score(screen, score):
        score_img = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_img, (20, 20))
    for _ in range(1):
        spawn_coin()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False

        all_sprites.update()

        collided_coins = pygame.sprite.spritecollide(player, coins_group, False)

        for coin in collided_coins:
            if coin.visible:
                coin.visible = False
                coin.last_switch = pygame.time.get_ticks()
                coin_trigger_sound.play()
                score += 1

        screen.blit(bg, (0, 0))

        all_sprites.draw(screen)

        draw_score(screen, score)

        pygame.display.flip()

        clock.tick(60)
if __name__ == "__main__":
    main()