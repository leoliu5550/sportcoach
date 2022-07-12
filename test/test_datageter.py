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

    def test_status_geter(self,mocker):
        # 對Product中的方法的返回值進行Mock
        mock_value = {"0":["REST","SLOWEAR"]}
        data_gt.status_data = mocker.patch(
            "utils.datageter.sport.status_data",
            return_value=mock_value)

        sportType = data_gt.status_geter(("0","Sunday"))
        assert sportType == ["REST","SLOWEAR"]

    def test_aerobic(self,mocker):
        mock_value = {
            "SPORT":{
                "Aerobic":{
                    "HIIT":{
                        "前跨步":{"Mark":[2]}
                        },
                    "SLOWEAR":{
                        "跳繩":{"Mark":[4]}
                    }
                }
            }
        }

        data_gt.sport_data = mocker.patch(
            "utils.datageter.sport.sport_data",
            return_value=mock_value)

        data = ["SLOWEAR","HIIT",0,1]
        assert data_gt.aerobic(data[0]) == "跳繩"
        assert data_gt.aerobic(data[1]) == "前跨步"
        assert data_gt.aerobic(data[2]) == "跳繩"
        assert data_gt.aerobic(data[3]) == "前跨步"  

    def test_weight(self,mocker):
        mock_value = {
            "SPORT":{
                "Aerobic":{},
                "Weight":{
                    "Strength":{
                        "Upper_S":{"Mark":[0]}
                        },
                    "Endurance":{
                        "ABS_E":{"Mark":[1]}
                    }
                }
            }
        }
        data_gt.sport_data = mocker.patch(
            "utils.datageter.sport.sport_data",
            return_value=mock_value)
        data = ["Strength","Endurance",0,1]
        assert data_gt.weight(data[0]) == "Upper_S"
        assert data_gt.weight(data[1]) == "ABS_E"
        assert data_gt.weight(data[2]) == "Upper_S"
        assert data_gt.weight(data[3]) == "ABS_E"

    def test_core(self,mocker):
        mock_value = {
            "SPORT":{
                "CORE":{
                    "sides":{"Mark":[1]},
                    "abs":{"Mark":[1]}
                }
            }
        }
        data_gt.sport_data = mocker.patch(
            "utils.datageter.sport.sport_data",
            return_value=mock_value)
        data = None
        assert data_gt.core(data) == ["sides" ,"abs"]

    def test_soft(self):
        assert data_gt.soft(0) == "Upper"
        assert data_gt.soft(1) == "CORE"
        assert data_gt.soft(2) == "LEG"
        assert data_gt.soft(3) == "BACK"
        pass

    def test_dict_dict_reverse(self):
        test = {'a':3 }
        result = data_gt.dict_reverse(test)
        assert result == {3:'a'}
