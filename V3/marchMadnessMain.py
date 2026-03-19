import csv
import random
import marchMadnessData as marMadData
import marchMadnessCalc as marMadCalc

#This code is written by Casey C W.

brackets = []
brackets.append(marMadData.bracket_data)

marMadData.generateTeamList()

#150k rows is close to the 100MB upload limit for Github
file = 'brackets(150k)_generation_1.csv'

with open(file,'w',newline='') as f:

        writer = csv.DictWriter(f, fieldnames=marMadData.headers)
        writer.writeheader()

        rowNum = 0
# Simulate the tournament
        for x in range(marMadData.num_brackets):
          i = 0
          
          for bracket in brackets:

              # Round 1
              rowNum = rowNum + 1
              bracket['Bracket Number'] = str(rowNum)

              #First Round
              for a in range(32):
                  
                  num = marMadCalc.calcWinner(
                      marMadData.round_1_seed_hist_win_pct.get(marMadData.teamList[i].seed),
                      marMadData.round_1_seed_hist_win_pct.get(marMadData.teamList[i+1].seed),
                      marMadData.teamList[i].netRanking,
                      marMadData.teamList[i+1].netRanking,
                      marMadData.teamList[i].rpi,
                      marMadData.teamList[i+1].rpi)

                  bracket['Round 1 Winner ' + str(a+1)] = marMadData.teamList[i].name if num == 0 else marMadData.teamList[i+1].name 
                  #Round1Team2.name #marMadData.teamList[i+num].name
                  
                  i = i + 2
                  
              i = 1
        
              #Second Round
              for b in range(16):
                  
                  Round1Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 1 Winner '+ str(i)])
                  Round1Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 1 Winner '+ str(i+1)])

                  num = marMadCalc.calcWinner(
                      marMadData.round_2_seed_hist_win_pct.get(Round1Team1.seed),
                      marMadData.round_2_seed_hist_win_pct.get(Round1Team2.seed),
                      Round1Team1.netRanking,
                      Round1Team2.netRanking,
                      Round1Team1.rpi,
                      Round1Team2.rpi)
                  
                  bracket['Round 2 Winner ' + str(b+1)] = Round1Team1.name if num == 0 else Round1Team2.name

                  #bracket['Round 2 Winner ' + str(b+1)] = Round1Team1.name if marMadCalc.calcWinner(
                   #       marMadData.round_2_seed_hist_win_pct.get(Round1Team1.seed), 
                    #      marMadData.round_2_seed_hist_win_pct.get(Round1Team2.seed)
                     #     ) == 1 else Round1Team2.name
                  
                  i = i + 2

              i = 1
          
              #Sweet 16
              for c in range(8):

                  Round2Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 2 Winner '+ str(i)])
                  Round2Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 2 Winner '+ str(i+1)])
                  
                  num = marMadCalc.calcWinner(
                      marMadData.sweet_16_seed_hist_win_pct.get(Round2Team1.seed),
                      marMadData.sweet_16_seed_hist_win_pct.get(Round2Team2.seed),
                      Round2Team1.netRanking,
                      Round2Team2.netRanking,
                      Round2Team1.rpi,
                      Round2Team2.rpi)
                  
                  bracket['Sweet 16 Winner ' + str(c+1)] = Round2Team1.name if num == 0 else Round2Team2.name

                  #bracket['Sweet 16 Winner ' + str(c+1)] = Round2Team1.name if marMadCalc.calcWinner(
                   #       marMadData.sweet_16_seed_hist_win_pct.get(Round2Team1.seed), 
                    #      marMadData.sweet_16_seed_hist_win_pct.get(Round2Team2.seed)
                     #     ) == 1 else Round2Team2.name 

                  i = i + 2

              i = 1

              #Elite 8
              for d in range(4):

                  Sweet16Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Sweet 16 Winner ' + str(i)])
                  Sweet16Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Sweet 16 Winner ' + str(i+1)])
                  
                  num = marMadCalc.calcWinner(
                      marMadData.elite_8_seed_hist_win_pct.get(Sweet16Team1.seed),
                      marMadData.elite_8_seed_hist_win_pct.get(Sweet16Team2.seed),
                      Sweet16Team1.netRanking,
                      Sweet16Team2.netRanking,
                      Sweet16Team1.rpi,
                      Sweet16Team2.rpi)
                  
                  bracket['Elite 8 Winner ' + str(d+1)] = Sweet16Team1.name if num == 0 else Sweet16Team2.name



                 # bracket['Elite 8 Winner ' + str(d+1)] = Sweet16Team1.name if marMadCalc.calcWinner(
                 #         marMadData.elite_8_seed_hist_win_pct.get(Sweet16Team1.seed), 
                 #         marMadData.elite_8_seed_hist_win_pct.get(Sweet16Team2.seed)
                 #         ) == 1 else Sweet16Team2.name

                  i = i + 2

              i = 1

              #Final Four
              for e in range(2):
                  Elite8Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Elite 8 Winner '+str(i)])
                  Elite8Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Elite 8 Winner '+str(i+1)])
                  
                  num = marMadCalc.calcWinner(
                      marMadData.final_4_seed_hist_win_pct.get(Elite8Team1.seed),
                      marMadData.final_4_seed_hist_win_pct.get(Elite8Team2.seed),
                      Elite8Team1.netRanking,
                      Elite8Team2.netRanking,
                      Elite8Team1.rpi,
                      Elite8Team2.rpi)
                  bracket['Final 4 Winner ' + str(e+1)] = Elite8Team1.name if num == 0 else Elite8Team2.name

                  #bracket['Final 4 Winner ' + str(e+1)] = Elite8Team1.name if marMadCalc.calcWinner(
                  #        marMadData.final_4_seed_hist_win_pct.get(Elite8Team1.seed), 
                  #        marMadData.final_4_seed_hist_win_pct.get(Elite8Team2.seed)
                   #       ) == 1 else Elite8Team2.name
                  i = i + 2
                  

              #Championship
              Final4Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Final 4 Winner 1'])
              Final4Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Final 4 Winner 2'])
              
              num = marMadCalc.calcWinner(
                      marMadData.champ_seed_hist_win_pct.get(Final4Team1.seed),
                      marMadData.champ_seed_hist_win_pct.get(Final4Team2.seed),
                      Final4Team1.netRanking,
                      Final4Team2.netRanking,
                      Final4Team1.rpi,
                      Final4Team2.rpi)
              bracket['Championship Winner'] = Final4Team1.name if num == 0 else Final4Team2.name

              #bracket['Championship Winner'] =  Final4Team1.name if marMadCalc.calcWinner(
                #          marMadData.champ_seed_hist_win_pct.get(Final4Team1.seed), 
                #          marMadData.champ_seed_hist_win_pct.get(Final4Team2.seed)
                  #        ) == 1 else Final4Team2.name
              
            # writer.writerow([bracket])
              writer.writerow(bracket)
