import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wildlife Information Display")

# Load images
background = pygame.image.load(r"C:\Users\HP\Desktop\Python Files\background")
animal = pygame.image.load(r"C:\Users\HP\Desktop\Python Files\animal.jpg")

# Scale images
background = pygame.transform.scale(background, (800, 600))
animal = pygame.transform.scale(animal, (300, 250))

font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 30)

heading = font.render("Wildlife Information", True, (255, 255, 255))
fact = small_font.render("Lions can sleep for up to 20 hours a day.", True, (255, 255, 255))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(animal, (250, 180))
    screen.blit(heading, (200, 50))
    screen.blit(fact, (100, 500))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()