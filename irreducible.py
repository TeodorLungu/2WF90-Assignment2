from variousFunctions import deg
from extended_eulclid import extended_euclid

def irreducible(mod,f):
    #t←1
    #while gcd(f,X^mod^t −X)=1 do t←t+1
    #if t = n then output ‘true’ else output ‘false’
    t = 1
    n = deg(f)
    test = [0 for i in range(pow(mod,t)+1)]
    test[-2]=-1  
    test[0]=1  
    while (extended_euclid(mod,f,test)[0]=='1'):
        t = t+1
        test = [0 for i in range(pow(mod,t)+1)]
        test[-2]=-1  
        test[0]=1 
    if (t==n):
        return True
    else:
        return False   

irreducible(31,[1,-11,19,-17])     