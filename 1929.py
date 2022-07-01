# BOJ 1929 소수구하기 
# M 이상 N 이하의 소수 모두 출력 

import sys 

M, N = list(map(int,sys.stdin.readline().split()))

for i in range(M, N+1):
    if i == 1:
        continue
    
    for j in range(2, int(i**0.5)+1):  # for-else statement!! 
        if i%j == 0:
            break
    else:   # else is executed when for-loop is not interrupted
        print(i) 


