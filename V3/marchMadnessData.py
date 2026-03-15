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
        'Team 1': 'Auburn',
        'Team 2': 'Alabama St.',
        'Team 3': 'Louisville',
        'Team 4': 'Creighton',
        'Team 5': 'Michigan',
        'Team 6': 'UC San Diego',
        'Team 7': 'Texas A&M',
        'Team 8': 'Yale',
        'Team 9': 'Ole Miss',
        'Team 10': 'North Carolina',
        'Team 11': 'Iowa St.',
        'Team 12': 'Lipscomb',
        'Team 13': 'Marquette',
        'Team 14': 'New Mexico',
        'Team 15': 'Michigan St.',
        'Team 16': 'Bryant',
        'Team 17': 'Florida',
        'Team 18': 'Norfolk St.',
        'Team 19': 'Uconn',
        'Team 20': 'Oklahoma',
        'Team 21': 'Memphis',
        'Team 22': 'Colorado St.',
        'Team 23': 'Maryland',
        'Team 24': 'Grand Canyon',
        'Team 25': 'Missouri',
        'Team 26': 'Drake',
        'Team 27': 'Texas Tech',
        'Team 28': 'UNC Wilmington',
        'Team 29': 'Kansas',
        'Team 30': 'Arkansas',
        'Team 31': 'St. John\'s',
        'Team 32': 'Omaha',
        'Team 33': 'Duke',
        'Team 34': 'Mount St. Mary\'s',
        'Team 35': 'Mississippi St.',
        'Team 36': 'Baylor',
        'Team 37': 'Oregon',
        'Team 38': 'Liberty',
        'Team 39': 'Arizona',
        'Team 40': 'Akron',
        'Team 41': 'BYU',
        'Team 42': 'VCU',
        'Team 43': 'Wisconsin',
        'Team 44': 'Montana',
        'Team 45': 'St. Mary\'s',
        'Team 46': 'Vanderbilt',
        'Team 47': 'Alabama',
        'Team 48': 'Robert Morris',
        'Team 49': 'Houston',
        'Team 50': 'SIU Edwardsville',
        'Team 51': 'Gonzaga',
        'Team 52': 'Georgia',
        'Team 53': 'Clemson',
        'Team 54': 'McNeese',
        'Team 55': 'Purdue',
        'Team 56': 'High Point',
        'Team 57': 'Illinois',
        'Team 58': 'Xavier',
        'Team 59': 'Kentucky',
        'Team 60': 'Troy',
        'Team 61': 'UCLA',
        'Team 62': 'Utah St.',
        'Team 63': 'Tennessee',
        'Team 64': 'Wofford',
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

def generateTeamList():
    counter = 0
    for key, value in teams.items():
        
        teamList.append(team.team(key, value,seedOrder[counter]))

        if counter == 15:
            counter = 0
        else:
            counter += 1

def find_object_by_attribute(objects, attribute, value):
    for obj in objects:
        if getattr(obj, attribute, None) == value:
            return obj
    return None


    