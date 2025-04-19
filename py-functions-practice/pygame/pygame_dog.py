import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

def draw_dog(surface):
    pygame.draw.circle(surface, (150, 100, 50), (300, 400), 60)  # Head
    pygame.draw.circle(surface, (0, 0, 0), (280, 390), 10)  # Eye Left
    pygame.draw.circle(surface, (0, 0, 0), (320, 390), 10)  # Eye Right
    pygame.draw.ellipse(surface, (150, 100, 50), (270, 430, 60, 30))  # Nose
    pygame.draw.polygon(surface, (150, 100, 50), [(260, 360), (280, 310), (290, 360)])  # Ear Left
    pygame.draw.polygon(surface, (150, 100, 50), [(340, 360), (320, 310), (310, 360)])  # Ear Right

running = True
while running:
    screen.fill((255, 255, 255))  # Fill background
    draw_dog(screen)  # Draw the dog
    pygame.display.flip()  # Update display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit loop

pygame.quit()
