from variousFunctions import elim_lead_zeros
from display_poly import display_poly
from variousFunctions import deg
from variousFunctions import reduction
import math as m
from itertools import product 
  

def generate_ff(mod,f):
    size=int(m.pow(mod,deg(f)))   
    N=deg(f)
    field=[ele for ele in product(range(0, mod), repeat = N)]    
    fieldPretty=[ele for ele in product(range(0, mod), repeat = N)]

    for i in range(len(field)):
        field[i]=list(field[i]) 
        fieldPretty[i]=display_poly(mod,field[i])[0]
        if (fieldPretty[i]==''):
            fieldPretty[i]='0'
    return fieldPretty,field

print(generate_ff(7,[1,0])[1])