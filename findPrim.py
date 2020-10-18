from primitive import primitive
from primitive import exponentiation
from generateFF import generate_ff
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
import random

def find_prim(mod,mod_poly):
    degree = deg(mod_poly)
    q = mod**degree
    q = q - 1
    prime_divisors, k = primeDivisors(q)
    field = generate_ff(mod,mod_poly)[1]
    r = random.randint(0, len(field) - 1)
    a = field[r]
    while not(primitive(mod,mod_poly,a)):
        r = random.randint(0, len(field) - 1)
        a = field[r]
    return a

print(find_prim(3,[1,0,0,1,-1]))