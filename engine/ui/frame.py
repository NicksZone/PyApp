import pygame
from ..ui.uielement import UIElement

class Frame(UIElement): #TODO: add a imageButton later
    def __init__(self, x, y, h, w):
        super().__init__(x, y, w, h)
        

    # def draw(self, screen): # inherited
    #     # draw the children
    #     self.draw()
        
    # def add_child(self, child): # inherited
    #     # add a child
    #     self.children.append(child)
        

    def handle_event(self, event): # inherited
        return super().handle_event(event)