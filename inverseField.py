from variousFunctions import isPrime
from extended_euclid import extended_euclid

def inverseField(mod,d,a):
    if isPrime(mod)==False:
        return "ERROR"
    output = extended_euclid(mod,a,d) #Run extended euclid algorithm
    if output[3]==[1]: #If b is 1 then there is a solution hence output it else there isn't an inverse
        return output[1],output[4]
    else:
        return "ERROR"

#print(inverseField(2,[1,1,0],[1]))        