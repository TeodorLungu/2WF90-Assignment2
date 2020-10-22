### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from longdivision import long_div_poly
from mul_poly import mul_poly
from sub_poly import sub_poly
from variousFunctions import mod_inverse
from variousFunctions import lc
from display_poly import display_poly
from variousFunctions import reduction
from add_poly import add_poly
from variousFunctions import deg,isPrime
from variousFunctions import elim_lead_zeros


def equals_poly_mod(mod, f, g, h):
    if (isPrime(mod)==False or h==[0]):
        return False
    #Reduce the coefficients of f,g,h modulo mod
    f = display_poly(mod,f)[1]
    g = display_poly(mod,g)[1]
    h = display_poly(mod,h)[1]
    
    #Divide f and g by h
    fh = long_div_poly(mod,f,h)[3]
    gh = long_div_poly(mod,g,h)[3]

    return (fh==gh)

#(equals_poly_mod(3, [1,4,4], [1,6,24,8], [1,2]))