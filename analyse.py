# you can download raw data on http://ocslab.hksecurity.net/Datasets/CAN-intrusion-dataset

import json
from itertools import groupby
from operator import itemgetter

numberOfTimeSegments = 10
f = open("data/DoS.csv", "r")
f_new = open("data/DoS.json", "w")

fHandler = f.readlines()
startTime = float(fHandler[0].split(",")[:1][0])
endTime = float(fHandler[len(fHandler) - 1].split(",")[:1][0])

stats = [[]]
statsCount = [[]]

count = (endTime - startTime) / numberOfTimeSegments

counter = 0
lineIndex = 0
print len(fHandler)

blocks = [[]]
for s in fHandler:
    packet = s.split(",")
    if float(packet[0]) > (startTime + count):
        startTime += count
        counter += 1
        blocks.append([])
    del packet[0]
    blocks[counter].append(packet)

countBlocks = []

def mapMyList(s):
    return [[s[0],s[1:]], 1]

def reduceMyList (s1, s2):
    return s1[0], s1[1] + s2[1]

counter = 1
res = []
for b in blocks:
    b = list(map(mapMyList, b))
    res.append([reduce(reduceMyList, group) for _, group in groupby(sorted(b), key=itemgetter(0))])
    counter += 1

ids = []
for b in res:
    for record in b:
        if record[0][0] not in ids:
            ids.append(record[0][0])

resMap = []
counter = 0
for b in res:
    resMap.append({})
    for id in ids:
        resMap[counter][id]=[]
    for record in b:
        resMap[counter][record[0][0]].append([record[0][1], record[1]])
    counter += 1

for b in resMap:
    for dev in b:
        b[dev] = sorted(b[dev], key=lambda x: x[1])

json.dump(resMap, f_new)

f.close()
f_new.close()
