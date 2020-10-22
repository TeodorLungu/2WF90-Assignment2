### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
from variousFunctions import elim_lead_zeros
from display_poly import display_poly
from variousFunctions import deg
from variousFunctions import reduction
from generateFF import generate_ff
from mul_poly import mul_poly
from longdivision import long_div_poly
import math as m
from variousFunctions import isPrime


def mul_table(mod,f):
    if isPrime(mod)==False:
        return "ERROR"

    size=int(m.pow(mod,deg(f)))

    #Create empty matrices for the result
    Matrix= [[0 for x in range(size)] for y in range(size)]
    MatrixPretty = [['0' for x in range(size)] for y in range(size)] 

    Field=generate_ff(mod,f)[1] #Generate the field for modulo mod and the modulo polynomial f

    #Multiply each element in the field with all the elements in the field
    for i in range(size):
        for j in range(size):
            Matrix[i][j] = mul_poly(mod,Field[i],Field[j])[1] #Multiplication of two elements of the field
            Matrix[i][j] = long_div_poly(mod,Matrix[i][j],f)[3] #Reduce the calculated product with the modulo polynomial
            MatrixPretty[i][j]=display_poly(mod,Matrix[i][j])[0] #Reduce the coefficients
    return MatrixPretty,Matrix  

#print(mul_table(2,[1,1,1]))    