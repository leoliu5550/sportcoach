import sys
sys.path.append("//Users//leoliu//Documents//fitproject")
from utils import timer as nw
class Test_timer(object):
    def test_now_date(self):
        self.tim = nw
        assert self.tim.now_date()[0] == 6
        assert self.tim.now_date()[1] == "Sunday"
    
