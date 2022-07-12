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
    def aerobic(self,data) -> str:
        '''data should be SLOWEAR:0 or HIIT:1'''
        sportbase = self.sport_data()["SPORT"]["Aerobic"]
        if data == "SLOWEAR" or data == 0:
            sportbase = sportbase["SLOWEAR"]
        if data == "HIIT" or data == 1:
            sportbase = sportbase["HIIT"]

        sportbase = list(sportbase.keys())
        result = random.choice(sportbase)
        return result

    # Weight PART
    def weight(self,data) -> str:
        '''data should be Strength:0 or Endurance:1'''
        sportbase = self.sport_data()["SPORT"]["Weight"]
        if data == "Strength" or data == 0:
            sportbase = sportbase["Strength"]
        if data == "Endurance" or data == 1:
            sportbase = sportbase["Endurance"]

        sportbase = list(sportbase.keys())  
        result = random.choice(sportbase)
        return result 

    # core PART
    def core(self,data) -> list:
        '''passing all core data'''
        sportbase = self.sport_data()["SPORT"]["CORE"]
        sportbase = list(sportbase.keys())  
        return sportbase

    # soft must part
    def soft(self,mark) ->str:
        sportbase = self.sport_data()["SPORT"]["SOFT"]
        result = sportbase[str(mark)]

        return result

    def dict_reverse(self,data:Dict) -> Dict:
        result = dict()
        for key in data.keys():
            result.update({data[key]:key})
        return result