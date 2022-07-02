# BOJ 9020 Goldbach's conjecture

import sys

#  multiple partitions? choose partition for which the differnce is minimized
# N is even, N = p+q => p,q must be odd (except for (2,2))

def f(x):
    odd_list = [i for i in range( (x)//2 -  int(((x)//2)%2==0) ,0,-2)]

    if x == 4:  # the only case where p,q are even 
        return "2 2" 

    for i in odd_list:    # just need to check for odd numbers, if i, x-i makes a prime pair
        prime_pair = True
        for j in range(2, int((x-i)**0.5)+1): # need to test up to possible factors of the larger one (ie. x-i > x)
            if (i % j == 0) or ((x-i) % j == 0):
                prime_pair = False
                break

        if prime_pair == True:
            return str(i) +" "+ str(x-i)

n = int(sys.stdin.readline().rstrip())  

for i in range(n):
    N = int(sys.stdin.readline().rstrip())

    print(f(N))

# Time cost could've been reduced by storing prime numbers in a list
# since we repeatedly check if a same number is prime or not.  