import requests

class HtmlReader:
    def __init__(self, parent, directory):
        #inherit parent functions
        self.parent = parent

        #define important varaiables
        self.directory = directory

    def getWeekData(self) -> list[dict]:
        #get response and convert it to JSON
        response = requests.get(self.directory)
        data = response.json()

        print(data)

        Days = []
        for day, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]):
            DayData = {
                "date": day,
                "temp": temp
            }

            Days.append(DayData)       
        
        return Days