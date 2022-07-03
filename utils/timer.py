import datetime

def now_date():
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    day = datetime.datetime.now()
    day = day.weekday()
    return (day,weekDays[day]) 
