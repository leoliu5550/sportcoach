import sys,json,pytest
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

    def test_sport_geter(self,mocker):
        # 對Product中的方法的返回值進行Mock
        mock_value = {"0":["REST","SLOWEAR"]}
        data_gt.status_data = mocker.patch(
            "utils.datageter.sport.status_data",
            return_value=mock_value)
        #  (str(day),weekDays[day]) 

        sportType = data_gt.sport_geter(("0","Sunday"))

        assert sportType == ["REST","SLOWEAR"]
    # def sport_geter(self,date:Tuple) -> list:
    #     status_data = self.status_data()
    #     sport_index = status_data[date[0]]

    #     return sports_index