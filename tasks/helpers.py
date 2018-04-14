from datetime import date,timedelta,time,timezone

def daterange(date1, date2):
    
    delta = date2 - date1

    for n in range(delta.days+1):
        yield date1 + timedelta(days=n)
