import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Smart Traffic Signal Simulator")

# Car sprite
car = pygame.sprite.Sprite()
car.image = pygame.Surface((60, 30))
car.image.fill((0, 100, 255))
car.rect = car.image.get_rect(center=(100, 300))

# Sprite group
cars = pygame.sprite.Group()
cars.add(car)

speed = 4

# Traffic signal
signal = "GREEN"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move car
    car.rect.x += speed

    # Road boundary
    if car.rect.right >= 750:
        car.rect.right = 750
        speed = -4
        signal = "RED"
        car.image.fill((255, 0, 0))

    elif car.rect.left <= 50:
        car.rect.left = 50
        speed = 4
        signal = "GREEN"
        car.image.fill((0, 255, 0))

    screen.fill((40, 40, 40))

    # Road
    pygame.draw.rect(screen, (80, 80, 80), (0, 250, 800, 120))

    # Traffic light
    pygame.draw.rect(screen, (20, 20, 20), (700, 50, 70, 170))
    pygame.draw.circle(screen, (255, 0, 0) if signal == "RED" else (60, 0, 0), (735, 80), 20)
    pygame.draw.circle(screen, (255, 255, 0), (735, 135), 20)
    pygame.draw.circle(screen, (0, 255, 0) if signal == "GREEN" else (0, 60, 0), (735, 190), 20)

    # Draw car sprite
    cars.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()