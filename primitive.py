from display_poly import display_poly
from mul_poly import mul_poly
from sub_poly import sub_poly
from add_poly import add_poly
from mul_field import mul_field
from variousFunctions import reduction
from variousFunctions import mod_inverse
from variousFunctions import deg
from variousFunctions import elim_lead_zeros
from variousFunctions import lc
from variousFunctions import primeDivisors
from display_field import display_field

def exponentiation(mod,mod_poly,a,power):
    r = a
    for i in range(power - 1):
        r = mul_poly(mod, r, a)[1]
    return display_field(mod,mod_poly,r)[1]


def primitive(mod,mod_poly,a):
    degree = deg(mod_poly)
    q = mod**degree
    q = q - 1
    prime_divisors, k = primeDivisors(q)
    i = 1
    while exponentiation(mod, mod_poly, a, q//prime_divisors[i - 1]) != [1]:
        i = i + 1
        if (not(i <= k)):
            break
    if i <= k:
        return False
    else:
        return True

#print(primitive(3,[1,0,0,1,-1],[2,2,2,1]))
#print(primitive(3,[1,0,0,1,-1],[2,1,1,0]))
#print(primitive(5,[1,0,1,1],[3,3]))
#print(primitive(5,[1,0,1,1],[3,1]))