import pygame
from ..ui.uielement import UIElement

class Image(UIElement): #TODO: add a imageButton later
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        w, h = self.image.get_size()
        super().__init__(x, y, w, h)

    def draw_self(self, screen): # inherited
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, "black", self.rect, 2)

    def handle_event(self, event): # inherited
        return super().handle_event(event)