intervals = [(0,30),(5,10),(15,20),(2,4)]
intervals.sort(key = lambda x: x[0])
print(intervals)

intervals = [(0,30),(5,10),(15,20),(2,4)]
intervals.sort(key = lambda x: x[1])
print(intervals)

