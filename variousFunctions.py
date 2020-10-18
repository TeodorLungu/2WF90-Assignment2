import math

def isPrime(p):
    if p <=1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, p//2):
        if p % i == 0:
            return False
    return True

def reduction(number,mod):
    #Reduce modulo mod if necessary
        if number >= mod or number < 0:
            number = number - mod * (number//mod)
        return number   

def lc(p):
    for i in range(len(p)):
        if(p[i] != 0):
            return p[i]
    return 0

def deg(p):
    for i in range(len(p)):
        if(p[i] != 0):
            return len(p)-i-1
    return 0

def mod_inverse(mod, a):
    aPrime = a
    mPrime = mod
    x_1 = 1
    x_2 = 0
    while mPrime > 0:
        q = int(aPrime/mPrime)
        r = aPrime - q*mPrime
        aPrime = mPrime
        mPrime = r
        x_3 = x_1 - q*x_2
        x_1 = x_2
        x_2 = x_3
    if aPrime == 1:
        return x_1
    else:
        return 0    

def elim_lead_zeros(p):
    d = deg(p)
    pPrime = [0 for i in range(d+1)]
    k = 0
    for i in range(len(p)-d-1,len(p)):
        pPrime[k] = p[i]
        k = k + 1
    return pPrime

def primeDivisors(n):
    prime_divisors = []
    for i in range(1,n//2 + 2):
        if n % i == 0 and isPrime(i):
            prime_divisors.append(i)
    return prime_divisors, len(prime_divisors)

