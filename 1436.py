# BOJ 1436 

import sys

N = int(sys.stdin.readline().rstrip())

def f(N):
    num = 666
    count = 0

    while True:
        if "666" in str(num): 
            count = count + 1
        if count == N:
            return num
        num = num + 1

print(f(N))