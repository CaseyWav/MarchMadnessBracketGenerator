import random

def calcWinner(team1SeedWinPct,team2SeedWinPct, team1NetRank, team2NetRank, team1Rpi, team2Rpi):
     #historical seed win pct
    num = coinFlip(team1SeedWinPct,team2SeedWinPct)

    #net ranking
    num = num + coinFlip(team1NetRank,team2NetRank)

    #If one of the teams won twice
    if num % 2 == 0:
        if num < 3:
            num = 0
        else:
            num = 1
    #If both teams won once, need a tie breaker
    else:
        num = 0 if coinFlip(team1Rpi, team2Rpi) == 1 else 1


def coinFlip(team1, team2):
    
    sum = team1 + team2
    
    randNum = random.random()

    if sum > 1:
        #how much over 100%
        surplusPct = sum - 1

        half = surplusPct / 2

        team1 = team1 - half
        #team2SeedWinPct = team2SeedWinPct - half

    elif sum < 1:
        #how much under 100%
        shortagePct = 1 - sum

        half = shortagePct / 2

        team1 = team1 + half
        #team2SeedWinPct = team2SeedWinPct + half

    if randNum <= team1:
        return 1
    else:
        return 2






