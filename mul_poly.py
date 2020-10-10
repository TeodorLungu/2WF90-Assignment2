from isPrime import isPrime
from display_poly import display_poly
from isPrime import reduction

def mul_poly(mod,f,g):
    if (isPrime(mod)==False):
        return "p is not prime"
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    mArray = [0 for i in range(lengthf+lengthg-1)]
    for i in range(lengthf):
        for j in range(lengthg):
            mArray[i+j]+=f[i]*g[j]
            mArray[i+j]=reduction(mArray[i+j],mod)
    display_poly(mArray,mod)
    print(mArray)                   

mul_poly(7,[1,1,1],[1,-1])