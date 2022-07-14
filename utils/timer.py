import datetime
from typing import Tuple

def Getdate() -> Tuple[str, str]:

    timer = datetime.datetime.now()
    day = timer.weekday()
    timer_out = timer.strftime("%Y-%m-%d") # %H:%M
    return (str(day),timer_out)

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


day = Getdate()
print(day)