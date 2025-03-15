import csv
import random
import marchMadnessData as marMadData
import marchMadnessCalc as marMadCalc

#This code is written by Casey C W.

brackets = []

marMadData.generateTeamList()

#150k rows is close to the 100MB upload limit for Github
file = 'brackets(150k)_generation_1.csv'

with open(file,'w',newline='') as f:

        writer = csv.DictWriter(f, fieldnames=marMadData.headers)
        writer.writeheader()

        i = 0
        rowNum = 0
# Simulate the tournament
        for bracket in brackets:

            # Round 1
            rowNum = rowNum + 1
            bracket['Bracket Number'] = str(rowNum)

            #First Round

            #look into f string python (dynamically pass in f string)
            #look into using pandas

            for a in range(32):
                bracket[f'Round 1 Winner {}' + str(a+1)] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                        marMadData.round_1_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                        marMadData.round_1_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
                i = i + 2

            #Second Round
            for b in range(16):
                
                #look into filter(lambda s: s.seed == bracket['Round 1 Winner '+str(b+1)], marchMadnessData.teamList)

                bracket['Round 2 Winner ' + str(b+1)] = bracket['Round 1 Winner '+str(b+1)] if marMadCalc.calcWinner(
                        marMadData.round_2_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                        marMadData.round_2_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)
                        ) == 1 else marMadData.teamList[i+1].name
            #Sweet 16
            for c in range(8):
                bracket['Sweet 16 Winner ' + str(c)] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                        marMadData.sweet_16_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                        marMadData.sweet_16_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
            #Elite 8
            for d in range(4):
                bracket['Elite 8 Winner ' + str(d)] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                        marMadData.elite_8_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                        marMadData.elite_8_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
            #Final Four
            bracket['Final Four Winner 1'] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
            
            bracket['Final Four Winner 2'] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
            
            bracket['Championship Winner'] = marMadData.teamList
            
           # writer.writerow([bracket])
            writer.writerow(bracket)
