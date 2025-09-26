from Data import HtmlReader
import pygame
import engine

class Application:
    def __init__(self):
        self.Display = engine.Render(1500, 600, "Weather App")
        self.Ui = engine.UIManager(self.Display)
        self.DataReader = HtmlReader('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current=temperature_2m')
    
    def run(self):
        self.loadui()
        
        self.Display.run(self.Ui)
        #while self.Display.running:
        pass
    
    def loadui(self):
        self.Display.renderBackground("black")
        
        font = pygame.font.SysFont('arial', 24)
        
        button = engine.Button(200, 200, 100, 100, "Test button", font, "green")
        image = engine.Image(100,100, "assets/Test.png")
        
        image.add_child(button)
        
        #self.Ui.add(button)
        self.Ui.add(image)