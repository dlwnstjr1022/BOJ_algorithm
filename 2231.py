import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N+1):
    L = list(map(int,[j for j in str(i)]))
    res = i + sum(L)
    if res == N:
        print(i)
        break
else:
    print(0)