import pygame

class UIElement:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        pass

    def draw(self, screen):
        raise NotImplementedError
    
    def handle_event(self, event):
        pass #not all elements require events

