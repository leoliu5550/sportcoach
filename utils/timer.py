import datetime
from typing import Tuple

def now_date() -> Tuple[str, str]:
    # weekDays = (
    #     "Monday",
    #     "Tuesday",
    #     "Wednesday",
    #     "Thursday",
    #     "Friday",
    #     "Saturday",
    #     "Sunday"datetime.datetime.now()
    # )
    timer = datetime.datetime.now()
    day = timer.weekday()
    timer_out = timer.strftime("%Y-%m-%d") # %H:%M
    return (str(day),timer_out)
