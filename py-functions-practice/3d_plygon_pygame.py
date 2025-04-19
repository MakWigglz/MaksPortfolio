import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

def project_3d(points, depth=300):
    """projects 3D points onto a 2D plane."""
    projected = []
    for x, y, z in points:
        scale = depth / (depth + z)
        projected.append((x * scale + 300, y * scale + 300))
    return projected

# define a simple cube shape
cube_points = [
    (-50, -50, -50), (50, -50, -50), (50, 50, -50), (-50, 50, -50),
    (-50, -50, 50), (50,-50, 50), (50, 50, 50), (-50, 50, 50)
    ]
edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4),
         (0,4), (1,5), (2,6), (3,7)]

running = True
angle = 0

while running:
    screen.fill((30, 30, 30))

    # rotate points around y-axis
    rotated_points = []
    for x, y, z in cube_points:
        x_rot = x * math.cos(angle) - z * math.sin(angle)
        z_rot + x * math.sin(angle) + z * math.cos(angle)
        rotated_points.append((x_rot, y, z_rot))
    projected_points = project_3d(rotated_points)

    # draw edges
    for edge in edges:
        pygame.draw.line(screen, (255, 255, 255), projected_points[edge[0]], projected_points[edge[1]], 2)

    angle += 0.02  # rotate slowly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

    
