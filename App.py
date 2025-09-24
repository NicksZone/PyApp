from Data import HtmlReader
from engine import Render

class Application:
    def __init__(self):
        self.Display = Render(1500, 600, "Weather App")
        self.DataReader = HtmlReader('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current=temperature_2m')
    
    def run(self):
        self.Display.run(self.Display)
        #while self.Display.running:
        pass