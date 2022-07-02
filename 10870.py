# BOJ 10870 Fibonacci Number

import sys

N = int(sys.stdin.readline().rstrip())

nums = [0] * (N+1)  # numbers storage space 

def f(x): #fibonacci function -> updates the nums list -> returns number.
    if x < 2: # when n = 0, 1
        nums[x] = x
        return x

    if nums[x] != 0:
        return nums[x]
    
    else: # if nums[x] == 0, change it, then return the (x)th number
        nums[x] = f(x-1) + f(x-2)
        return nums[x]

print(f(N))