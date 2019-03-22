import pygame
from Grass import Grass
from Road import Road


class Game:
    def __init__(self, width, height, fps, s):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.FPS = fps
        self.caption = s
        self.cells = []
        self.pressed_cell = None

        pygame.display.set_caption(s)

        grass = Grass((50, 50), (40, 40))
        road = Road((400, 400), (50, 50))

        self.cells.append(grass)
        self.cells.append(road)
        self.screen.blit(grass.get_image(), grass.get_position())
        self.screen.blit(road.get_image(), road.get_position())

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for cell in self.cells:
                    if cell.get_rect().collidepoint(event.pos):
                        self.pressed_cell = cell
                else:
                    if self.pressed_cell is not None:
                        x = event.pos[0] - self.pressed_cell.get_width() // 2
                        y = event.pos[1] - self.pressed_cell.get_height() // 2
                        rect = pygame.Rect(x, y, self.pressed_cell.get_width(), self.pressed_cell.get_height())
                        if rect.collidelist(self.cells) == -1:

                            new_cell = self.pressed_cell.copy((x, y))
                            self.pressed_cell = None
                            self.screen.blit(new_cell.get_image(), new_cell.get_position())
                            self.cells.append(new_cell)

    def main_loop(self):
        while True:
            self.clock.tick(self.FPS)

            self.handle_events()
            pygame.display.update()
