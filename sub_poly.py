from variousFunctions import isPrime
from display_poly import display_poly
from variousFunctions import reduction

def sub_poly(mod,f,g):
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    maximum = max(lengthf,lengthg)
    sArray = [0 for i in range(maximum)]
    if (lengthf == maximum):
        while (lengthg<maximum):
            g.insert(0,0)
            lengthg=len(g)
    if (lengthg == maximum):
        while (lengthf<maximum):
            f.insert(0,0)
            lengthf=len(f)        
    j=lengthf-1
    for i in range(lengthf):
        sArray[i]=f[i]
        reduction(sArray[i],mod)
    for i in range(lengthg-1,-1,-1):
        sArray[j]-=g[i]
        j=j-1
        reduction(sArray[i],mod)
    return display_poly(mod,sArray)[0], sArray
   
sub_poly(7,[1,2,3],[2,3,4,0])        