class UIManager():
    def __init__(self, render):
        self.elements = [] #create the list of elements
        self.render = render
    
    def draw_all(self):
        for element in self.elements:
            element.draw(self.render.screen)
    
    def add(self, element):
        self.elements.append(element)

    def handle_events(self, event):
        for element in self.elements:
            element.handle_event(event)