# BOJ 2447 별 찍기 Patterns  

import sys
import math

N = int(sys.stdin.readline().rstrip())
   
main_array = [["*","*","*"],["*"," ","*"],["*","*","*"]]

for i in range(round(math.log(N//3,3))):
    sub_array = main_array  # main array is a sub array of the next step
    main_array = []
    block_r1 = []
    block_r2 = []
    block_r3 = []
    
    #1st Block Row
    for row in sub_array:
        new_row = []
        for _ in range(3): # make a long row
            new_row += row 
        block_r1.append(new_row)

    #2nd Block Row
    for row in sub_array:
        new_row = row + [" "*(3**(i+1))] + row
        block_r2.append(new_row)

    #3rd Block Row
    block_r3 = block_r1

    # Main array (list of rows) = 1st + 2nd + 3rd block rows
    main_array = block_r1 + block_r2 + block_r3

for row in main_array:
    print("".join(row))