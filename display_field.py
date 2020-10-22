### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from longdivision import long_div_poly
from display_poly import display_poly
from variousFunctions import isPrime


def display_field(mod,f,a):
    if isPrime(mod)==False:
        return "ERROR"
    result = long_div_poly(mod,a,f)[3] #Execute division by the polynomial modulo
    return display_poly(mod,result)[0],result #Reduce the coefficients

#print(display_field(5,[1,0,2],[1,0,0]))
#(display_field(7,[2,-2],[1,1,1]))  
  