import json
from typing import Any,Dict,Tuple

class sport(object):
    
    def __init__(self) -> None:
        pass

    def status_data(self,path='') -> Dict[str, list]:
        if path == '':
            path = 'data//STATUS.json'
        with open(path,'r') as file:
            data = json.load(file)
        return data

    def sport_data(self,path='') -> Any:
        if path =='':
            path = 'data//SPORT.json'
        with open(path,'r') as file:
            data = json.load(file)
        return data    

    #  should get timer (str(day),weekDays[day]) 
    def status_geter(self,data:Tuple) -> list:
        status_data = self.status_data()
        sport_index = data[0]
        sportType = status_data[sport_index]
        return sportType 

    def sport_geter(self):

        pass

    