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
        'Team 1': 'UConn',
        'Team 2': 'Stetson',
        'Team 3': 'FAU',
        'Team 4': 'Northwestern',
        'Team 5': 'San Diego St.',
        'Team 6': 'UAB',
        'Team 7': 'Auburn',
        'Team 8': 'Yale',
        'Team 9': 'BYU',
        'Team 10': 'Duquesne',
        'Team 11': 'Illinois',
        'Team 12': 'Morehead St.',
        'Team 13': 'Washington St.',
        'Team 14': 'Drake',
        'Team 15': 'Iowa St.',
        'Team 16': 'South Dakota St.',
        'Team 17': 'North Carolina',
        'Team 18': '',
        'Team 19': 'Mississippi St.',
        'Team 20': 'Michigan St.',
        'Team 21': 'Saint Mary\'s',
        'Team 22': 'Grand Canyon',
        'Team 23': 'Alabama',
        'Team 24': 'Charleston',
        'Team 25': 'Clemson',
        'Team 26': 'New Mexico',
        'Team 27': 'Baylor',
        'Team 28': 'Colgate',
        'Team 29': 'Dayton',
        'Team 30': 'Nevada',
        'Team 31': 'Arizona',
        'Team 32': 'Long Beach St.',
        'Team 33': 'Houston',
        'Team 34': 'Longwood',
        'Team 35': 'Nebraska',
        'Team 36': 'Texas A&M',
        'Team 37': 'Wisconsin',
        'Team 38': 'James Madison',
        'Team 39': 'Duke',
        'Team 40': 'Vermont',
        'Team 41': 'Texas Tech',
        'Team 42': 'NC State',
        'Team 43': 'Kentucky',
        'Team 44': 'Oakland',
        'Team 45': 'Florida',
        'Team 46': '',
        'Team 47': 'Marquette',
        'Team 48': 'Western Ky.',
        'Team 49': 'Purdue',
        'Team 50': '',
        'Team 51': 'Utah St.',
        'Team 52': 'TCU',
        'Team 53': 'Gonzaga',
        'Team 54': 'Mcneese',
        'Team 55': 'Kansas',
        'Team 56': 'Samford',
        'Team 57': 'South Carolina',
        'Team 58': 'Oregon',
        'Team 59': 'Creighton',
        'Team 60': 'Akron',
        'Team 61': 'Texas',
        'Team 62': '',
        'Team 63': 'Tennessee',
        'Team 64': 'St. Peter\'s',
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

round_1_seed_hist_win_pct = {
    1:.99,
    2:.93,
    3:.86,
    4:.79,
    5:.65,
    6:.62,
    7:.61,
    8:.49,
    9:.51,
    10:.39,
    11:.38,
    12:.35,
    13:.21,
    14:.14,
    15:.07,
    16:.01
}

round_2_seed_hist_win_pct = {
    1:.85,
    2:.67,
    3:.62,
    4:.60,
    5:.53,
    6:.47,
    7:.31,
    8:.22,
    9:.10,
    10:.41,
    11:.45,
    12:.42,
    13:.19,
    14:.09,
    15:.36,
    16:0
}

sweet_16_seed_hist_win_pct = {
    1:.79,
    2:.72,
    3:.49,
    4:.32,
    5:.23,
    6:.36,
    7:.34,
    8:.56,
    9:.63,
    10:.38,
    11:.35,
    12:.09,
    13:0,
    14:0,
    15:.25,
    16:0
}

elite_8_seed_hist_win_pct = {
    1:.59,
    2:.47,
    3:.44,
    4:.61,
    5:.75,
    6:.19,
    7:.30,
    8:.67,
    9:.40,
    10:.11,
    11:.56,
    12:0,
    13:0,
    14:0,
    15:0,
    16:0
}

final_4_seed_hist_win_pct = {
    1:.62,
    2:.41,
    3:.65,
    4:.29,
    5:.44,
    6:.67,
    7:.33,
    8:.67,
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
    1:.65,
    2:.38,
    3:.36,
    4:.50,
    5:0,
    6:.50,
    7:1,
    8:.25,
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


    