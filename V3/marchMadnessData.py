import team

# Generate the brackets
num_brackets = 150000

# Define the format of the CSV file
headers = ['Bracket Number','Round 1 Winner 1', 'Round 1 Winner 2', 'Round 1 Winner 3', 'Round 1 Winner 4', 'Round 1 Winner 5', 'Round 1 Winner 6', 'Round 1 Winner 7', 
        'Round 1 Winner 8', 'Round 1 Winner 9', 'Round 1 Winner 10','Round 1 Winner 11', 'Round 1 Winner 12', 'Round 1 Winner 13', 'Round 1 Winner 14', 'Round 1 Winner 15',
        'Round 1 Winner 16', 'Round 1 Winner 17', 'Round 1 Winner 18', 'Round 1 Winner 19', 'Round 1 Winner 20', 'Round 1 Winner 21', 'Round 1 Winner 22', 'Round 1 Winner 23',
        'Round 1 Winner 24', 'Round 1 Winner 25', 'Round 1 Winner 26', 'Round 1 Winner 27', 'Round 1 Winner 28', 'Round 1 Winner 29', 'Round 1 Winner 30', 'Round 1 Winner 31','Round 1 Winner 32', 
        'Round 2 Winner 1', 'Round 2 Winner 2', 'Round 2 Winner 3', 'Round 2 Winner 4', 'Round 2 Winner 5', 'Round 2 Winner 6', 'Round 2 Winner 7',
        'Round 2 Winner 8', 'Round 2 Winner 9', 'Round 2 Winner 10', 'Round 2 Winner 11', 'Round 2 Winner 12', 'Round 2 Winner 13', 'Round 2 Winner 14', 'Round 2 Winner 15','Round 2 Winner 16',
        'Sweet 16 Winner 1', 'Sweet 16 Winner 2', 'Sweet 16 Winner 3', 'Sweet 16 Winner 4', 'Sweet 16 Winner 5', 'Sweet 16 Winner 6', 'Sweet 16 Winner 7', 'Sweet 16 Winner 8',
        'Elite 8 Winner 1', 'Elite 8 Winner 2', 'Elite 8 Winner 3', 'Elite 8 Winner 4', 
        'Final 4 Winner 1', 'Final 4 Winner 2',
        'Championship Winner']

teamList = []

teams = {
        'Team 1': 'Duke',
        'Team 2': 'Siena.',
        'Team 3': 'Ohio St.',
        'Team 4': 'TCU',
        'Team 5': 'St. John\'s',
        'Team 6': 'Northern Iowa',
        'Team 7': 'Kansas',
        'Team 8': 'Cal Baptist',
        'Team 9': 'Louisville',
        'Team 10': 'South Florida',
        'Team 11': 'Michigan St.',
        'Team 12': 'North Dakota St.',
        'Team 13': 'UCLA',
        'Team 14': 'UCF',
        'Team 15': 'UConn',
        'Team 16': 'Furman',
        'Team 17': 'Florida',
        'Team 18': 'Prairie View A&M',
        'Team 19': 'Clemson',
        'Team 20': 'Iowa',
        'Team 21': 'Vanderbilt',
        'Team 22': 'Mcneese',
        'Team 23': 'Nebraska',
        'Team 24': 'Troy',
        'Team 25': 'North Carolina',
        'Team 26': 'VCU',
        'Team 27': 'Illinois',
        'Team 28': 'Penn',
        'Team 29': 'Saint Mary\'s',
        'Team 30': 'Texas A&M',
        'Team 31': 'Houston',
        'Team 32': 'Idaho',
        'Team 33': 'Arizona',
        'Team 34': 'Long Island',
        'Team 35': 'Villanova',
        'Team 36': 'Utah St.',
        'Team 37': 'Wisconsin',
        'Team 38': 'High Point',
        'Team 39': 'Arkansas',
        'Team 40': 'Hawaii',
        'Team 41': 'BYU',
        'Team 42': 'Texas',
        'Team 43': 'Gonzaga',
        'Team 44': 'Kennesaw St.',
        'Team 45': 'Miami (FL)',
        'Team 46': 'Missouri',
        'Team 47': 'Purdue',
        'Team 48': 'Queens (N.C.)',
        'Team 49': 'Michigan',
        'Team 50': 'Howard',
        'Team 51': 'Georgia',
        'Team 52': 'Saint Louis',
        'Team 53': 'Texas Tech',
        'Team 54': 'Akron',
        'Team 55': 'Alabama',
        'Team 56': 'Hofstra',
        'Team 57': 'Tennessee',
        'Team 58': 'Miami (Ohio)',
        'Team 59': 'Virginia',
        'Team 60': 'Wright St.',
        'Team 61': 'Kentucky',
        'Team 62': 'Santa Clara',
        'Team 63': 'Iowa St.',
        'Team 64': 'Tennessee St.',
    }
 
