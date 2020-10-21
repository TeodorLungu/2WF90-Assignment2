from inverseField import inverseField
from mul_field import mul_field
from variousFunctions import isPrime


def div_field(mod,f,a,b):
    if isPrime(mod)==False:
        return "ERROR"
    if b==[0]:
        return "ERROR"    
    multINV=inverseField(mod,f,b)[1] #Find the inverse
    if (multINV=='ERROR'): #If there is not an inverse then return error
        return 'ERROR'
    else:  
        return mul_field(mod,f,a,multINV) #Else multiply by the inverse, hence dividing by the polynomial
    
#print(div_field(2,[1,0,1,1],[1,0],[1,1,1]))    
#print(div_field(5,[1,0,2],[1,0,0],[3]))