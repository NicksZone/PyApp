import pygame

class UIElement:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.children = []
        pass
    
    def add_child(self, child):
        self.children.append(child)

    def draw(self, screen):
        # draw self (subclasses implement _draw_self)
        self.draw_self(screen)

        # draw children relative to this element
        for child in self.children:
            child.draw_at(screen, self.rect.x + child.rect.x, self.rect.y + child.rect.y)
    
    def draw_self(self, screen):
        #chilrden classes override this
        raise NotImplementedError
    
    def draw_at(self, screen, offset_x, offset_y):
        # draw at edited cords
        self.rect = pygame.Rect(offset_x, offset_y, self.rect.width, self.rect.height)
        self.draw_self(screen)
        pass
    
    def handle_event(self, event):
        pass #not all elements require events

