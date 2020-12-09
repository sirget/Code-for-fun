import datetime

timestr = '15-05-2020 - 18:04:30'
time = datetime.datetime.strptime(timestr, "%d-%m-%Y - %H:%M:%S")
print(time)
x = datetime.datetime.now()
print(x)
date = datetime.datetime.timestamp(x)
print(date)
sttotime = datetime.datetime.fromtimestamp(date)
print(sttotime)
print(type(sttotime))
strt = str(sttotime)
print(type(strt))
