from div_field import div_field
from variousFunctions import isPrime


def equals_field(mod,f,a,b):
    if isPrime(mod)==False:
        return False
    if (div_field(mod,f,a,b)[1]==[1]): 
        #If the result of the division is 1 then output true else false
        return True
    else:
        return False    
