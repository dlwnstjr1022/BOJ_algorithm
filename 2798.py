# BOJ 2798 BlackJack

import sys

N,M = list(map(int,sys.stdin.readline().split()))
card_list = list(map(int,sys.stdin.readline().split())) 

res = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = card_list[i] + card_list[j] + card_list[k]
            if sum > res and sum <= M:
                res = sum

print(res)
