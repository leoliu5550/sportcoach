import sys,json
sys.path.append("//Users//leoliu//Documents//fitproject")
from utils import datageter as gt

data_gt =gt.sport()

class Test_data(object):
    def test_status_data(self):
        with open('data//STATUS.json','r') as file:
            data = json.load(file)
        assert data == data_gt.status_data()

    def test_sport_data(self):
        with open('data//SPORT.json','r') as file:
            data = json.load(file)
        assert data == data_gt.sport_data()