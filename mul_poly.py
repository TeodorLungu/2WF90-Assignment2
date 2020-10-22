### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from variousFunctions import isPrime
from display_poly import display_poly
from variousFunctions import reduction

def mul_poly(mod,f,g):
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    mArray = [0 for i in range(lengthf+lengthg-1)] #Create an empty polynomial
    for i in range(lengthf):
        for j in range(lengthg):
            mArray[i+j]+=f[i]*g[j] #Multiply each corresponding element
            mArray[i+j]=reduction(mArray[i+j],mod) #Reduce each calculated product
    return display_poly(mod,mArray)[0], mArray                 

#print(mul_poly(2,[1,3,4],[1,3,4,1,4,6]))