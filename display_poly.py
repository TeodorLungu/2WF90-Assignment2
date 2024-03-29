### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from variousFunctions import elim_lead_zeros

def display_poly(mod , poly):
    s = "" #The final result will be stored in string s
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹") #Make translation table to display superscripts
    k = len(poly) #Store the power for each term

    if elim_lead_zeros(poly) == [0]:
        return "0", [0]

    for i in range(len(poly)): #Iterate through the coefficients of the polynomial starting with the leading coefficient
        k = k - 1 #Subtract 1 from the current power. If this is the first subtraction then this will be the leading power of the polynomial
        #If the powers are 1 or 0 then the formatting of those terms doesn't need superscripts or even the X
        if (i != len(poly) - 1 and i != len(poly) - 2):
            term = "X^" + str(k)
        elif i == len(poly) - 2:
            term = "X"
        else:
            term = ""

        #Reduce modulo mod if necessary
        if poly[i] >= mod or poly[i] < 0:
            poly[i] = poly[i] - mod * (poly[i]//mod)
        
        #If the coefficient is 1 or 0 then it doesn't need to be shown
        if(poly[i] != 0 and (poly[i] != 1 or i == len(poly) - 1)):
            term = str(poly[i]) + term

        #The leading term does not need a + and if it is 0 then the following term doesn't need a plus either
        if (k != len(poly) - 1 and not (k == len(poly) - 2 and poly[0] == 0)):
                term = "+" + term
        
        #If the coefficient is 0 then the entire term doesn't need to be shown
        if (poly[i] != 0):
            s = s + term
    
    #Print and return the result
    return s, elim_lead_zeros(poly)
    
#print(display_poly(5,[5,1,1,-2,1,3,2,1,1,1,1,1,1,24,1,0]))
#print(display_poly(7,[0,0]))