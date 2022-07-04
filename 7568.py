# BOJ 7568 덩치 

# 등수 = 자신보다 큰 덩치 사람 수

import sys

N = int(sys.stdin.readline().rstrip())
storage = [[0,0] for _ in range(N)]

for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    storage[i][0] = x
    storage[i][1] = y

for i in range(N): # for each row, we will print its rank!
    num = 1 
    self_x = storage[i][0]
    self_y = storage[i][1]

    for j in range(N): # visit all the rows and count if the row is 'bigger' than the pivot row
        if storage[j][0] > self_x and storage[j][1] > self_y:
            num = num + 1 
    
    print(num)