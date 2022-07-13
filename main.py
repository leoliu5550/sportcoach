from utils import timer,datageter
import pickledb

def main():
    db = pickledb.load('data#RECROD.db', True)

    # get first timestamp at here
    TIME_INFO = timer.now_date()
    print(TIME_INFO)
    # create the current day record
    if db.dexists("record",TIME_INFO[1]) == False:
        db.dadd("record",(TIME_INFO[1],{}))
    
    sporter = datageter.sport()
    statusType = sporter.status_geter(TIME_INFO)
    print(statusType)

    #sdfsdfsd
    pass



if __name__ == "__main__":
    main()