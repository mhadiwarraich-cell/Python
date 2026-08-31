import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

# Player
player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill((0, 255, 0))
player.rect = player.image.get_rect(center=(400, 500))

# Enemies
enemies = pygame.sprite.Group()

for i in range(7):
    enemy = pygame.sprite.Sprite()
    enemy.image = pygame.Surface((40, 40))
    enemy.image.fill((255, 0, 0))
    enemy.rect = enemy.image.get_rect(
        center=(random.randint(50, 750), random.randint(50, 400))
    )
    enemies.add(enemy)

score = 0
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    # Collision
    if pygame.sprite.spritecollide(player, enemies, False):
        score += 1

    screen.fill((10, 10, 30))

    enemies.draw(screen)
    screen.blit(player.image, player.rect)

    # Score
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()