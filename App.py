from Data import HtmlReader
import pygame
import engine

class Application:
    def __init__(self):
        self.Display = engine.Render(1500, 600, "Weather App")
        self.Ui = engine.UIManager(self.Display)
        self.DataReader = HtmlReader('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current=temperature_2m')
    
    def run(self):
        self.Display.renderBackground("black")
        
        font = pygame.font.SysFont('arial', 24)
        
        self.Ui.add(engine.Button(100, 100, 100, 100, "Test button", font, "white"))
        
        
        self.Display.run(self.Ui)
        #while self.Display.running:
        pass