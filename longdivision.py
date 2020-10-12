from display_poly import display_poly
from mul_poly import mul_poly
from sub_poly import sub_poly
from add_poly import add_poly
from variousFunctions import reduction
from variousFunctions import mod_inverse
from variousFunctions import deg
from variousFunctions import elim_lead_zeros
from variousFunctions import lc
        
def long_div_poly(mod,a,b):
    if deg(b) == 0: #Division with a scalar
        digit = b[-1]
        digit = mod_inverse(mod,digit)
        result = mul_poly(mod,a,[digit])[1]
        r = [0]
        return display_poly(mod,result)[0],display_poly(mod,r)[0],result,r
    maximum = max(len(a),len(b))
    q = [0 for i in range(maximum)]
    r = a
    while deg(r)>=deg(b):
        x = [0 for i in range(maximum)]
        inv = mod_inverse(mod, lc(b))
        q_i = reduction(inv*lc(r),mod)
        d = deg(r) - deg(b)
        x[-(d+1)] = q_i
        q = add_poly(mod, q, x)[1]
        r = sub_poly(mod,r,mul_poly(mod,x,b)[1])[1]
        q = display_poly(mod,q)[1]
        r = display_poly(mod,r)[1]
    q = elim_lead_zeros(q)
    r = elim_lead_zeros(r)
    return display_poly(mod,q)[0],display_poly(mod,r)[0],q,r
