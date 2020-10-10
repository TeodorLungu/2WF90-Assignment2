from isPrime import isPrime
from display_poly import display_poly
from isPrime import reduction

def add_poly(mod,f,g):
    if (isPrime(mod)==False):
        return "p is not prime"
    s = "" #The final result will be stored in string s
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    maximum = max(lengthf,lengthg)
    sArray = [0 for i in range(maximum)]
    if (lengthf == maximum):
        j=lengthf-1
        for i in range(lengthf):
            sArray[i]=f[i]
            reduction(sArray[i],mod)
        for i in range(lengthg-1,-1,-1):
            sArray[j]+=g[i]
            j=j-1
            reduction(sArray[i],mod)
    if (lengthg==maximum):
        j=lengthg-1
        for i in range(lengthg):
            sArray[i]=g[i]
            reduction(sArray[i],mod)
        for i in range(lengthf-1,-1,-1):
            sArray[j]+=f[i]
            j=j-1 
            reduction(sArray[i],mod)
    display_poly(sArray,mod)
    print(sArray)    
   
add_poly(7,[5,2,3],[2,3,4,0])        