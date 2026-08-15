import pygame

pygame.init()

state = 0
screen = pygame.display.set_mode((512, 512))
pygame.draw.line(screen, (255, 255, 255), (100,100), (1, 3), 3)
pygame.display.set_caption("Beginner's Hardware")
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
            else:
                if event.key == pygame.K_RIGHT:
                    running = False
pygame.quit()
