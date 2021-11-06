import csv, random


# Read CSV
def readCharacters():
    file = csv.reader(open('characters.csv'))
    fields = next(file)
    final_list = []
    for i in file:
        final_list.append(i)
    return final_list


# Generate Character 1
def genChar1():
    while True:
        num = random.randrange(0, 55)
        # Roll will never get picked
        if num != 35:
            break
    return num


# Generate Character 2
def genChar2(chlist, id1, p1):
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
def genChar3(chlist, id1, p1, id2, p2):
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
def genTeam():
    # Get list of all characters and their associated data
    all_characters = readCharacters()    
    # Get first character
    first = genChar1()
    ch1 = all_characters[first]
    ch1_name = ch1[1]
    ch1_point = ch1[2]
    ch1_assist = ch1[random.randrange(0,2) + 3]
    print('%s, %s Type (%s)' % (ch1_name, ch1_assist, ch1_point))
    # Get second character
    second = genChar2(all_characters,
                      int(first),
                      int(ch1_point))
    ch2 = all_characters[second]
    ch2_name = ch2[1]
    ch2_point = ch2[2]
    ch2_assist = ch2[random.randrange(0,2) + 3]
    print('%s, %s Type (%s)' % (ch2_name, ch2_assist, ch2_point))
    # Get third character
    third = genChar3(all_characters,
                     int(first),
                     int(ch1_point),
                     int(second),
                     int(ch2_point))
    ch3 = all_characters[third]
    ch3_name = ch3[1]
    ch3_point = ch3[2]
    ch3_assist = ch3[random.randrange(0,2) + 3]
    print('%s, %s Type (%s)' % (ch3_name, ch3_assist, ch3_point))


# Print character data
def printChData(character, assist):
    print('ID: %s' % character[0])
    print('NAME: %s' % character[1])
    print('POINTS: %s' % character[2])
    print('ASSIST: %s' % assist)
    return
    

def dev01():
    print(random.randrange(1,1))


genTeam()
#dev01()







