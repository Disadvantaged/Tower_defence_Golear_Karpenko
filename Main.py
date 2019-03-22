import pygame
pygame.init()

FPS = 60
WIDTH = 600
HEIGHT = 800


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def main():
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    clock = pygame.time.Clock()
    pygame.draw.circle(screen, (255, 255, 255, 0), (150, 150), 15)
    while True:
        clock.tick(FPS)

        handle_events()
        pygame.display.update()


if __name__ == '__main__':
    main()


