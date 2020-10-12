import random
from irreducible import irreducible
from variousFunctions import elim_lead_zeros
from display_poly import display_poly

def find_irred(mod,degree):
    polynom = [random.randint(0,mod-1) for i in range(degree+1)]
    polynom[0] = random.randint(1,mod-1)
    while (irreducible(mod,polynom)==False):
        polynom = [random.randint(0,mod-1) for i in range(degree+1)]
        polynom[0] = random.randint(1,mod-1)
    polynom=elim_lead_zeros(polynom)
    return display_poly(mod,polynom)[0],polynom

print(find_irred(2,6))