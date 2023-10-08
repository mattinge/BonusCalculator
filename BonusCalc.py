#Algo to calculate points for staff bonus in medical office


def BonusCalc(workHrs, numFollowUps, numEvals):
    totalPoints = (numEvals * 1.5) + numFollowUps
    numPatients = numFollowUps + numEvals
    
    if workHrs > 32:
        return 0
    elif workHrs == 32:
        if numPatients < 40:
            return 0
        elif numPatients >= 40:
            bonusNum = totalPoints - 40
            if bonusNum <= 0:
                return 0
            else:
                return bonusNum
    elif workHrs >= 40:
        if numPatients < 50:
            return 0
        elif numPatients > 50:
            bonusNum = totalPoints -50
            if bonusNum <= 0:
                return 0
            else:
                return bonusNum
            

result = BonusCalc(32,45,0)
print(result)