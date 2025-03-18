import random


def calcWinner(team1SeedWinPct, team2SeedWinPct):
    
    sum = team1SeedWinPct + team2SeedWinPct
    
    randNum = random.random()

    if sum > 1:
        #how much over 100%
        surplusPct = sum - 1

        half = surplusPct / 2

        team1SeedWinPct = team1SeedWinPct - half
        #team2SeedWinPct = team2SeedWinPct - half

    elif sum < 1:
        #how much under 100%
        shortagePct = 1 - sum

        half = shortagePct / 2

        team1SeedWinPct = team1SeedWinPct + half
        #team2SeedWinPct = team2SeedWinPct + half

    if randNum <= team1SeedWinPct:
        return 1
    else:
        return 2






