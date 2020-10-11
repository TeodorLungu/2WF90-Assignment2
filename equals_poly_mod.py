from longdivision import long_div_poly
from longdivision import mul_poly
from longdivision import sub_poly
from longdivision import mod_inverse
from longdivision import lc
from longdivision import display_poly
from longdivision import reduction
from longdivision import add_poly
from longdivision import deg
from longdivision import elim_lead_zeros


def equals_poly_mod(mod, f, g, h):
    f = display_poly(mod,f)[1]
    g = display_poly(mod,g)[1]
    h = display_poly(mod,h)[1]
    fh = long_div_poly(mod,f,h)[3]
    gh = long_div_poly(mod,g,h)[3]
    return (fh==gh)

print(equals_poly_mod(3, [1,4,4], [1,6,24,8], [1,2]))