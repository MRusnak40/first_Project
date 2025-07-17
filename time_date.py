import datetime

date = datetime.date(2025,1,2)



time= datetime.time
time = datetime.time(hour=1,minute=1,second=1)
now = datetime.datetime.now()

now=now.strftime("%m/%d/%Y, %H:%M:%S")
print(now)