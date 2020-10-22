### AfS software assignment 1 ###
# ### Group 22 ###
# ### Paul Zelina; Ana Popa; Teodor Lungu; Radu Lucian Radulescu ###
# ### 1431153;     1440098;  1416332;      1438808               ###
import random
from irreducible import irreducible
from variousFunctions import elim_lead_zeros
from display_poly import display_poly

def find_irred(mod,degree):
    #Direct implentation of algorithm 5.1.6
    polynom = [random.randint(0,mod-1) for i in range(degree+1)]  #Construct a random polynomial
    polynom[0] = random.randint(1,mod-1)
    while (irreducible(mod,polynom)==False):
        polynom = [random.randint(0,mod-1) for i in range(degree+1)]
        polynom[0] = random.randint(1,mod-1)
    polynom=elim_lead_zeros(polynom) #Eliminate potential leading zeros
    return display_poly(mod,polynom)[0],polynom

#(find_irred(2,3))