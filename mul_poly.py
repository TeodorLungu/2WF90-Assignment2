from variousFunctions import isPrime
from display_poly import display_poly
from variousFunctions import reduction

def mul_poly(mod,f,g):
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    mArray = [0 for i in range(lengthf+lengthg-1)]
    for i in range(lengthf):
        for j in range(lengthg):
            mArray[i+j]+=f[i]*g[j]
            mArray[i+j]=reduction(mArray[i+j],mod)
    return display_poly(mod,mArray)[0], mArray                 

mul_poly(7,[1,1,1],[1,-1])