bracket_data = {
    'Bracket Number' : '',
    'Round 1 Winner 1': '',
    'Round 1 Winner 2': '',
    'Round 1 Winner 3': '',
    'Round 1 Winner 4': '',
    'Round 1 Winner 5': '',
    'Round 1 Winner 6': '',
    'Round 1 Winner 7': '',
    'Round 1 Winner 8': '',
    'Round 1 Winner 9': '',
    'Round 1 Winner 10': '',
    'Round 1 Winner 11': '',
    'Round 1 Winner 12': '',
    'Round 1 Winner 13': '',
    'Round 1 Winner 14': '',
    'Round 1 Winner 15': '',
    'Round 1 Winner 16': '',
    'Round 1 Winner 17': '',
    'Round 1 Winner 18': '',
    'Round 1 Winner 19': '',
    'Round 1 Winner 20': '',
    'Round 1 Winner 21': '',
    'Round 1 Winner 22': '',
    'Round 1 Winner 23': '',
    'Round 1 Winner 24': '',
    'Round 1 Winner 25': '',
    'Round 1 Winner 26': '',
    'Round 1 Winner 27': '',
    'Round 1 Winner 28': '',
    'Round 1 Winner 29': '',
    'Round 1 Winner 30': '',
    'Round 1 Winner 31': '',
    'Round 1 Winner 32': '',
    'Round 2 Winner 1': '',
    'Round 2 Winner 2': '',
    'Round 2 Winner 3': '',
    'Round 2 Winner 4': '',
    'Round 2 Winner 5': '',
    'Round 2 Winner 6': '',
    'Round 2 Winner 7': '',
    'Round 2 Winner 8': '',
    'Round 2 Winner 9': '',
    'Round 2 Winner 10': '',
    'Round 2 Winner 11': '',
    'Round 2 Winner 12': '',
    'Round 2 Winner 13': '',
    'Round 2 Winner 14': '',
    'Round 2 Winner 15': '',
    'Round 2 Winner 16': '',
    'Sweet 16 Winner 1': '',
    'Sweet 16 Winner 2': '',
    'Sweet 16 Winner 3': '',
    'Sweet 16 Winner 4': '',
    'Sweet 16 Winner 5': '',
    'Sweet 16 Winner 6': '',
    'Sweet 16 Winner 7': '',
    'Sweet 16 Winner 8': '',
    'Elite 8 Winner 1': '',
    'Elite 8 Winner 2': '',
    'Elite 8 Winner 3': '',
    'Elite 8 Winner 4': '',
    'Final 4 Winner 1': '',
    'Final 4 Winner 2': '',
    'Championship Winner': '',
}

#All these percentages are for the year 2021-2025
round_1_seed_hist_win_pct = {
    1:.95,
    2:.85,
    3:.9,
    4:.8,
    5:.65,
    6:.5,
    7:.65,
    8:.45,
    9:.55,
    10:.35,
    11:.5,
    12:.35,
    13:.2,
    14:.1,
    15:.15,
    16:.05
}

round_2_seed_hist_win_pct = {
    1:.83,
    2:.75,
    3:.55,
    4:.66,
    5:.63,
    6:.5,
    7:.16,
    8:.36,
    9:.1,
    10:.3,
    11:.4,
    12:.2,
    13:0,
    14:0,
    15:.6,
    16:0
}

