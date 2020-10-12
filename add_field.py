from add_table import add_table
from add_poly import add_poly
from longdivision import long_div_poly
from display_poly import display_poly


def add_field(mod,f,a,b):
    g=add_poly(mod,a,b)[1]
    g=long_div_poly(mod,g,f)[3]
    return display_poly(mod,g)[0],g

print(add_field(2,[1,1,1],[1,1],[1]))
