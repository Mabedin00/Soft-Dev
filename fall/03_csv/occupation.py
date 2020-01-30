import random

file = open("occupations.csv", "r")
workingList = file.readlines()[1:len(file.readlines())-1]
workingDict = {}
for job in workingList:
    job = job.rsplit(",", 1)
    workingDict.update({job[0]: job[1]})
file.close()
#print(workingDict)

def randomPick():
    largeList = []
    for job in workingDict:
        counter = 0
        while (counter < float(workingDict.get(job)) * 10):
            largeList.append(job)
            counter += 1
    return random.choice(largeList)

print(randomPick())
