# handles rendering

import pygame

from typing import TYPE_CHECKING

#doesn't run runtime
if TYPE_CHECKING:
    from manager import UiManager

class Render:
    def __init__(self, x =  400, y = 1500, caption = "Untitled", fps = 60):
        pygame.init()
        #define important variables
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()
        self.fps = fps
        pygame.display.set_caption(caption)
        self.running = False
        self.font = pygame.font.Font(None, 24)

    # def renderText(self, x, y, text = "", color = (1,1,1)):
    #     print(text)
    #     text_surface = self.font.render(text, True, color)
    #     self.screen.blit(text_surface, (x, y))

    def renderBackground(self, color):
        self.screen.fill(color)

    # def renderDays(self, data):
    #     x = 0
    #     for day in data:
    #         text = f"Date: {day['date']} | Temp: {day['temp']}"
    #         self.renderText(10, x, text, (1,1,1))
    #         x += 50
    
    def run(self, ui):
        self.renderBackground("white")
        self.running = True

        #self.renderText(100, 100, "Welcome to weather app", "black")

        #self.renderDays(self.parent.DataReader.getWeekData())
        #ui.draw_all() #draw all the ui on the screen

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            pygame.display.flip()
            
            self.clock.tick(self.fps)
        
        pygame.quit()
