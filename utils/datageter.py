import json
from typing import Any,Dict

class sport(object):
    def __init__(self) -> None:
        pass

    def status_data(self,path='') -> any:
        if path == '':
            path = 'data//STATUS.json'
        with open(path,'r') as file:
            data = json.load(file)
        return data

    def sport_data(self,path='') -> any:
        if path =='':
            path = 'data//SPORT.json'
        with open(path,'r') as file:
            data = json.load(file)
        return data    

