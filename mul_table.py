from variousFunctions import elim_lead_zeros
from display_poly import display_poly
from variousFunctions import deg
from variousFunctions import reduction
from generateFF import generate_ff
from mul_poly import mul_poly
from longdivision import long_div_poly
import math as m

def mul_table(mod,f):
    size=int(m.pow(mod,deg(f)))
    Matrix= [[0 for x in range(size)] for y in range(size)]
    MatrixPretty = [['0' for x in range(size)] for y in range(size)] 
    Field=generate_ff(mod,f)[1]
    for i in range(size):
        for j in range(size):
            Matrix[i][j]=mul_poly(mod,Field[i],Field[j])[1]
            Matrix[i][j]=long_div_poly(mod,Matrix[i][j],f)[3]
            MatrixPretty[i][j]=display_poly(mod,Matrix[i][j])[0]
    return MatrixPretty,Matrix  

(mul_table(7,[1,0]))    