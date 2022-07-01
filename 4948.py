# BOJ 4948 Bertrand's postulate 베르트랑 공준

# thm: for all N, there exists prime between N, 2N
# Objective : to count the number of primes x with N<x<=2N

import sys

def f(x):
    if x == 1:
        return 1 

    count = 0
    for i in range(x+1, 2*x+1):

        prime_test = False
        
        for j in range(2, int(i**(0.5)) +1): #if composite number, it must have a factor in this very range
            if i % j == 0:
                prime_test = True

        if prime_test == True:
            count = count + 1 

    return count


while True:
    N = int(sys.stdin.readline().rstrip()) 
    if N == 0:
        break
    print(f(N))
