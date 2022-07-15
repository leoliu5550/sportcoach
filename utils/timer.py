import datetime
from typing import Tuple

def Getdate() -> Tuple[str, str]:
    timer = datetime.datetime.now()
    day = timer.weekday()
    timer_out = timer.strftime("%Y-%m-%d") # %H:%M
    return (str(day),timer_out)

def time_segment() -> Tuple:
    seg = {
        0:'Morning',
        1:'Afternoon',
        2:'Beforesleep',
        3:'Rest'        
    }

    with open('data//config.yaml', 'r') as f:
        TIMESEG = yaml.safe_load(f)
        TIMESEG = TIMESEG['TIMESEG']
    timer = datetime.datetime.now()
    time = int(timer.strftime("%H"))
    def rod(data):
        if data[0] > data[1]:
            data[0],data[1] = data[1],data[0]
            return data
        return data
    
    mon = rod(TIMESEG['MORNING'])
    noon = rod(TIMESEG['AFTERNOON'])
    sleep = rod(TIMESEG['BEFORESLEEP'])

    if time in range(mon):
        result = seg[0]
    elif time in range(noon):
        result = seg[1]
    elif time in range(sleep):
        result = seg[2]
    else:
        result = seg[3]

    return result 


def trans_read(time_) -> str:
    Days = time_
    """
    should get now_date func
    """
    weekDays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )
    Days = weekDays[int(time_[0])]
    return Days