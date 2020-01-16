import sys
import pygame

pygame.init()

size = width, height = 320, 240

screen = pygame.display.set_mode(size)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((255,255,255))
        pygame.display.flip()
