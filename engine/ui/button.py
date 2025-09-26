import pygame
from ..ui.uielement import UIElement

class Button(UIElement): #TODO: add a imageButton later
    def __init__(self, x, y, width, height, text, font, color):
        super().__init__(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color

    def draw_self(self, screen): # inherited
        pygame.draw.rect(screen, self.color, self.rect)
        
        pygame.draw.rect(screen, "black", self.rect, 2)
        # Optionally, draw text:
        if self.text:
            text_surface = self.font.render(self.text, True, (0,0,0))
            # center text inside the button
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    
    def handle_event(self, event): # inherited
        return super().handle_event(event)