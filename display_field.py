from longdivision import long_div_poly
from display_poly import display_poly

def display_field(mod,f,a):
    result = long_div_poly(mod,a,f)[3]
    return display_poly(mod,result)[0],result

print(display_field(5,[1,0,2],[1,0,0]))
print(display_field(7,[2,-2],[1,1,1]))    