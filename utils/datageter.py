import json
from typing import Any,Dict,Tuple
import random

class sport(object):
    
    def __init__(self,status_path = '',sport_path = '') -> None:
        if status_path != '':
            self.status_path = status_path
        else:
            self.status_path = 'data//STATUS.json'

        if sport_path != '':
            self.sport_path = sport_path
        else:
            self.sport_path = 'data//SPORT.json'
        pass

    def status_data(self) -> Dict[str, list]:
        path = self.status_path

        with open(path,'r') as file:
            data = json.load(file)
        return data

    def sport_data(self) -> Any:
        path = self.sport_path

        with open(path,'r') as file:
            data = json.load(file)
        return data    
    
    #  should get timer (str(day),weekDays[day]) 
    def status_geter(self,data:Tuple) -> list:
        status_data = self.status_data()
        sport_index = data[0]
        sportType = status_data[sport_index]
        return sportType 

    # Aerobic PART
    def aerobic(self) -> str:
        sportbase = sport_data()["SPORT"]
        
        if data[1] == "SLOWEAR":
            sportbase = sportbase["Aerobic"]["SLOWEAR"]
            
            pass
        else: #  data[1] == "HIIT"
            sportbase = sportbase["Aerobic"]["HIIT"]
            pass
        sportbase = list(sportbase.keys())
        result = random.choice(sportbase)

        return result

    # Weight PART
    def Weight(self,category:int) -> str:
        '''
        category:
            0 : "Strength"  set 8
            1 : "Endurance" set 20
        '''
        sportbase = sport_data()["SPORT"]["Weight"]
        if category == 0:
            sportbase = sportbase["Strength"]
        else:
            sportbase = sportbase["Endurance"]

        sportbase = list(sportbase.keys())  
        result = random.choice(sportbase)
        return result 



    def sport_geter(self,data:list) -> None:

        sportbase["Weight"]
        sportbase["Soft"]

        pass

