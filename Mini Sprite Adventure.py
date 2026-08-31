import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Sprite Adventure")

x = 375
y = 275
speed = 5
color = (0, 150, 255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Keep sprite inside the screen
    x = max(0, min(x, 750))
    y = max(0, min(y, 550))

    # Change color at screen edges
    if x == 0:
        color = (255, 0, 0)
    elif x == 750:
        color = (0, 255, 0)
    elif y == 0:
        color = (255, 255, 0)
    elif y == 550:
        color = (255, 0, 255)

    screen.fill((30, 30, 30))

    # Solid rectangle
    pygame.draw.rect(screen, color, (x, y, 50, 50))

    # Outlined rectangle
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50), 3)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()