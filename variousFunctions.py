### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
import math

#Checks if a number is prime
def isPrime(p):
    if p <=1: #If the number is at most 1 then clearly it is not prime
        return False
    if p == 2: #The only even prime number is 2
        return True
    if p % 2 == 0: #If a number is even and it is not 2 then clearly it is not prime
        return False
    for i in range(3, p//2): #If a number is divisible by a number larger than 3 then it is not prime
        if p % i == 0:
            return False
    return True #If the function did not return until here then the number is prime

#Reduce a number modulo mod
def reduction(number,mod):
        if number >= mod or number < 0: #If the number is higher than mod or less than 0 it needs to be reduced
            number = number - mod * (number//mod) #General formula to reduce
        return number   

#Returns the leading coefficient of a polynomial
def lc(p):
    for i in range(len(p)):
        if(p[i] != 0):
            return p[i]
    return 0

#Returns the degree of a polynomial
def deg(p):
    for i in range(len(p)):
        if(p[i] != 0):
            return len(p)-i-1
    return 0

#Returns the inverse modulo mod of a number
#It is an implementation of algorithm 2.11 hence no further explanation is required
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

#Eliminates leading zeros from a polynomial
def elim_lead_zeros(p):
    d = deg(p)
    pPrime = [0 for i in range(d+1)] #Constructs a new polynomial without the zeros
    k = 0
    for i in range(len(p)-d-1,len(p)): 
        pPrime[k] = p[i]
        k = k + 1
    return pPrime

#Return the prime divisors of a number
def primeDivisors(n):
    prime_divisors = []
    for i in range(1,n//2 + 2): #Iterate through all the numbers smaller than n/2
        if n % i == 0 and isPrime(i):  #If one divides n and it is also prime then add it to the list
            prime_divisors.append(i)
    return prime_divisors, len(prime_divisors)

