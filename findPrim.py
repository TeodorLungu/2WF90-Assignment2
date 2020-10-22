### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
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
from variousFunctions import isPrime
from irreducible import irreducible


def find_prim(mod,mod_poly):
    if isPrime(mod)==False: #Check if mod is prime
        return "ERROR"
    if not(irreducible(mod,mod_poly)):
        return "ERROR"
    degree = deg(mod_poly)
    q = mod**degree
    q = q - 1
    prime_divisors, k = primeDivisors(q) #Obtain the prime divisors of q
    field = generate_ff(mod,mod_poly)[1] #Generate the field based on the mod and the polynomial modulo
    r = random.randint(0, len(field) - 1) #Randomly select an element from the field
    a = field[r]

    #Direct implementation of algorithm 4.4.4
    while not(primitive(mod,mod_poly,a)):
        r = random.randint(0, len(field) - 1)
        a = field[r]
    elim_lead_zeros(a)
    return display_field(mod,mod_poly,a)

#print(find_prim(7,[1,0,1]))
#print(primitive(7,[1,0,1],[6,3]))
#print(primitive(7,[1,0,1],[6,2]))
#print(primitive(7,[1,0,6],[2,2]))