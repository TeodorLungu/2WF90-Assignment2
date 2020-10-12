from variousFunctions import deg
from extended_eulclid import extended_euclid
from longdivision import long_div_poly

def irreducible(mod,f):
    #t←1
    #while gcd(f,X^mod^t −X)=1 do t←t+1
    #if t = n then output ‘true’ else output ‘false’
    t = 1
    n = deg(f)
    test = [0 for i in range(pow(mod,t)+1)]
    test[-2]=-1  
    test[0]=1
    test = long_div_poly(mod,test,f)[3]  
    while (extended_euclid(mod,f,test)[0]=='1'):
        t = t+1
        test = [0 for i in range(pow(mod,t)+1)]
        test[-2]=-1  
        test[0]=1 
        test = long_div_poly(mod,test,f)[3]  
    if (t==n):
        return True
    else:
        return False   

print(irreducible(2,[1,0,0,0,0,0,0,0,0,1,0,1]))   