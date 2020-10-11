from longdivision import long_div_poly
from longdivision import mul_poly
from longdivision import sub_poly
from longdivision import mod_inverse
from longdivision import lc
from longdivision import display_poly
from longdivision import reduction
from longdivision import add_poly
from longdivision import deg
from longdivision import elim_lead_zeros
from extended_eulclid import extended_euclid
from longdivision import deg

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
        print(t)
        test = [0 for i in range(pow(mod,t)+1)]
        test[-2]=-1  
        test[0]=1 
    if (t==n):
        return True
    else:
        return False   

print(irreducible(51,[1,-11,19,-17,1,1,1]))        