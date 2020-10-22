### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from variousFunctions import deg
from extended_euclid import extended_euclid
from longdivision import long_div_poly
from variousFunctions import isPrime

def irreducible(mod,f):
    if (isPrime(mod)==False or f==[0]): #Check if division by 0 is wanted or if the modulo is prime
        return False
    t = 1
    n = deg(f)
    test = [0 for i in range(pow(mod,t)+1)] #Create empty polynomial
    test[-2]=-1
    test[0]=1
    test = long_div_poly(mod,test,f)[3]  

    #Direct implementation of algorithm 5.1.4
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

#print(irreducible(2,[1,0,1]))   