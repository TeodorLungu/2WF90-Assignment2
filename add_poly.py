### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from variousFunctions import isPrime
from display_poly import display_poly
from variousFunctions import reduction

def add_poly(mod,f,g):
    s = "" #The final result will be stored in string s
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    maximum = max(lengthf,lengthg)
    sArray = [0 for i in range(maximum)]

    #If f has higher degree
    if (lengthf == maximum):
        j=lengthf-1
        #Copy the polynomial with higher degree in the result list
        for i in range(lengthf):
            sArray[i]=f[i]
            reduction(sArray[i],mod)
    
        #Add each corresponding elements
        for i in range(lengthg-1,-1,-1):
            sArray[j]+=g[i]
            j=j-1
            reduction(sArray[i],mod)

    #If g has higher degree
    if (lengthg==maximum):
        j=lengthg-1
        #Copy the polynomial with higher degree in the result list
        for i in range(lengthg):
            sArray[i]=g[i]
            reduction(sArray[i],mod)

        #Add each corresponding elements
        for i in range(lengthf-1,-1,-1):
            sArray[j]+=f[i]
            j=j-1 
            reduction(sArray[i],mod)
    return display_poly(mod,sArray)[0], sArray  
   
#(add_poly(7,[5,2,3],[2,3,4,0]))    