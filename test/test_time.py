import sys
sys.path.append("//Users//leoliu//Documents//fitproject")
from utils import timer as nw
import pytest
import datetime

class Test_timer(object):
    def test_now_date(self,mocker):
        self.tim = nw
        day = datetime.datetime.now().weekday()
        assert self.tim.now_date()[0] == str(day)
        
    
