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

              #look into f string python (dynamically pass in f string)
              #look into using pandas

              for a in range(32):
                  bracket['Round 1 Winner ' + str(a+1)] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                      marMadData.round_1_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                      marMadData.round_1_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
                  i = i + 2
                  
              i = 1
        
              #Second Round
              for b in range(16):
                  
                  #look into filter(lambda s: s.seed == bracket['Round 1 Winner '+str(b+1)], marchMadnessData.teamList)

                  #bracket['Round 2 Winner ' + str(b+1)] = bracket['Round 1 Winner '+str(b+1)] if marMadCalc.calcWinner(
                  #       marMadData.round_2_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                  #       marMadData.round_2_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)
                    #     ) == 1 else marMadData.teamList[i+1].name
                  
                  #marMadData.round_2_seed_hist_win_pct.get(getattr(marMadData.teamList,bracket['Round 1 Winner '+str(b+1)])marMadData.teamList[i].seed),
                  

                  #attrs = [o.attr for o in objs]

                  #need to do i = 1 between first and second round
                  #Round1Team1 = filter(lambda o: o.name == bracket['Round 1 Winner '+str(i)], marMadData.teamList)
                # Round1Team2 = filter(lambda o: o.name == bracket['Round 1 Winner '+str(i+1)], marMadData.teamList)
                # Round1Team1.__getattribute__
                # bracket['Round 2 Winner ' + str(b+1)] = Round1Team1.name if marMadCalc.calcWinner(
                  #        marMadData.round_2_seed_hist_win_pct.get(Round1Team1.seed), 
                  #        marMadData.round_2_seed_hist_win_pct.get(Round1Team2.seed)
                  #       ) == 1 else Round1Team2.name 
                  
                  
                  Round1Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 1 Winner '+str(i)])
                  Round1Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 1 Winner '+str(i+1)])

                  bracket['Round 2 Winner ' + str(b+1)] = Round1Team1.name if marMadCalc.calcWinner(
                          marMadData.round_2_seed_hist_win_pct.get(Round1Team1.seed), 
                          marMadData.round_2_seed_hist_win_pct.get(Round1Team2.seed)
                          ) == 1 else Round1Team2.name
                  
                  i = i + 2

              i = 1
          
              #Sweet 16
              for c in range(8):

                  Round2Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 2 Winner '+str(i)])
                  Round2Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Round 2 Winner '+str(i+1)])

                  bracket['Sweet 16 Winner ' + str(c+1)] = Round2Team1.name if marMadCalc.calcWinner(
                          marMadData.sweet_16_seed_hist_win_pct.get(Round2Team1.seed), 
                          marMadData.sweet_16_seed_hist_win_pct.get(Round2Team2.seed)
                          ) == 1 else Round2Team2.name 

                # bracket['Sweet 16 Winner ' + str(c)] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                    #      marMadData.sweet_16_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                      #    marMadData.sweet_16_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
                  i = i + 2

              i = 1

              #Elite 8
              for d in range(4):

                  Sweet16Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Sweet 16 Winner '+str(i)])
                  Sweet16Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Sweet 16 Winner '+str(i+1)])

                  bracket['Elite 8 Winner ' + str(d+1)] = Sweet16Team1.name if marMadCalc.calcWinner(
                          marMadData.elite_8_seed_hist_win_pct.get(Sweet16Team1.seed), 
                          marMadData.elite_8_seed_hist_win_pct.get(Sweet16Team2.seed)
                          ) == 1 else Sweet16Team2.name

                  #bracket['Elite 8 Winner ' + str(d)] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                    #      marMadData.elite_8_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                    #      marMadData.elite_8_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name

                  i = i + 2

              i = 1

              #Final Four
              for e in range(2):
                  Elite8Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Elite 8 Winner '+str(i)])
                  Elite8Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Elite 8 Winner '+str(i+1)])

                  bracket['Final 4 Winner ' + str(e+1)] = Elite8Team1.name if marMadCalc.calcWinner(
                          marMadData.final_4_seed_hist_win_pct.get(Elite8Team1.seed), 
                          marMadData.final_4_seed_hist_win_pct.get(Elite8Team2.seed)
                          ) == 1 else Elite8Team2.name
                  
              #Final Four
              #bracket['Final Four Winner 1'] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                #  marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                # marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
              
              #bracket['Final Four Winner 2'] = marMadData.teamList[i].name if marMadCalc.calcWinner(
                #  marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i].seed), 
                # marMadData.final_4_seed_hist_win_pct.get(marMadData.teamList[i+1].seed)) == 1 else marMadData.teamList[i+1].name
              
            # bracket['Championship Winner'] = marMadData.teamList

              #Championship
              Final4Team1 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Final 4 Winner 1'])
              Final4Team2 = marMadData.find_object_by_attribute(marMadData.teamList, "name", bracket['Final 4 Winner 2'])

              bracket['Championship Winner'] =  Final4Team1.name if marMadCalc.calcWinner(
                          marMadData.champ_seed_hist_win_pct.get(Final4Team1.seed), 
                          marMadData.champ_seed_hist_win_pct.get(Final4Team2.seed)
                          ) == 1 else Final4Team2.name
              
            # writer.writerow([bracket])
              writer.writerow(bracket)
