from display_poly import display_poly
from mul_poly import mul_poly
from sub_poly import sub_poly
from add_poly import add_poly
from variousFunctions import reduction
from variousFunctions import mod_inverse
from variousFunctions import deg
from variousFunctions import elim_lead_zeros
from variousFunctions import lc
from variousFunctions import isPrime
        
def long_div_poly(mod,a,b):
    if isPrime(mod)==False:
        return "ERROR"
    if deg(b) == 0: #Division with a scalar
        if (b==[0]):
            return "ERROR"
        digit = b[-1] #Take the scalar and store it in 'digit'
        digit = mod_inverse(mod,digit) #Find the inverse of the digit
        result = mul_poly(mod,a,[digit])[1] #Multiply the inverse of the digit with the polynomial
        r = [0] #Division with a scalar always has remainder 0 in finite fields
        return display_poly(mod,result)[0],display_poly(mod,r)[0],result,r #return pretty print and Poly

    maximum = max(len(a),len(b))
    q = [0 for i in range(maximum)] #Create empty quotient polynomial
    r = a #Remainder

    #Direct implementation of algorithm 2.2.6, hence no further explanation
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

    #Eliminate possible leading zeros
    q = elim_lead_zeros(q)
    r = elim_lead_zeros(r)
    return display_poly(mod,q)[0],display_poly(mod,r)[0],q,r

#print(long_div_poly(6,[5,2,3,4],[2,3,4,0]))
#print(long_div_poly(7,[6],[5]))
#print(long_div_poly(7,[1,1,1],[2,-2]))
#print(long_div_poly(7,[1,1,1],[0]))
