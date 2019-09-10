import random
def randomNames(dict):
    teamNum = random.randint(0,len(dict)-1)
    if (teamNum == 0):
        tempList = dict["orpheus"]
    elif (teamNum == 1):
        tempList = dict["rex"]
    else:
        tempList = dict["endymion"]

    nameNum = random.randint(0,len(tempList)-1)
    print(tempList[nameNum])


randomNames({"orpheus": ["Emily", "Kevin", "Vishwaa", "Eric"],
             "rex":     ["William", "Joseph", "Calvin", "Ethan"],
             "endymion":["Grace", "Nahi", "Derek", "Connor"]})
