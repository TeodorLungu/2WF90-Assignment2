from mul_table import mul_table
from mul_poly import mul_poly
from longdivision import long_div_poly
from display_poly import display_poly


def mul_field(mod,f,a,b):
    g=mul_poly(mod,a,b)[1]
    g=long_div_poly(mod,g,f)[3]
    return display_poly(mod,g)[0],g

(mul_field(2,[1,1,1],[1,1],[1]))
