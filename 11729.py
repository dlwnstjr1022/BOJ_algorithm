# BOJ 11729 Hanoi Tower

from itertools import count
import sys

N = int(sys.stdin.readline().rstrip())

# N plates at first pillar
# want to move to the third pillar
# pillars - {origin} {empty} {target}
# 1. Let N-1 plates be at the {empty}
# 2. Move the N th plate to the {target}
# 3. Move the N-1 plates on the {target}
# def f(N) to be f(N-1)

global count
count = 0

def f(N,j,k): # N plates stacked up at jth pillar, to be moved to kth pillar
    global count
    if N == 1:
        print(f"{j} {k}")
        count += 1
        return

    else:
        f(N-1,j,6-j-k)
        print(f"{j} {k}")
        count += 1
        return f(N-1,6-j-k,k)


print(2**N-1)
f(N,1,3)