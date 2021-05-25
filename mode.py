import csv
from collections import Counter
with open ('Copy+of+data+-+data.csv', newline = '') as f :
    reader = csv.reader(f)
    data = list(reader)
data.pop (0)
newdata = []
for i in range (len(data)):
    num = data [i][1]
    newdata.append(float(num))
data1 = Counter(newdata)
modeforrange = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}    
for height,accurance in data1.items ():
    if 50 < float (height)<60:
        modeforrange["50-60"]+=accurance
    
    if 60 < float (height)<70:
        modeforrange["60-70"]+=accurance
    
    if 70 < float (height)<80:
        modeforrange["70-80"]+=accurance    
moderange,modeaccurance = 0,0
for range,accurance in modeforrange.items():
     if accurance>modeaccurance:
         moderange,modeaccurance = [int(range.split("-")[0]),int(range.split("-")[1])],accurance
mode = float ((moderange[0]+moderange[1])/2)
print (mode)