from mul_table import mul_table
from mul_poly import mul_poly
from longdivision import long_div_poly
from display_poly import display_poly
from variousFunctions import isPrime



def mul_field(mod,f,a,b):
    if isPrime(mod)==False:
        return "ERROR"
    g = mul_poly(mod,a,b)[1] #Regularly multiply the polynomials modulo mod
    g = long_div_poly(mod,g,f)[3] #Reduce by the modulo polynomial
    return display_poly(mod,g)[0],g #Reduce the coefficients and display

#print(mul_field(2,[1,1,1],[1,1],[1]))
