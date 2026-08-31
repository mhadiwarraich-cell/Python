import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pet Food Collection Game")

# Pet and food
pet = pygame.Rect(100, 250, 50, 50)
food = pygame.sprite.Group()

for x, y in [(300, 200), (500, 350), (650, 150)]:
    item = pygame.sprite.Sprite()
    item.rect = pygame.Rect(x, y, 30, 30)
    food.add(item)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pet.x -= 5
    if keys[pygame.K_RIGHT]:
        pet.x += 5
    if keys[pygame.K_UP]:
        pet.y -= 5
    if keys[pygame.K_DOWN]:
        pet.y += 5

    # Collect food
    for item in food.copy():
        if pet.colliderect(item.rect):
            food.remove(item)

    screen.fill((100, 200, 100))

    pygame.draw.rect(screen, (100, 100, 255), pet)

    for item in food:
        pygame.draw.circle(screen, (255, 200, 0), item.rect.center, 15)

    # Completion message
    if len(food) == 0:
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("All Food Collected!", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=(400, 300)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()