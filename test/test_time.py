import sys
sys.path.append("//Users//leoliu//Documents//fitproject")
from utils.timer import *
import pytest
import datetime

class Test_timer(object):

    def test_Getdate(self):
        day = datetime.datetime.now().weekday()
        assert Getdate()[0] == str(day)
        
    def test_trans_read(self,mocker):
        mock_value = ('3', '2022-07-14')
        Getdate_ = mocker.patch(
            "utils.timer.Getdate",
            return_value=mock_value)
        time_ = Getdate()
        assert trans_read(time_) == "Thursday"

