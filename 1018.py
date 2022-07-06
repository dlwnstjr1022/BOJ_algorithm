# 1018 Chessboard

import sys

M, N = map(int,(sys.stdin.readline().split()))

encode = {'B' : 1, 'W' : -1} # encode B, 
decode = { 1 : 'B' , -1 : 'W'}
array = []

for i in range(M):
    array.append(list(encode[j] for j in sys.stdin.readline().rstrip()))

min_count = 64
for i in range(M-7):
    for j in range(N-7):
        pivots = [1,-1]  

        for pivot in pivots: # need to check for both cases!! - pivot being B / W 
            count = 0
            for k in range(8):  # constructing 8x8 chessborad and check for each values
                for l in range(8):
                    if (k+l) % 2 == 0 and array[i+k][j+l] != pivot:
                        count += 1
                    if (k+l) % 2 == 1 and array[i+k][j+l] != -1*pivot:
                        count += 1

            if count < min_count:
                min_count = count
        
            # print(f"pivot[{decode[pivot]}] : ({i},{j}) / count = {count}")  # for Debugging
        

print(min_count)