import sys
from datetime import datetime

PATH = sys.argv[1]

class Interval:
    def __init__(self, time, flag,id=-1):
        self.time = time
        self.flag = flag
        self.id = id

    def __lt__(self, other):
        return self.time < other.time

class MaxInterval:
    def __init__(self, time, flag,id,count):
        self.time = time
        self.flag = flag
        self.id = id
        self.count = count

    def __lt__(self, other):
        return self.time < other.time


intervals = []
id = 0

with open(PATH) as file:
    for line in file:
        intervals.append(Interval(datetime.time(datetime.strptime(line.split()[0],'%H:%M')),'start',id))
        intervals.append(Interval(datetime.time(datetime.strptime(line.split()[1],'%H:%M')),'end',id))
        id +=1

intervals.sort()

count = 0
maxCount = 0

max_interv = []

for time in range (len(intervals)):
    if intervals[time].flag == 'start':
        count += 1
    else:
        count -= 1
    maxCount = max(count, maxCount)
    max_interv.append(MaxInterval(intervals[time].time, intervals[time].flag, intervals[time].id, count))

union = []


for time in range(len(max_interv )):
    #print(max_interv[time].time,max_interv[time].flag,max_interv[time].count)
    if max_interv[time].count == maxCount :
        if max_interv[time-1].count < maxCount and max_interv[time-2].count < maxCount:
            union.append( max_interv[time].time)
    if time == len(max_interv )-1:
        pass
    else:
        if max_interv[time].count < maxCount and max_interv[time+1].count < maxCount and max_interv[time-1].count == maxCount:
            union.append( max_interv[time].time)
union.sort()
i = 0
while i < len(union):
    print(union[i].strftime("%H:%M"),union[i+1].strftime("%H:%M"))
    i+=2


















