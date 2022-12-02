opp_dict = {'A':1, 'B':2, 'C':3}
player_dict = {'X':1, 'Y':2, 'Z':3}
outcomes_part1 = {'AX':4, 'AY':8, 'AZ':3, 'BX':1, 'BY':5, 'BZ':9, 'CX':7, 'CY':2, 'CZ':6}
outcomes_part2 = {'AX':3, 'AY':4, 'AZ':9, 'BX':1, 'BY':5, 'BZ':9, 'CX':2, 'CY':5, 'CZ':7} # X - lose (0), Y = draw (3), Z = win (6) : R -> S -> P -> R...

with open("input.txt", "r") as f:
    count = 0

    opp_val = 0
    opp_choice = ''

    player_val = 0
    player_choice = ''

    calc_outcome = 0
    total_p1 = 0
    total_p2 = 0

    for line in f:
        opp_choice = line[0]
        player_choice = line[2]

        calc_outcome = opp_choice + player_choice
        
        print(calc_outcome)
        for i in outcomes_part1:
            if calc_outcome == i:
                total_p1 += outcomes_part1[i]
        
        for j in outcomes_part2:
            if calc_outcome == j:
                total_p2 += outcomes_part2[j]

    print("Part 1:", total_p1)
    print("Part 2:", total_p2) # Not giving correct answer!!!

    # One liner
    print(*map(sum,zip(*[(b-87+3*((b-a-67)%3),1+(b-88)*3+(a+b-151)%3)for l in open('input.txt').readlines()if(a:=ord(l[0]),b:=ord(l[2]))])))

    '''
    RX - L  3
    RY - D  4
    RZ - W  9
    PX - L  1
    PY - D  5
    PZ - W  9
    SX - L  2
    SY - D  5
    SZ - W  7
    '''