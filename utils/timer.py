import datetime
from typing import Tuple

def now_date() -> Tuple[str, str]:
    weekDays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )
    day = datetime.datetime.now()
    day = day.weekday()
    return (str(day),weekDays[day]) 