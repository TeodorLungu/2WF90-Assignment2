### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
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