sweet_16_seed_hist_win_pct = {
    1:.56,
    2:.41,
    3:.33,
    4:.36,
    5:.4,
    6:.6,
    7:0,
    8:.2,
    9:.2,
    10:.2,
    11:.3,
    12:.2,
    13:0,
    14:0,
    15:.2,
    16:0
}

elite_8_seed_hist_win_pct = {
    1:.73,
    2:.2,
    3:0,
    4:.3,
    5:.2,
    6:0,
    7:0,
    8:.2,
    9:.2,
    10:0,
    11:.4,
    12:0,
    13:0,
    14:0,
    15:0,
    16:0
}

final_4_seed_hist_win_pct = {
    1:.7,
    2:0,
    3:0,
    4:.2,
    5:.1,
    6:0,
    7:0,
    8:.2,
    9:0,
    10:0,
    11:0,
    12:0,
    13:0,
    14:0,
    15:0,
    16:0
}

champ_seed_hist_win_pct = {
    1:.6,
    2:0,
    3:0,
    4:.2,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0,
    13:0,
    14:0,
    15:0,
    16:0
}

seedOrder = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]

#this list is supposed to "correlate to teams 1-64 (i had to adjust their rankings to fit within 1-64)"

netRankingList = [0.984375
                ,0.078125
                ,0.546875
                ,0.4375
                ,0.75
                ,0.265625
                ,0.671875
                ,0.21875
                ,0.734375
                ,0.359375
                ,0.828125
                ,0.1875
                ,0.53125
                ,0.34375
                ,0.84375
                ,0.0625
                ,0.9375
                ,0
                ,0.46875
                ,0.578125
                ,0.796875
                ,0.3125
                ,0.78125
                ,0.171875
                ,0.625
                ,0.390625
                ,0.875
                ,0.140625
                ,0.65625
                ,0.375
                ,0.921875
                ,0.125
                ,0.953125
                ,0.03125
                ,0.453125
                ,0.59375
                ,0.609375
                ,0.25
                ,0.765625
                ,0.203125
                ,0.640625
                ,0.40625
                ,0.890625
                ,0.109375
                ,0.5
                ,0.296875
                ,0.859375
                ,0.046875
                ,0.96875
                ,0.015625
                ,0.484375
                ,0.515625
                ,0.703125
                ,0.328125
                ,0.71875
                ,0.234375
                ,0.6875
                ,0.28125
                ,0.8125
                ,0.15625
                ,0.5625
                ,0.421875
                ,0.90625
                ,0.09375]

#this list is supposed to correlate to teams 1-64
rpiList = [0.689
          ,0.523
          ,0.584
          ,0.566
          ,0.63
          ,0.549
          ,0.635
          ,0.56
          ,0.605
          ,0.601
          ,0.633
          ,0.535
          ,0.587
          ,0.585
          ,0.641
          ,0.513
          ,0.64
          ,0.442
          ,0.589
          ,0.564
          ,0.626
          ,0.59
          ,0.614
          ,0.547
          ,0.634
          ,0.612
          ,0.618
          ,0.546
          ,0.627
          ,0.553
          ,0.641
          ,0.488
          ,0.682
          ,0.509
          ,0.602
          ,0.632
          ,0.599
          ,0.553
          ,0.638
          ,0.531
          ,0.608
          ,0.544
          ,0.633
          ,0.519
          ,0.578
          ,0.555
          ,0.631
          ,0.514
          ,0.683
          ,0.483
          ,0.571
          ,0.609
          ,0.627
          ,0.596
          ,0.625
          ,0.57
          ,0.591
          ,0.595
          ,0.633
          ,0.524
          ,0.588
          ,0.61
          ,0.623
          ,0.534]

def generateTeamList():
    seedCounter = 0
    counter = 0
    for key, value in teams.items():
        
        teamList.append(team.team(key, value,seedOrder[seedCounter], netRankingList[counter], rpiList[counter]))

        if seedCounter == 15:
            seedCounter = 0
        else:
            seedCounter += 1

        counter += 1

def find_object_by_attribute(objects, attribute, value):
    for obj in objects:
        if getattr(obj, attribute, None) == value:
            return obj
    return None


    