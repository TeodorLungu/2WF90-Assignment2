### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from add_table import add_table
from add_poly import add_poly
from longdivision import long_div_poly
from display_poly import display_poly
from variousFunctions import isPrime


def add_field(mod,f,a,b):
    if isPrime(mod)==False:
        return "ERROR"
    g=add_poly(mod,a,b)[1] #Regular additionn
    g=long_div_poly(mod,g,f)[3] #Reduce by the polynomial modulo
    return display_poly(mod,g)[0],g #Reduce the coefficients by modulo mod

#(add_field(2,[1,1,1],[1,1],[1]))
