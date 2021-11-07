import csv, json, random
from os import path


################################################################################
# CSV functions
# Read CSV
def read_csv():
    file = csv.reader(open('characters.csv', 'r'))
    # Remove the headers
    fields = next(file)
    final_list = []
    for i in file:
        final_list.append(i)
    return final_list


# Generate Character 1
def gen_char1():
    while True:
        num = random.randrange(0, 55)
        # Roll will never get picked
        if num != 35:
            break
    return num


# Generate Character 2
def gen_char2(chlist, id1, p1):
    while True:
        num = random.randrange(0, 55)
        # Roll will never get picked and no duping of previous character
        if num == 35 or num == id1 + 1:
            continue
        else:
            # Must be less points than difference from first and 7
            ch2p = int(chlist[num][2])
            if ch2p < 7 - p1:
                break
            else:
                continue
    return num


# Generate Character 3
def gen_char3(chlist, id1, p1, id2, p2):
    while True:
        num = random.randrange(0, 55)
        # Roll will never get picked and no duping of previous character
        if num == 35 or num == id1 + 1 or num == id2 + 1:
            continue
        else:
            # Must be less points than difference from first and 7
            ch3p = int(chlist[num][2])
            if ch3p <= 7 - p1 - p2:
                break
            else:
                continue
    return num
    
    
# Generate team
def gen_team():
    # Get list of all characters and their associated data
    all_characters = read_csv()    
    # Get first character
    first = gen_char1()
    ch1 = all_characters[first]
    ch1_name = ch1[1]
    ch1_point = ch1[2]
    ch1_assist = ch1[random.randrange(0,2) + 3]
    print('%s, %s Type (%s)' % (ch1_name, ch1_assist, ch1_point))
    # Get second character
    second = gen_char2(all_characters,
                      int(first),
                      int(ch1_point))
    ch2 = all_characters[second]
    ch2_name = ch2[1]
    ch2_point = ch2[2]
    ch2_assist = ch2[random.randrange(0,2) + 3]
    print('%s, %s Type (%s)' % (ch2_name, ch2_assist, ch2_point))
    # Get third character
    third = gen_char3(all_characters,
                     int(first),
                     int(ch1_point),
                     int(second),
                     int(ch2_point))
    ch3 = all_characters[third]
    ch3_name = ch3[1]
    ch3_point = ch3[2]
    ch3_assist = ch3[random.randrange(0,2) + 3]
    print('%s, %s Type (%s)' % (ch3_name, ch3_assist, ch3_point))



################################################################################
# JSON functions
# Remove all file contents before writing anything, but only if it exists
def rem_file(fname):
    if path.exists(fname):
        open(fname, 'w').close()
    return fname


# Convert CSV file to JSON
def convert_json():
    jname = rem_file('characters.json')
    file = read_csv()
    dlist = []
    for i in file:
        dlist.append({'id': int(i[0]),
                      'name': i[1],
                      'points': int(i[2]),
                      'assist_1': i[3],
                      'assist_2': i[4],
                      'assist_3': i[5]
                      })
    json.dump(dlist, open(jname, 'w', encoding = 'utf8'), indent = 2)  


# Generate Character 2
def gen_char2j(chlist, id1, p1):
    while True:
        num = random.randrange(0, 55)
        # Roll will never get picked and no duping of previous character
        if num == 35 or num == id1 + 1:
            continue
        else:
            # Must be less points than difference from first and 7
            ch2p = chlist[num]['points']
            if ch2p < 7 - p1:
                break
            else:
                continue
    return num


# Generate Character 3
def gen_char3j(chlist, id1, p1, id2, p2):
    while True:
        num = random.randrange(0, 55)
        # Roll will never get picked and no duping of previous character
        if num == 35 or num == id1 + 1 or num == id2 + 1:
            continue
        else:
            # Must be less points than difference from first and 7
            ch3p = chlist[num]['points']
            if ch3p <= 7 - p1 - p2:
                break
            else:
                continue
    return num
    

# Generate Team
def gen_team2():
    # Get list of all characters and their associated data
    with open('characters.json', 'r') as file:
        all_characters = json.load(file)
        file.close()
    # Get first character
    first = gen_char1()
    ch1 = all_characters[first]
    ch1_name = ch1['name']
    ch1_point = ch1['points']
    ch1_assist = ch1[random.choice(['assist_1', 'assist_2', 'assist_3'])]
    print('%s, %s Type (%s)' % (ch1_name, ch1_assist, ch1_point))
    # Get second character
    second = gen_char2j(all_characters,
                       first,
                       ch1_point)
    ch2 = all_characters[second]
    ch2_name = ch2['name']
    ch2_point = ch2['points']
    ch2_assist = ch2[random.choice(['assist_1', 'assist_2', 'assist_3'])]
    print('%s, %s Type (%s)' % (ch2_name, ch2_assist, ch2_point))
    # Get third character
    third = gen_char3j(all_characters,
                      first,
                      ch1_point,
                      second,
                      ch2_point)
    ch3 = all_characters[third]
    ch3_name = ch3['name']
    ch3_point = ch3['points']
    ch3_assist = ch3[random.choice(['assist_1', 'assist_2', 'assist_3'])]
    print('%s, %s Type (%s)' % (ch3_name, ch3_assist, ch3_point))
    
    
#gen_team()
gen_team2()
#convert_json()






