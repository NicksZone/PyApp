import pygame
from ..ui.uielement import UIElement

class Button(UIElement): #TODO: add a imageButton later
    def __init__(self, x, y, width, height, text, font, color):
        super().__init__(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color

    def draw(self, screen): # inherited
        pygame.draw.rect(screen, )
    
    def handle_event(self, event): # inherited
        return super().handle_event(event)