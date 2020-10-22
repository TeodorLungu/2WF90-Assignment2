### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from variousFunctions import isPrime
from display_poly import display_poly
from variousFunctions import reduction

def sub_poly(mod,f,g):
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    maximum = max(lengthf,lengthg)
    sArray = [0 for i in range(maximum)] #Construct an empty polynomial of size maximum

    #Add leading zeros to the polynomial that has a smaller degree
    if (lengthf == maximum):
        while (lengthg<maximum):
            g.insert(0,0)
            lengthg=len(g)
    if (lengthg == maximum):
        while (lengthf<maximum):
            f.insert(0,0)
            lengthf=len(f)        

    #Put the polynomial with a higher degree in f
    j= lengthf - 1
    for i in range(lengthf):
        sArray[i]=f[i]
        reduction(sArray[i],mod)
    
    #Subtract each corrsponding coefficients
    for i in range(lengthg-1,-1,-1):
        sArray[j] -= g[i]
        j= j - 1
        reduction(sArray[i],mod)

    return display_poly(mod,sArray)[0], sArray
   
#print(sub_poly(7,[1,2,3],[2,3,4,0]))   