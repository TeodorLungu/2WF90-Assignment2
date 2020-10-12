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

def extended_euclid(mod,a,b):
    x = [1]
    y = [0]
    u = [0]
    v = [1]
    while b != [0]:
        q = long_div_poly(mod,a,b)[2]
        r = long_div_poly(mod,a,b)[3]
        a = b
        b = r
        xPrime = x
        yPrime = y
        x = u
        y = v
        u = sub_poly(mod,xPrime,mul_poly(mod,q,u)[1])[1]
        v = sub_poly(mod,yPrime,mul_poly(mod,q,v)[1])[1]
    inv_lc_a = mod_inverse(mod,lc(a))
    ila = [inv_lc_a]
    d = mul_poly(mod,a,ila)[1]
    fx = mul_poly(mod,x,ila)[1]
    fy = mul_poly(mod,y,ila)[1]
    return display_poly(mod,d)[0],display_poly(mod,fx)[0],display_poly(mod,fy)[0],d,fx,fy

extended_euclid(3,[1,0,2,1],[1,1,1])

