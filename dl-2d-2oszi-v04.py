import numpy as np
import pygame
import matplotlib.colors as mcolors

# Initialisierungsparameter
dt = 0.1

width, height = 100, 100
laplace_strength = 0.5
rotation_speed = 3.0
damping = 0.4 #0.76
scale = 5
arrow_spacing = 4

masse1 = 0.0  # masse
masse2 = 0.0  # masse

# Laplace-Operator für 2D
laplacian2 = lambda Z: (
    np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
    np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) - 4 * Z
)

# Wellenfunktion: Real- und Imaginärteil
a1 = np.zeros((width, height))
a2 = np.zeros((width, height))
v1 = np.zeros((width, height))
v2 = np.zeros((width, height))

# Zentraler Impuls
cx, cy = width // 2, height // 2
#a1[cx-1:cx+2, cy-1:cy+2] = 1.0

# Pygame vorbereiten
pygame.init()
screen = pygame.display.set_mode((2 * width * scale, height * scale))
pygame.display.set_caption("λΔ: Wellenfunktion & Phasenrichtung")

def psi_to_rgb(a1, a2):
    mag = np.sqrt(a1**2 + a2**2)
    phase = np.arctan2(a2, a1)
    hue = (phase + np.pi) / (2 * np.pi)
    sat = np.ones_like(hue)
    val = np.clip(mag, 0, 1)
    hsv = np.stack((hue, sat, val), axis=-1)
    rgb = mcolors.hsv_to_rgb(hsv)
    return (rgb * 255).astype(np.uint8)

# Endlossimulation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type in( pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION )  and pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            gx, gy = (mx % (width * scale)) // scale, my // scale
            if 0 <= gx < width and 0 <= gy < height:
                a1[gx, gy] += 1.0

    # todo/future: modifiziere die zeit, um zu versuchen gravitation zu simulieren
    
    # Dynamik der Wellenfunktion
    f1 = laplace_strength * laplacian2(a1) -masse1*a1
    f2 = laplace_strength * laplacian2(a2) -masse2*a2

    v1 += f1 * dt - rotation_speed * a2 * dt
    v2 += f2 * dt + rotation_speed * a1 * dt

    v1 *= damping
    v2 *= damping

    a1 += v1 * dt
    a2 += v2 * dt

    # Bild links: RGB-Wellenfunktion
    rgb_image = psi_to_rgb(a1, a2)
    surface1 = pygame.surfarray.make_surface(rgb_image) #.swapaxes(0, 1))
    surface1 = pygame.transform.scale(surface1, (width * scale, height * scale))
    screen.blit(surface1, (0, 0))

    # Bild rechts: Phasengradient-Vektorfeld
    phase = np.arctan2(a2, a1)
    grad_x = np.roll(phase, -1, axis=0) - np.roll(phase, 1, axis=0)
    grad_y = np.roll(phase, -1, axis=1) - np.roll(phase, 1, axis=1)

    grad_mag = np.sqrt(grad_x**2 + grad_y**2) + 1e-6
    dx = grad_x / grad_mag
    dy = grad_y / grad_mag

    surface2 = pygame.Surface((width * scale, height * scale))
    surface2.fill((0, 0, 0))
    
    for x in range(0, width, arrow_spacing):
        for y in range(0, height, arrow_spacing):
            cx = x * scale
            cy = y * scale
            ex = int(cx + dx[x, y] * scale * arrow_spacing/3)
            ey = int(cy + dy[x, y] * scale * arrow_spacing/3)
            pygame.draw.line(surface2, (255, 255, 0), (cx, cy), (ex, ey), 1)

    screen.blit(surface2, (width * scale, 0))
    pygame.display.flip()
